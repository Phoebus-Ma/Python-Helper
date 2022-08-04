###
# Openvino image ssd test.
#
# License - MIT.
###

import sys

# pip install opencv-python numpy
import cv2 as cv
import numpy as np

# pip install openvino-dev[caffe,onnx,tensorflow2,pytorch,mxnet]
from openvino.preprocess import PrePostProcessor
from openvino.runtime import Core, Layout, PartialShape, Type


# Main function.
def main() -> int:
# {
    # 1. Get input parameters.
    # ----------------------------------------------------------------
    if 4 != len(sys.argv):
        print(f'Usage: {sys.argv[0]} <path_to_model> <path_to_image> <device_name>')
        return 1

    model_name  = sys.argv[1]
    image_name  = sys.argv[2]
    device_name = sys.argv[3]

    # 2. Initialize OpenVINO Runtime Core.
    # ----------------------------------------------------------------
    core = Core()

    # 3. Read a model.
    # (.xml & .bin) or .onnx.
    # ----------------------------------------------------------------
    model = core.read_model(model_name)

    # 4. Set up input.
    # ----------------------------------------------------------------

    # Read input image
    image = cv.imread(image_name)

    # Add N dimension
    input_tensor = np.expand_dims(image, 0)

    # Reshaping the model to the height and width of the input image.
    n, h, w, c = input_tensor.shape
    model.reshape({model.input().get_any_name(): PartialShape((n, c, h, w))})

    # 5. Apply preprocessing.
    # ----------------------------------------------------------------
    ppp = PrePostProcessor(model)

    # 1) Set input tensor information:
    # - input() provides information about a single model input
    # - precision of tensor is supposed to be 'u8'
    # - layout of data is 'NHWC'
    ppp.input().tensor() \
        .set_element_type(Type.u8) \
        .set_layout(Layout('NHWC'))  # noqa: N400

    # 2) Here we suppose model has 'NCHW' layout for input
    ppp.input().model().set_layout(Layout('NCHW'))

    # 3) Set output tensor information:
    # - precision of tensor is supposed to be 'f32'
    ppp.output().tensor().set_element_type(Type.f32)

    # 4) Apply preprocessing modifing the original 'model'
    model = ppp.build()

    # 6. Loading model to the device.
    # ----------------------------------------------------------------
    compiled_model = core.compile_model(model, device_name)

    # 7. Create infer request and do inference synchronously.
    # ----------------------------------------------------------------
    results = compiled_model.infer_new_request({0: input_tensor})

    # 8. Process output.
    # ----------------------------------------------------------------
    predictions = next(iter(results.values()))

    # Change a shape of a numpy.ndarray with results ([1, 1, N, 7]) to get another one ([N, 7]),
    # where N is the number of detected bounding boxes
    detections = predictions.reshape(-1, 7)

    for detection in detections:
        confidence = detection[2]

        if confidence > 0.5:
            xmin = int(detection[3] * w)
            ymin = int(detection[4] * h)
            xmax = int(detection[5] * w)
            ymax = int(detection[6] * h)

            print(f'Found: confidence = {confidence:.2f}, ' f'coords = ({xmin}, {ymin}), ({xmax}, {ymax})')

            # Draw a bounding box on a output image
            cv.rectangle(image, (xmin, ymin), (xmax, ymax), (0, 255, 0), 2)

    cv.imshow('Result image', image)

    cv.waitKey(0)
    cv.destroyAllWindows()

    return 0
# }


# Program entry.
if '__main__' == __name__:
# {
    sys.exit(main())
# }
