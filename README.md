# Application of Capsule Network for land cover classification in satellite images

## Aim

The work aims at exploration of one of the interesting current advances in neural networks to land cover classification in satellite images.

## Overview

1. Capsule net or CapsNet is a new deep learning technique for image classification.
2. Sara Sabour, Nicholas Frost and Geoffrey Hinton proposed it in a paper titled [“Dynamic Routing Between Capsules”](https://arxiv.org/abs/1710.09829).
3. It solves several problems Convolutional Neural Networks or CNN cannot solve.
4. CNN is good for classifying images that are close to the training set.
5. CapsNet gives relatively better results in MNIST dataset.

## Data

* 12 bands(channels) in total 
+ 2 :Blue
+ 3 Green
+ 4 Red
* Fewer data than regular (404 for training and 793 for testing)
* Pixel values range between 1 and 28000
* Needed to be cut
* Image sizes of training data is 9x9 and 32x32
* Both 3 band and 12 band are used in training and testing

## Todo:

1. Prepare a official list of results
2. Write paper

## Few Sources : 

[VERY DEEP CONVOLUTIONAL NETWORKS FOR LARGE-SCALE IMAGE RECOGNITION](https://arxiv.org/pdf/1409.1556.pdf)
[ ImageNet Classification with Deep Convolutional Neural Networks](https://papers.nips.cc/paper/4824-imagenet-classification-with-deep-convolutional-neural-networks.pdf)
[“Dynamic Routing Between Capsules”](https://arxiv.org/abs/1710.09829).
[Capsnet-keras](https://github.com/XifengGuo/CapsNet-Keras)
[Capsnet-tensorflow](https://github.com/ageron/handson-ml/blob/master/extra_capsnets.ipynb)