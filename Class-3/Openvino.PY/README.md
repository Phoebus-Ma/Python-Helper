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

1. image-classification.py          ---- Image classification for deep learning model.
2. image-classification-async.py    ---- Asynchronous Image classification for deep learning model.
3. image-ssd-v1.py                  ---- Image SSD test, Note: It may no longer be available in the latest version.
4. image-ssd-v2.py                  ---- Image SSD test version 2.


### Example:

1. Image classification test:

*Note: In addition to googlenet-v1 model file, you can use other model files, such as alexnet.*

```console
$ python image-classification.py public/googlenet-v1/FP32/googlenet-v1.xml images/banana.jpg GPU

banana, probability: 0.9990779.

$ python image-classification.py public/googlenet-v1/FP32/googlenet-v1.xml images/car.bmp CPU

minivan, probability: 0.8150495.
```

2. Image classification async test:

*Note: In addition to googlenet-v1 model file, you can use other model files, such as alexnet.*

```console
$ copy images/banana.jpg images/banana1.jpg
$ copy images/banana.jpg images/banana2.jpg
$ copy images/banana.jpg images/banana3.jpg
$ python image-classification-async.py public/googlenet-v1/FP32/googlenet-v1.xml images/*.jpg CPU

banana, probability: 0.9990778.
banana, probability: 0.9990778.
banana, probability: 0.9990778.
banana, probability: 0.9990778.
```

3. Image ssd test:

*Note: you can use mobilenet-ssd, ssdlite_mobilenet_v2, person-detection-retail-0013, etc.*
*Warning: It may no longer be available in the latest version.*

```console
$ omz_downloader --name mobilenet-ssd
$ omz_converter --name mobilenet-ssd
$ python image-ssd-v1.py public/mobilenet-ssd/FP32/mobilenet-ssd.xml images/banana.jpg GPU

Found: confidence = 0.58, coords = (21, 97), (279, 216)
```

4. Image ssd test version 2:

```console
$ omz_downloader --name person-detection-retail-0013
$ python image-ssd-v2.py intel/person-detection-retail-0013/FP32/person-detection-retail-0013.xml images/person_detection.png CPU

Found: confidence = 0.72, coords = (852, 187), (983, 520)
```

### Resource

- https://raw.githubusercontent.com/pytorch/hub/master/imagenet_classes.txt

- https://storage.openvinotoolkit.org/data/test_data/images/banana.jpg

- https://storage.openvinotoolkit.org/data/test_data/images/car.bmp
