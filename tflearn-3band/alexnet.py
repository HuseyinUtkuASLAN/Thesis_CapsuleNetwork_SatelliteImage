# -*- coding: utf-8 -*-

""" AlexNet.

Applying 'Alexnet' to Oxford's 17 Category Flower Dataset classification task.

References:
    - Alex Krizhevsky, Ilya Sutskever & Geoffrey E. Hinton. ImageNet
    Classification with Deep Convolutional Neural Networks. NIPS, 2012.
    - 17 Category Flower Dataset. Maria-Elena Nilsback and Andrew Zisserman.

Links:
    - [AlexNet Paper](http://papers.nips.cc/paper/4824-imagenet-classification-with-deep-convolutional-neural-networks.pdf)
    - [Flower Dataset (17)](http://www.robots.ox.ac.uk/~vgg/data/flowers/17/)

"""

from __future__ import division, print_function, absolute_import
## This stops program to give warnings.  INFO = 1   WARNING = 2     ERROR = 3
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
##
import tflearn
from tflearn.data_utils import shuffle
from tflearn.layers.core import input_data, dropout, fully_connected
from tflearn.layers.conv import conv_2d, max_pool_2d
from tflearn.layers.normalization import local_response_normalization
from tflearn.layers.estimator import regression
from tflearn.data_preprocessing import ImagePreprocessing
from tflearn.data_augmentation import ImageAugmentation

import numpy as np
from data import get_data_set

NUM_OF_CLASSES = 4


optimizer='rmsprop'
# optimizer='adam'
# optimizer='momentum'
X,Y, _ = get_data_set("train")
X_test, Y_test, _ = get_data_set("test")


network = input_data(shape=[None, 32, 32, 3])
network = conv_2d(network, 96, 11, strides=4, activation='relu')
network = max_pool_2d(network, 3, strides=2)
network = local_response_normalization(network)
network = conv_2d(network, 256, 5, activation='relu')
network = max_pool_2d(network, 3, strides=2)
network = local_response_normalization(network)
network = conv_2d(network, 384, 3, activation='relu')
network = conv_2d(network, 384, 3, activation='relu')
network = conv_2d(network, 256, 3, activation='relu')
network = max_pool_2d(network, 3, strides=2)
network = local_response_normalization(network)
network = fully_connected(network, 4096, activation='tanh')
network = dropout(network, 0.5)
network = fully_connected(network, 4096, activation='tanh')
network = dropout(network, 0.5)
network = fully_connected(network, NUM_OF_CLASSES, activation='softmax')
network = regression(network, optimizer=optimizer,
                     loss='categorical_crossentropy',
                     learning_rate=0.0001)

# Training
# checkpoint_path='checkpoints/model_alexnet'
model = tflearn.DNN(network, tensorboard_verbose=0,
  tensorboard_dir = "tensorboard/")
model.fit(X, Y, n_epoch=500, validation_set=(X_test,Y_test), shuffle=True,
          show_metric=True, batch_size=64, snapshot_step=False,
          snapshot_epoch=True, run_id='alexnet_' + optimizer+ "_afterInputFix")

