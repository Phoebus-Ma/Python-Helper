
# 1. Introduction

Tensorflow image recognition for fruits.


# 2. Enviorment

Windows 11:

Such as tensorflow-2.10.1:

- Python-3.10.11.exe.

Optional:

- cuda_11.2.0_460.89_win10.exe
- cudnn-11.2-windows-x64-v8.1.1.33.zip

Linux (Ubuntu 22.04):

```bash
$ sudo apt update
$ sudo apt install python3 python3-venv
```

Optional:

- Cuda 11.2

```bash
$ wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/cuda-ubuntu2004.pin
$ sudo mv cuda-ubuntu2004.pin /etc/apt/preferences.d/cuda-repository-pin-600
$ wget https://developer.download.nvidia.com/compute/cuda/11.2.0/local_installers/cuda-repo-ubuntu2004-11-2-local_11.2.0-460.27.04-1_amd64.deb
$ sudo dpkg -i cuda-repo-ubuntu2004-11-2-local_11.2.0-460.27.04-1_amd64.deb
$ sudo apt-key add /var/cuda-repo-ubuntu2004-11-2-local/7fa2af80.pub
$ sudo apt update
$ sudo apt -y install cuda
```

- libcudnn8-dev_8.1.1.33-1+cuda11.2_amd64.deb


# 3. Usage

Train the model (3.1 step), then use the model (3.2 step).

```bash
$ python -m pip install --upgrade pip
$ pip install -r requirements.txt
```

Or, you can use python virtual enviorment:

Windows 11:

```bash
$ py -3.10 -m venv "PyEnv1"
$ & PyEnv1\Scripts\Activate.ps1
(PyEnv1) $ python -m pip install --upgrade pip
(PyEnv1) $ pip install -r requirements.txt
```

Linux (Ubuntu 22.04):

```bash
$ sudo apt update
$ sudo apt install python3 python3-venv
$ python3 -m venv "PyEnv1"
$ source PyEnv/bin/activate
(PyEnv1) $ python3 -m pip install --upgrade pip 
(PyEnv1) $ pip install -r requirements.txt 
```

finally, on the end (optional):

```bash
(PyEnv1) $ deactivate
```


## 3.1 Train model

- Copy some pictures to "data/train" and "data/val" folder.
- The "data/train" folder contains 80% of the images, "data/val" contains 20%.
- The picture format need is jpeg, png, gif or bmp.

Directory structure:

"data/train" folder: 100 pictures per folder, "data/val" folder: 25 pictures per folder,
100 is just an example, you can use any number.

```bash
.
├─train
│  ├─apple
│  │      apple1.png
│  │      ...
│  │      apple100.png
│  │
│  ├─banana
│  │      banana1.png
│  │      ...
│  │      banana100.png
│  │
│  ├─orange
│  │      orange1.png
│  │      ...
│  │      orange100.png
│  │
│  └─watermelon
│          watermelon1.png
│          ...
│          watermelon100.png
│
└─val
    ├─apple
    │      apple1.png
    │      ...
    │      apple25.png
    │
    ├─banana
    │      banana1.png
    │      ...
    │      banana25.png
    │
    ├─orange
    │      orange1.png
    │      ...
    │      orange25.png
    │
    └─watermelon
            watermelon1.png
            ...
            watermelon25.png
```

Note: You can add fruits class, such as pear, grape, mango, etc.

1. Train mobilenet model:

```bash
$ python train_mobilenet.py
```

2. Train CNN model:

```bash
$ python train_cnn.py
```

If everything goes well, you get a model in "models" folder.


## 3.2 Test model

```bash
$ python test_model.py
```


## 3.3 Use model

Default use mobilenet model, you can edit "default_model" to use CNN model:

```bash
$ python main.py
```
