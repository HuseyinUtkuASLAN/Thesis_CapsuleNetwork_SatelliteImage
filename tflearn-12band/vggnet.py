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

import numpy as np
from data import get_data_set

NUM_OF_CLASSES = 4
learning_rate = 1e-4
optimizer='rmsprop'
# optimizer='momentum'
X,Y, _ = get_data_set("train")
X_test, Y_test, _ = get_data_set("test")
# combined
# X = np.concatenate((X, X_test), axis=0)
# Y = np.concatenate((Y, Y_test), axis = 0)
# X, Y = shuffle(X, Y)

network = input_data(shape = [None, 32, 32, 12])
network = conv_2d(network,64,3,strides = 1, activation='relu')
network = max_pool_2d(network,2,strides = 2)
network = conv_2d(network,128,3,strides = 1, activation='relu')
network = max_pool_2d(network,2,strides = 2)
network = conv_2d(network,256,3,strides = 1, activation='relu')
network = conv_2d(network,256,3,strides = 1, activation='relu')
network = max_pool_2d(network,2,strides = 2)
network = conv_2d(network,256,3,strides = 1, activation='relu')
network = conv_2d(network,256,3,strides = 1, activation='relu')
network = max_pool_2d(network,2,strides = 2)

network = fully_connected(network, 4096, activation = 'relu')
network = dropout(network,0.5)
network = fully_connected(network, 4096, activation = 'relu')
network = dropout(network,0.5)
network = fully_connected(network, 1000, activation = 'relu')
network = dropout(network,0.5)
network = fully_connected(network, NUM_OF_CLASSES, activation = 'softmax')
network = regression(network, optimizer=optimizer,
                     loss='categorical_crossentropy',
                     learning_rate=learning_rate)

model = tflearn.DNN(network, tensorboard_verbose=0,
  tensorboard_dir = "tensorboard/")

model.fit(X, Y, n_epoch=500, validation_set=(X_test,Y_test), shuffle=True,
          show_metric=True, batch_size=64, snapshot_step=False,
          snapshot_epoch=True, run_id='VGGNet_A_' + optimizer)