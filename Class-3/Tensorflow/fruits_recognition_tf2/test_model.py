###
# Test ai model.
#
# License - MIT.
###

import tensorflow as tf
import numpy as np


# Loading dataset.
# Load the training set and validation set from the training dataset folder
# and the test folder respectively.
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


# Test the accuracy of the mobilenet model.
def test_mobilenet():
# {
    # Load data.
    train_ds, test_ds, class_names = data_load(train_folder, val_folder, 224, 224, 16)

    # Load model.
    model = tf.keras.models.load_model(mobilenet_model)
    model.summary()

    # Test.
    loss, accuracy = model.evaluate(test_ds)

    print('Mobilenet model loss: %.3f, accuracy: %.3f' % (loss, accuracy))
    print('--------------------------------')

    # Reasoning about the model separately.
    test_real_labels = []
    test_pre_labels  = []

    for test_batch_images, test_batch_labels in test_ds:
        test_batch_labels = test_batch_labels.numpy()
        test_batch_pres   = model.predict(test_batch_images)

        test_batch_labels_max = np.argmax(test_batch_labels, axis = 1)
        test_batch_pres_max   = np.argmax(test_batch_pres,   axis = 1)

        # The label corresponding to the inference is taken out.
        for i in test_batch_labels_max:
            test_real_labels.append(i)

        for i in test_batch_pres_max:
            test_pre_labels.append(i)

    class_names_length = len(class_names)
    heat_maps          = np.zeros((class_names_length, class_names_length))

    for test_real_label, test_pre_label in zip(test_real_labels, test_pre_labels):
        heat_maps[test_real_label][test_pre_label] = heat_maps[test_real_label][test_pre_label] + 1

    print(heat_maps)
    print('--------------------------------')

    heat_maps_sum   = np.sum(heat_maps, axis = 1).reshape(-1, 1)
    heat_maps_float = heat_maps / heat_maps_sum

    print(heat_maps_float)
    print('--------------------------------')
# }


# Test the accuracy of the CNN model.
def test_cnn():
# {
    # Load data.
    train_ds, test_ds, class_names = data_load(train_folder, val_folder, 224, 224, 16)

    # Load model.
    model = tf.keras.models.load_model(cnn_model)
    model.summary()

    # Test model.
    loss, accuracy = model.evaluate(test_ds)

    print('CNN model loss: %.3f, accuracy: %.3f' % (loss, accuracy))
    print('--------------------------------')

    # Reasoning about the model separately.
    test_real_labels = []
    test_pre_labels  = []

    for test_batch_images, test_batch_labels in test_ds:
        test_batch_labels = test_batch_labels.numpy()
        test_batch_pres   = model.predict(test_batch_images)

        test_batch_labels_max = np.argmax(test_batch_labels, axis = 1)
        test_batch_pres_max   = np.argmax(test_batch_pres, axis = 1)

        # The label corresponding to the inference is taken out.
        for i in test_batch_labels_max:
            test_real_labels.append(i)

        for i in test_batch_pres_max:
            test_pre_labels.append(i)

    class_names_length = len(class_names)
    heat_maps          = np.zeros((class_names_length, class_names_length))

    for test_real_label, test_pre_label in zip(test_real_labels, test_pre_labels):
        heat_maps[test_real_label][test_pre_label] = heat_maps[test_real_label][test_pre_label] + 1

    print(heat_maps)
    print('--------------------------------')

    heat_maps_sum   = np.sum(heat_maps, axis = 1).reshape(-1, 1)
    heat_maps_float = heat_maps / heat_maps_sum

    print(heat_maps_float)
    print('--------------------------------')
# }


if '__main__' == __name__:
    train_folder    = 'data/train'
    val_folder      = 'data/val'
    mobilenet_model = 'models/mobilenet_fruits.h5'
    cnn_model       = 'models/cnn_fruits.h5'

    print('====================================')
    print('--------Test Mobilenet model--------')
    test_mobilenet()

    print('====================================')
    print('--------Test CNN model--------------')
    test_cnn()
