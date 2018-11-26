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
We extracted data from Sentinel-2 space mission of European Space Agency(ESA). We used Sentinel-1C, top-of-atmosphere reflectances in cartografic geometry. Data belong to zone code UTM zone 34N and acquired in Sentinel-2 tiling grid T34UED. Official tile id is S2A_OPER_MSI_L1C_TL_SGS__20161017T133123_A006897_T34UED_N02.04 and data strip id is S2A_OPER_MSI_L1C_DS_SGS__20161017T133123_S20161017T094431_N02.04.
The bands originally having resolution coarser than 10m  (i.e. 20 and 60m) had been oversampled to 10m.

* 13 bands(channels) in total 
+ 2 :Blue
+ 3 Green
+ 4 Red
* Fewer data than regular (404 for training and 793 for testing)
* Pixel values range between 0 and 28000
* Needed to be cut
* Image sizes of training data is 9x9 and 32x32
* Both 3 band and 13 band are used in training and testing

<!---
## RGB Image : 
![alt text](https://github.com/HuseyinUtkuASLAN/Thesis_CapsuleNetwork_SatelliteImage/blob/master/input/scripts/RGB_city "whole city")
## Few Sources : 
--->

## Algortihms :
We used VGGNet and AlexNet to compare results. Due to image sizes, paddings are set to same. For Capsule Network, we only changed kernel sizes in convolutions. We droped it to 3.

## Results :
Highest accuracy we got is 90.41% with CapsNet trained with 9x9 image sizes with all 13 bands while closest accuracy received is 89.66% with AlexNet trained with 9x9 image sizes with all 13 bands. When we look at the[“EuroSAT: A Novel Dataset and Deep Learning Benchmark for Land Use and Land Cover Classification”](https://arxiv.org/abs/1709.00029) paper, we see that highest accuracy they received is with RGB bands but in out tests we’ve observed that, 13 bands gives better accuracy. They received 98.57% with ResNet-50. Our dataset is considarably small compare to theies. Ours has 1197 images with 4 labels while theirs has 28000 images with 10 labels.


| Architectures | 9x9x13 | 9x9x3 | 32x32x3 | 32x32x13 |
| --- | --- | --- | --- | --- |
| AlexNet | 78.18 | 72.76 | 89.66 | 85.37 |
| VGGNet A | 78.56 | 79.19 | 87.89 | 86.00 |
| VGGNet D | 78.81 | 73.14 | 88.27 | 85.88 |
| VGGNet E | 76.80 | 79.32 | 86.51 | 84.74 |
| CapsNet | 78.31 | 76.29 | **90.41** |86.25 |

#### CapsNet Confusion matrix :
![alt text](https://github.com/HuseyinUtkuASLAN/Thesis_CapsuleNetwork_SatelliteImage/blob/master/confusion_matrix.png "confusion matirx of CapsNet")

### Few Sources to read
[VERY DEEP CONVOLUTIONAL NETWORKS FOR LARGE-SCALE IMAGE RECOGNITION](https://arxiv.org/pdf/1409.1556.pdf)
[ ImageNet Classification with Deep Convolutional Neural Networks](https://papers.nips.cc/paper/4824-imagenet-classification-with-deep-convolutional-neural-networks.pdf)
[“Dynamic Routing Between Capsules”](https://arxiv.org/abs/1710.09829).
[Capsnet-keras](https://github.com/XifengGuo/CapsNet-Keras)
[Capsnet-tensorflow](https://github.com/ageron/handson-ml/blob/master/extra_capsnets.ipynb)
[“EuroSAT: A Novel Dataset and Deep Learning Benchmark for Land Use and Land Cover Classification”](https://arxiv.org/abs/1709.00029)
