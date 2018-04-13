from __future__ import division, print_function, absolute_import
## This stops program to give warnings.  INFO = 1   WARNING = 2     ERROR = 3
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
##
'''
source : https://github.com/tflearn/tflearn/blob/master/examples/images/convnet_cifar10.py
'''

# -*- coding: utf-8 -*-

""" Convolutional network applied to CIFAR-10 dataset classification task.

References:
    Learning Multiple Layers of Features from Tiny Images, A. Krizhevsky, 2009.

Links:
    [CIFAR-10 Dataset](https://www.cs.toronto.edu/~kriz/cifar.html)

"""


import tflearn
from tflearn.data_utils import shuffle, to_categorical
from tflearn.layers.core import input_data, dropout, fully_connected
from tflearn.layers.conv import conv_2d, max_pool_2d
from tflearn.layers.estimator import regression
from tflearn.data_preprocessing import ImagePreprocessing
from tflearn.data_augmentation import ImageAugmentation

# Data loading and preprocessing
import numpy as np
from data import get_data_set

NUM_OF_CLASSES = 4
# optimizer='rmsprop'
optimizer='adam'


X,Y, _ = get_data_set("train")
X_test, Y_test, _ = get_data_set("test")

# X = np.concatenate((X, X_test), axis=0)
# Y = np.concatenate((Y, Y_test), axis = 0)
# X, Y = shuffle(X, Y)
# Y = to_categorical(Y)
# Y_test = to_categorical(Y_test)

# Real-time data preprocessing
img_prep = ImagePreprocessing()
img_prep.add_featurewise_zero_center()
img_prep.add_featurewise_stdnorm()

# Real-time data augmentation
img_aug = ImageAugmentation()
img_aug.add_random_flip_leftright()
img_aug.add_random_rotation(max_angle=25.)

# Convolutional network building
network = input_data(shape=[None, 32, 32, 12],
                     data_preprocessing=img_prep,
                     data_augmentation=img_aug)
network = conv_2d(network, 32, 3, activation='relu')
network = max_pool_2d(network, 2)
network = conv_2d(network, 64, 3, activation='relu')
network = conv_2d(network, 64, 3, activation='relu')
network = max_pool_2d(network, 2)
network = fully_connected(network, 512, activation='relu')
network = dropout(network, 0.5)
network = fully_connected(network, NUM_OF_CLASSES, activation='softmax')
network = regression(network, optimizer = optimizer,
                     loss='categorical_crossentropy',
                     learning_rate=0.001)

# Train using classifier
model = tflearn.DNN(network, tensorboard_verbose=0,tensorboard_dir = "tensorboard/")
model.fit(X, Y, n_epoch=500, shuffle=True, validation_set=(X_test,Y_test),
          show_metric=True, batch_size=96, run_id='cifar10_cnn' + optimizer )