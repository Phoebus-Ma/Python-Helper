### Description

Openvino test for python.


### Platform

Python 3.6~3.8 for Windows/Linux/MacOS.


### Install

- Step 1:

```console
$ python -m pip install opencv-python numpy pandas
$ python -m pip install openvino-dev[caffe,onnx,tensorflow2,pytorch,mxnet]
$ omz_downloader --name googlenet-v1
$ omz_converter --name googlenet-v1
```

- Step 2:

[download banana image](https://storage.openvinotoolkit.org/data/test_data/images/banana.jpg)
[download car image](https://storage.openvinotoolkit.org/data/test_data/images/car.bmp)


### Feature

1. image-classification.py      ---- Image classification for deep learning model.


### Example:

1. Image classification test:
```console
$ python image-classification.py public/googlenet-v1/FP32/googlenet-v1.xml banana.jpg GPU

banana, probability: 0.9990779.

$ python image-classification.py public/googlenet-v1/FP32/googlenet-v1.xml car.bmp CPU

minivan, probability: 0.8150495.
```

2. test:
```console
$ 
```

### Resource

- https://raw.githubusercontent.com/pytorch/hub/master/imagenet_classes.txt

- https://storage.openvinotoolkit.org/data/test_data/images/banana.jpg

- https://storage.openvinotoolkit.org/data/test_data/images/car.bmp
