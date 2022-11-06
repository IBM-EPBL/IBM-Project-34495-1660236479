# -*- coding: utf-8 -*-
"""Sprint-2

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/14bhf6JP2sFZ0j2gEdPtHiWh1sifGRxIN
"""

# -*- coding: utf-8 -*-
"""Sprint 2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1RA_CMEylbBD_m5k5gme8m_aLw4rS8-wT
"""

import cv2
import numpy as np
from keras.datasets import mnist
from keras.layers import Dense, Flatten, MaxPooling2D, Dropout
from keras.layers.convolutional import Conv2D
from keras.models import Sequential
from tensorflow.keras.utils import to_categorical
import matplotlib.pyplot as plt

(X_train, y_train), (X_test, y_test) = mnist.load_data()

plt.imshow(X_train[0], cmap="gray")
plt.show()
print (y_train[0])