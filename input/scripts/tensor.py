from os import walk

import sys
import numpy as np
import pickle



def get_data_set(name = "train",normalize = False):
	x = []
	y = []
	l = ["agriculture", "tree", "building", "water"]

	folder_name = "../inputs/merged/"
	if name == "train":
		folder_name += "train/"
	elif name == "test":
		folder_name += "test/"

	def label_index(label):
		i = 0
		if label == "agri":
			i = 0
		elif label == "tree":
			i = 1
		elif label == "build":
			i = 2
		elif label == "water":
			i = 3
		elif label == "unclassified":
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
		data = np.load(folder_name + dirs[i] + "/" + file_name)
		
		reshaped = []


		for d in data:
			reshaped.append(d.flatten())
			y_row = np.zeros(len(dirs))
			y_row[label_index(dirs[i])] = 1
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

# print(get_data_set(name = "train",normalize = True))
# get_data_set(name = "train")[0].shape
