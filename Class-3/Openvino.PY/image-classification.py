###
# Openvino image classification.
#
# License - MIT.
###

import os
import sys

# pip install opencv-python numpy pandas
import cv2 as cv
import numpy as np

# pip install openvino-dev[caffe,onnx,tensorflow2,pytorch,mxnet]
from openvino.preprocess import PrePostProcessor, ResizeAlgorithm
from openvino.runtime import Core, Layout, Type


# Main function.
def main() -> int:
# {
    # 1.Get parameters.
    # ----------------------------------------------------------------
    if 4 != len(sys.argv):
        print('Parameter error.')
        return -1

    model_name  = sys.argv[1]
    image_name  = sys.argv[2]
    device_name = sys.argv[3]

    with open('imagenet_classes.txt', 'r') as f:
        labels = [line.strip() for line in f.readlines()]

    # 2.Init openvino core.
    # ----------------------------------------------------------------
    core = Core()

    # 3.Read model.
    # ----------------------------------------------------------------
    model = core.read_model(model_name)

    # 4.Read image.
    # ----------------------------------------------------------------
    image = cv.imread(image_name)

    # Resize images to model input dims
    _, _, h, w = model.input().shape
    resize_img = cv.resize(image, (w, h))

    # Expand dimension.
    input_tensor = np.expand_dims(resize_img, 0)

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
    results = compiled_model.infer_new_request({0: input_tensor})

    # 8.Process output data.
    # ----------------------------------------------------------------
    objects = next(iter(results.values()))
    index = np.argmax(objects, 1)[0]

    print('%s, probability: %.7f.' \
        % (labels[index], objects[0][index]))

    return 0
# }


# Program entry.
if '__main__' == __name__:
# {
    sys.exit(main())
# }
