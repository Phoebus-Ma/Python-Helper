### Description

Pytorch test for python.


### Platform

Python 3 for Windows/Linux/MacOS.


### Install

```console
$ python -m pip install matplotlib numpy
```

If your pc have not GPU:
```console
$ python -m pip3 install torch torchvision torchaudio
```

If your pc have nvidia GPU:

1. First, you need run nvidia smi tool to get gpu support cuda version:
```console
$ nvidia-smi
```

*on Windows: C:\Program Files\NVIDIA Corporation\NVSMI\nvidia-smi.exe*

2. such as support cuda version 11.3, run:

```console
$ python -m pip3 install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu113
```

if your gpu support others cuda version, you can find install command in here:
(Previous version)[https://pytorch.org/get-started/previous-versions/]


### Feature

1. base-linear.py           ---- Pytorch Linear regression machine learning example.


### Example:

1. Linear regression machine learning test:
```console
$ python base-linear.py

Iteration: 0 w0: -0.05 w1: -0.46 b: 0.133549 accuracy:92.00%
Iteration: 10 w0: -0.95 w1: -1.13 b: 0.307991 accuracy:93.50%
Iteration: 20 w0: -3.30 w1: -2.85 b: 1.092746 accuracy:94.00%
Iteration: 30 w0: -6.13 w1: -4.94 b: 2.562052 accuracy:95.00%
Iteration: 40 w0: -8.95 w1: -7.08 b: 4.621525 accuracy:95.50%
Iteration: 50 w0: -11.56 w1: -9.18 b: 7.176139 accuracy:97.00%
Iteration: 60 w0: -13.91 w1: -11.21 b: 10.142098 accuracy:97.50%
Iteration: 70 w0: -15.99 w1: -13.18 b: 13.443925 accuracy:98.00%
Iteration: 80 w0: -17.82 w1: -15.10 b: 17.020126 accuracy:98.00%
Iteration: 90 w0: -19.43 w1: -16.98 b: 20.825619 accuracy:98.50%
Iteration: 100 w0: -20.83 w1: -18.82 b: 24.822052 accuracy:99.00%
Iteration: 110 w0: -22.06 w1: -20.63 b: 28.968710 accuracy:99.00%
Iteration: 120 w0: -23.17 w1: -22.41 b: 33.232208 accuracy:99.50%
```

2. test:
```console
$ 
```


### Resource

- https://pytorch.org/

- https://github.com/pytorch
