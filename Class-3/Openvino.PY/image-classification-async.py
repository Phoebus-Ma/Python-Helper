###
# Openvino image classification.
#
# License - MIT.
###

from genericpath import isdir
import os
import sys

# pip install opencv-python numpy pandas
import cv2 as cv
import numpy as np

from glob import glob

# pip install openvino-dev[caffe,onnx,tensorflow2,pytorch,mxnet]
from openvino.preprocess import PrePostProcessor
from openvino.runtime import Core, Layout, Type, AsyncInferQueue, InferRequest


# infer callback function.
def infer_callback(infer_request: InferRequest, image_path: str) -> None:
# {
    objects = next(iter(infer_request.results.values()))
    index = np.argmax(objects, 1)[0]

    print('%s, probability: %.7f.' \
        % (labels[index], objects[0][index]))
# }


# Main function.
def main() -> int:
# {
    # 1.Get parameters.
    # ----------------------------------------------------------------
    if 4 != len(sys.argv):
        print('Parameter error.')
        return -1

    model_name  = sys.argv[1]
    image_path  = sys.argv[2]
    device_name = sys.argv[3]

    if not os.path.isdir(image_path):
        print('Error in image path.')
        return -1

    # 2.Init openvino core.
    # ----------------------------------------------------------------
    core = Core()

    # 3.Read model.
    # ----------------------------------------------------------------
    model = core.read_model(model_name)

    # 4.Read image.
    # ----------------------------------------------------------------
    # Opencv read images.
    images = [cv.imread(image) for image in glob(image_path)]

    # Resize images to model input dims
    _, _, h, w = model.input().shape
    resize_imgs = [cv.resize(image, (w, h)) for image in images]

    # Expand dimension.
    input_tensors = [np.expand_dims(image, 0) for image in resize_imgs]

    # 5.PreProcessing.
    # ----------------------------------------------------------------
    ppp = PrePostProcessor(model)

    # 5.1 Set input information.
    ppp.input().tensor() \
        .set_element_type(Type.u8) \
            .set_layout(Layout('NHWC'))

    # 5.2 NHWC to NCHW.
    ppp.input().model().set_layout(Layout('NCHW'))

    # 5.3 Set output tensor information.
    ppp.output().tensor().set_element_type(Type.f32)

    # 5.4 Apply settings.
    model = ppp.build()

    # 6.Loading model to device.
    # ----------------------------------------------------------------
    compiled_model = core.compile_model(model, device_name)

    # 7.infer.
    # ----------------------------------------------------------------
    infer_queue = AsyncInferQueue(compiled_model)
    infer_queue.set_callback(infer_callback)

    # 8.Start infer.
    for i, input_tensor in enumerate(input_tensors):
        infer_queue.start_async({0: input_tensor}, images[i])

    infer_queue.wait_all()

    return 0
# }


# Program entry.
if '__main__' == __name__:
# {
    with open('imagenet_classes.txt', 'r') as f:
        labels = [line.strip() for line in f.readlines()]

    sys.exit(main())
# }
