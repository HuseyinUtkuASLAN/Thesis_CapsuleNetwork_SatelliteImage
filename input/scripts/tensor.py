from os import walk

import sys
import numpy as np
import pickle



def create_tensor(name = "train",normalize = False, flatten = False, n_band = 3):
	x = []
	y = []
	l = ["agriculture", "tree", "building", "water"]

	band = "_" + str(n_band) + "band"

	folder_name = "../inputs/"
	if name == "train":
		folder_name += "train" + band + "/"
	elif name == "test":
		folder_name += "test" + band + "/"

	def label_index(label):
		i = 0
		if label == "agri.npy":
			i = 0
		elif label == "tree.npy":
			i = 1
		elif label == "build.npy":
			i = 2
		elif label == "water.npy":
			i = 3
		elif label == "unclassified.npy":
			i = 4
		else:
			print("ERROR LABEL!!!!!")

		return i


	files = []
	dirs = []
	for (dirpath, dirnames, filenames) in walk(folder_name):
		dirs.extend(dirnames)
		files.extend(filenames)

	

	for i,file_name in enumerate(files):
		y_class = []
		# read data
		data = np.load(folder_name + "/" + file_name)
		
		reshaped = []


		for d in data:
			if flatten:
				d = d.flatten()
			reshaped.append(d)
			y_row = np.zeros(len(files))
			y_row[label_index(file_name)] = 1
			y_class.append(y_row)
		y.extend(y_class)
		x.extend(reshaped)
		
		# create labels
		
	# normalzie numpy matrix
	def nomalize_matrix(x):
		x = np.array(x)
		return (x - x.min()) / (x.max()-x.min())
	if normalize:
		x = nomalize_matrix(x)
	

	return np.array(x), np.array(y), l

# print(get_data_set(name = "train"))
# get_data_set(name = "train")
