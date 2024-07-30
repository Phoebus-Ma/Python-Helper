###
# Tensorflow2 train CNN model.
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


# Building the CNN model.
def model_load(IMG_SHAPE = (224, 224, 3), class_num = 12):
# {
    # Building the Model.
    model = tf.keras.models.Sequential([
        # Normalize the model and convert numbers between 0 and 255 to between 0 and 1.
        tf.keras.layers.experimental.preprocessing.Rescaling(1. / 255, input_shape = IMG_SHAPE),

        # Convolution layer, the output of this convolution layer is 32 channels,
        # the size of the convolution kernel is 3 * 3, and the activation function is relu.
        tf.keras.layers.Conv2D(32, (3, 3), activation = 'relu'),

        # Add a pooling layer, the kernel size of the pooling is 2 * 2.
        tf.keras.layers.MaxPooling2D(2, 2),

        # Add another convolution.
        # Convolution layer, output is 64 channels,
        # convolution kernel size is 3 * 3, activation function is relu.
        tf.keras.layers.Conv2D(64, (3, 3), activation = 'relu'),

        # Pooling layer, maximum pooling, pooling operation on 2 * 2 area.
        tf.keras.layers.MaxPooling2D(2, 2),

        # Convert the two-dimensional output to one-dimensional.
        tf.keras.layers.Flatten(),

        # The same 128 dense layers, and 10 output layers as in the pre-convolution example:
        tf.keras.layers.Dense(128, activation = 'relu'),

        # The model is output as a neuron of class name length through the softmax function,
        # and the activation function uses the probability value corresponding to softmax.
        tf.keras.layers.Dense(class_num, activation = 'softmax')
    ])

    # Output information.
    model.summary()

    # The optimizer of the model training is sgd optimizer,
    # and the loss function of the model is the cross-entropy loss function.
    model.compile(optimizer = 'sgd', loss = 'categorical_crossentropy', metrics = ['accuracy'])

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
    model = model_load(class_num = len(class_names))

    # Specify the number of training epochs and start training.
    history = model.fit(train_ds, validation_data = val_ds, epochs = epochs)

    # Save the model.
    model.save(default_model)

    # Record end time.
    end_time = time()
    run_time = end_time - begin_time

    print('Total running time: ', run_time, 's')
# }


if '__main__' == __name__:
    train_folder  = 'data/train'
    val_folder    = 'data/val'
    default_model = 'models/cnn_fruits.h5'

    # train times.
    train(epochs = 50)
