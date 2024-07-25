###
# Tensorflow image recognition for fruits.
#
# License - MIT.
###

import tensorflow as tf
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys
import cv2
from PIL import Image
import numpy as np


class MainWindow(QWidget):
# {
    def __init__(self):
    # {
        super().__init__()

        # Application title.
        self.setWindowTitle('Fruits recognition')

        # Model.
        self.model = tf.keras.models.load_model(default_model)

        # Default display picture.
        self.display_picture = default_picture

        # Index of fruits class name.
        self.class_names = [
            'apple',
            'banana',
            'orange',
            'watermelon'
        ]

        self.resize(900, 700)
        self.initUI()
    # }


    # Set UI.
    def initUI(self):
    # {
        # Left Layout.
        # --------------------------------
        left_widget    = QWidget()
        left_layout    = QVBoxLayout()
        self.img_label = QLabel()

        # Image preprocessing.
        img_init = cv2.imread(self.display_picture)
        h, w, c  = img_init.shape
        scale    = 400 / h
        img_init = cv2.resize(img_init, (224, 224))
        cv2.imwrite('images/target.png', img_init)

        # Image label.
        self.img_label.setPixmap(QPixmap('images/target.png'))

        left_layout.addWidget(self.img_label, 1, Qt.AlignCenter)
        left_widget.setLayout(left_layout)


        # Right layout.
        # --------------------------------
        right_widget = QWidget()
        right_layout = QVBoxLayout()
        font         = QFont('Helvetica', 15)

        # Button 1.
        btn_change   = QPushButton('Upload picture')
        btn_change.clicked.connect(self.change_img)
        btn_change.setFont(font)

        # Button 2.
        btn_predict  = QPushButton('Start recognition')
        btn_predict.clicked.connect(self.predict_img)
        btn_predict.setFont(font)

        # Label 1.
        label_result = QLabel('Fruit name')
        label_result.setFont(QFont('Helvetica', 16))

        # Label 2.
        self.result  = QLabel('Waiting for recognition')
        self.result.setFont(QFont('Helvetica', 24))

        right_layout.addStretch()
        right_layout.addWidget(label_result, 0, Qt.AlignCenter)
        right_layout.addStretch()
        right_layout.addWidget(self.result,  0, Qt.AlignCenter)
        right_layout.addStretch()
        right_layout.addStretch()
        right_layout.addWidget(btn_change)
        right_layout.addWidget(btn_predict)
        right_layout.addStretch()

        right_widget.setLayout(right_layout)


        # Main layout
        # --------------------------------
        main_layout = QHBoxLayout()
        main_layout.addWidget(left_widget)
        main_layout.addWidget(right_widget)

        self.setLayout(main_layout)
    # }


    # Load local image and display.
    def change_img(self):
    # {
        openfile_name = QFileDialog.getOpenFileName(
                            self, 'chose files', '', 'Image files(*.jpg *.png *jpeg)')
        img_name = openfile_name[0]

        if img_name == '':
            pass
        else:
            img_init = cv2.imread(img_name)
            h, w, c  = img_init.shape
            scale    = 400 / h

            img_init = cv2.resize(img_init, (224, 224)) # Resize the image to 224 * 224.
            cv2.imwrite('images/target.png', img_init)  # Save image to png.

            # Display selected image.
            self.img_label.setPixmap(QPixmap('images/target.png'))
            self.result.setText('Waiting for recognition')
    # }


    # Reasoning image.
    def predict_img(self):
    # {
        img          = Image.open('images/target.png')  # Read image.
        img          = np.asarray(img)                  # Convert the image to a numpy array.

        # Inference.
        outputs      = self.model.predict(img.reshape(1, 224, 224, 3))

        result_index = int(np.argmax(outputs))          # Get result index.

        if (result_index <= len(self.class_names)):
            result   = self.class_names[result_index]   # Get the corresponding fruit name.
        else:
            result   = "Not found"

        self.result.setText(result)
    # }


    # Close.
    def closeEvent(self, event):
    # {
        self.close()
        event.accept()
    # }
# }


# Program entry.
if '__main__' == __name__:
    default_model   = 'models/mobilenet_fruits.h5'
    default_picture = 'images/apple.jpg'

    app = QApplication(sys.argv)
    x = MainWindow()
    x.show()
    sys.exit(app.exec_())
