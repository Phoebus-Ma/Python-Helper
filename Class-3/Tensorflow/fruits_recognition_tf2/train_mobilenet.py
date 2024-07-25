###
# Tensorflow train mobilenet model.
#
# License - MIT.
###

import tensorflow as tf
import matplotlib.pyplot as plt
from time import *


# Loading dataset.
# Specify the location of the dataset and treat it as imgheight * imgwidth, and set the batch.
def data_load(data_dir, test_data_dir, img_height, img_width, batch_size):
# {
    # Loading the training set.
    train_ds = tf.keras.preprocessing.image_dataset_from_directory(
        data_dir,
        label_mode = 'categorical',
        seed       = 123,
        image_size = (img_height, img_width),
        batch_size = batch_size)

    # Loading the test set.
    val_ds = tf.keras.preprocessing.image_dataset_from_directory(
        test_data_dir,
        label_mode = 'categorical',
        seed       = 123,
        image_size = (img_height, img_width),
        batch_size = batch_size)

    class_names = train_ds.class_names

    # Returns the processed training set, validation set, and class names.
    return train_ds, val_ds, class_names
# }


# Building the mobilenet model.
# Load the model, specify the size of the image processing and whether to perform transfer learning.
def model_load(IMG_SHAPE=(224, 224, 3), class_num=12):
# {
    # Normalization is not needed in the process of fine-tuning.
    # Loading the pre-trained mobilenet model.
    base_model = tf.keras.applications.MobileNetV2(input_shape = IMG_SHAPE,
                                                   include_top = False,
                                                   weights     = 'imagenet')

    # The backbone parameters of the model are frozen.
    base_model.trainable = False
    model = tf.keras.models.Sequential([
        # Perform normalization.
        tf.keras.layers.experimental.preprocessing.Rescaling(1. / 127.5, offset=-1, input_shape=IMG_SHAPE),

        # Set up the backbone model.
        base_model,

        # Global average pooling is performed on the output of the backbone model.
        tf.keras.layers.GlobalAveragePooling2D(),

        # It is mapped to the final number of classes through the fully connected layer.
        tf.keras.layers.Dense(class_num, activation='softmax')
    ])

    model.summary()

    # The optimizer of the model training is adam optimizer,
    # and the loss function of the model is the cross-entropy loss function.
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

    return model
# }


# Train model.
def train(epochs):
# {
    # Start training and record the start time.
    begin_time = time()

    # Loading the dataset.
    train_ds, val_ds, class_names = data_load(train_folder, val_folder, 224, 224, 16)
    print(class_names)

    # Loading the model.
    model = model_load(class_num=len(class_names))

    # Specify the number of training epochs and start training.
    history = model.fit(train_ds, validation_data=val_ds, epochs=epochs)

    # Save the model.
    model.save(default_model)

    # Record end time.
    end_time = time()
    run_time = end_time - begin_time

    print('Total running time', run_time, 's')
# }


if '__main__' == __name__:
    train_folder  = 'data/train'
    val_folder    = 'data/val'
    default_model = 'models/mobilenet_fruits.h5'

    train(epochs=50)
