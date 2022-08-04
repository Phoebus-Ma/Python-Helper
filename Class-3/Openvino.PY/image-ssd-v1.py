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
from openvino.inference_engine import IECore


# Main function.
def main() -> int:
# {
    # 1. Get input parameters.
    # ----------------------------------------------------------------
    if 4 != len(sys.argv):
        print('Parameters error.')
        return -1

    model_name  = sys.argv[1]
    image_name  = sys.argv[2]
    device_name = sys.argv[3]

    # 2. Initialize inference engine core.
    # ----------------------------------------------------------------
    core = IECore()

    # 3. Read a model.
    # (.xml & .bin) or .onnx.
    # ----------------------------------------------------------------
    net = core.read_network(model_name)

    # 4. Configure input & output.
    # Get names of input and output blobs.
    # ----------------------------------------------------------------
    input_blob  = next(iter(net.input_info))
    out_blob    = next(iter(net.outputs))

    # Set input and output precision manually.
    net.input_info[input_blob].precision = 'U8'
    net.outputs[out_blob].precision      = 'FP32'

    # Read image.
    image       = cv.imread(image_name)

    # Resize image.
    _, _, h, w  = net.input_info[input_blob].tensor_desc.dims
    resize_img  = cv.resize(image, (w, h))
    output_img  = resize_img.copy()

    # Change data layout from HWC to CHW.
    resize_img  = resize_img.transpose((2, 0, 1))

    # Add N dimension to transform to NCHW.
    resize_img  = np.expand_dims(resize_img, 0)

    # 5. Loading model to the device.
    # ----------------------------------------------------------------
    exec_net    = core.load_network(net, device_name)

    # 6. Do inference.
    # ----------------------------------------------------------------
    res = exec_net.infer({input_blob: resize_img})

    # 7. Process output.
    # ----------------------------------------------------------------
    res = res[out_blob]

    # Change a shape of a numpy.ndarray with results ([1, 1, N, 7]) to get
    # another one ([N, 7]), where N is the number of detected bounding boxes.
    detections = res.reshape(-1, 7)

    for detection in detections:
        confidence = detection[2]
        if confidence > 0.5:
            xmin = int(detection[3] * w)
            ymin = int(detection[4] * h)
            xmax = int(detection[5] * w)
            ymax = int(detection[6] * h)

            print(f'Found: confidence = {confidence:.2f}, ' f'coords = ({xmin}, {ymin}), ({xmax}, {ymax})')

            # Draw a bounding box on a output image.
            cv.rectangle(output_img, (xmin, ymin), (xmax, ymax), (0, 255, 0), 2)

    cv.imshow('Result image', output_img)

    cv.waitKey(0)
    cv.destroyAllWindows()

    return 0
# }


# Program entry.
if '__main__' == __name__:
# {
    sys.exit(main())
# }
