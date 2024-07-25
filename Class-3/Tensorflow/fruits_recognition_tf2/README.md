
# 1. Introduction

Tensorflow image recognition for fruits.


# 2. Enviorment

On Windows:

Such as tensorflow-2.10.1:

- Python-3.10.11.exe.

optional:

- cuda_11.2.0_460.89_win10.exe
- cudnn-11.2-windows-x64-v8.1.1.33.zip


# 3. Usage

Train the model (3.1 step), then use the model (3.2 step).

```bash
$ python -m pip install --upgrade pip
$ pip install -r requirements.txt
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

```bash
$ python train_mobilenet.py
```

If everything goes well, you get a model in "models" folder.


## 3.2 Use model

```bash
$ python main.py
```
