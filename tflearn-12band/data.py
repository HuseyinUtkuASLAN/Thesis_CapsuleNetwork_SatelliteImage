from os import walk

import sys
import numpy as np
import pickle



def get_data_set(name = "train",normalize = False, flatten = False):
	
	folder_name = "../input/"
	if name == "train":
		folder_name += "train_12band/"
	elif name == "test":
		folder_name += "test_12band/"
	
	x = np.load(folder_name + "x" + ".npy")
	if flatten:
		new_x = []
		for i,d in enumerate(x):
			new_x.append(d.flatten())
		x = np.array(new_x)
	y = np.load(folder_name + "y" + ".npy")
	l = np.load(folder_name + "label" + ".npy")
	# normalzie numpy matrix
	def nomalize_matrix(x):
		x = np.array(x)
		return (x - x.min()) / (x.max()-x.min())
	if normalize:
		x = nomalize_matrix(x)
	

	return np.array(x,dtype = "float64"), np.array(y,dtype = "float64"), l

# print(get_data_set(name = "train",normalize = True))
# get_data_set(name = "train")[0].shape
