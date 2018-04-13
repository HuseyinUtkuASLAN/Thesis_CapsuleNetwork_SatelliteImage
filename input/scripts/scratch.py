
import numpy as np
from PIL import Image

'''
R = band 4
G = band 3
B = band 2
'''

def divide(image_size_x, image_size_y, file_path, image_path):
	"""Divides big image into smaller parts corresponds to given coordinates.

	Recommendation: Run divide before running merging operation.
		Creates a pivot that postions itself to top right of the croped image.
		If croped image is not in the boundaries of original image, pivot is shifted to fit in the original image. 

	Args:
		image_size_x: width of output
		image_size_y: heigth of output
		file_path: path of coordinates
		image_path: path of big image


	Returns:
		array: a numpy array of croped images

	"""
	
	file = open(file_path, "r")
	im = Image.open(image_path)
	imarray = np.array(im)

	x_size = int(image_size_x / 2)
	y_size = int(image_size_y / 2)

	array = []

	for line in file:
		line = line.split(' ')
		x = int(line[0].strip()) - x_size
		y = int(line[1].strip()) - y_size
		
		


		if int(line[0].strip()) + x_size > imarray.shape[0]: 
			print (file.name ,"x out of bound ", x , "\tpivot moved")
			x = imarray.shape[0] - image_size_x
		if int(line[0].strip()) - x_size < 0:
			print (file.name ,"x out of bound ", x , "\tpivot moved")
			x = 0

		

		if int(line[1].strip()) + y_size > imarray.shape[1]: 
			print (file.name ,"y out of bound ", y , "\tpivot moved")
			y = imarray.shape[1] - image_size_y
		if int(line[1].strip()) - y_size < 0:
			print (file.name ,"y out of bound ", y , "\tpivot moved")
			y = 0
		
		img = imarray[x:x+image_size_x,y:y+image_size_y]

		array.append(img)

	array = np.array(array)
	return array

def divide_test(image_size_x, image_size_y, file_path, image_path, unclassified = False):
	"""Divides big image into smaller parts corresponds to given coordinates for TEST DATA

	Recommendation: Run divide before running merging operation.
		Creates a pivot that postions itself to top right of the croped image.
		If croped image is not in the boundaries of original image, pivot is shifted to fit in the original image. 

	Args:
		image_size_x: width of output
		image_size_y: heigth of output
		file_path: path of coordinates
		image_path: path of big image
		unclassified: wheter or not using unclassified data in validation points


	Returns:
		array: a numpy array of croped images
		labels: a numpy array for classes

	"""
	
	file = open(file_path, "r")
	im = Image.open(image_path)
	imarray = np.array(im)

	x_size = int(image_size_x / 2)
	y_size = int(image_size_y / 2)

	array = []
	labels = []

	label_def = ["agri","tree","build","water","unclassified"]

	
	for line in file:
		line = line.split(' ')
		x = int(line[0].strip()) - x_size
		y = int(line[1].strip()) - y_size
		# labels of test classes // validation has 3 columns
		l = int(line[2].strip())
		

		if l == 5 and not unclassified:
			continue


		if int(line[0].strip()) + x_size > imarray.shape[0]: 
			print (file.name ,"x out of bound ", x , "\tpivot moved")
			x = imarray.shape[0] - image_size_x
		if int(line[0].strip()) - x_size < 0:
			print (file.name ,"x out of bound ", x , "\tpivot moved")
			x = 0

		

		if int(line[1].strip()) + y_size > imarray.shape[1]: 
			print (file.name ,"y out of bound ", y , "\tpivot moved")
			y = imarray.shape[1] - image_size_y
		if int(line[1].strip()) - y_size < 0:
			print (file.name ,"y out of bound ", y , "\tpivot moved")
			y = 0

		img = imarray[x:x+image_size_x,y:y+image_size_y]
		array.append(img)

		label = label_def[l-1]
		labels.append(label)

	# for a in array:
	# 	print(a.shape)
	array = np.array(array)
	labels = np.array(labels)
	return array, labels



def test_array(test_x, test_y):
	agri = []
	tree = []
	water = []
	build = []

	for i,y in enumerate(test_y):
		if y == "agri":
			agri.append(test_x[i])
		elif y == "tree":
			tree.append(test_x[i])
		elif y == "water":
			water.append(test_x[i])
		elif y == "build":
			build.append(test_x[i])
		else:
			print("ERRORRRRRR!!!!!!!!!!!!")

	return np.array(agri), np.array(tree), np.array(water), np.array(build)


def create_3_band_array(k2b, k3b, k4b, bgr = False):


	datas = []

	for i in range(k2b.shape[0]):
		image = []
		for x in range(k2b.shape[1]):
			row = []
			for y in range(k2b.shape[2]):
				pixel = []
				if bgr:
					pixel.append(k2b[i,x,y])
					pixel.append(k3b[i,x,y])
					pixel.append(k4b[i,x,y])
					# print(np.array(pixel).shape)
				else:
					pixel.append(k4b[i,x,y])
					pixel.append(k3b[i,x,y])
					pixel.append(k2b[i,x,y])

				row.append(pixel)
			image.append(np.array(row))
		datas.append(np.array(image))

	return np.array(datas,dtype = np.float64)

def create_k_band_array(bands, k = [1,2,3,4,5,6,7,8,9,10,11,12]):
	k = np.array(k)
	assert bands.shape[0] >= k.shape[0], "shape of bands is smaller than k {0} !>= {1}".format(bands.shape[0],k.shape[0])
	assert bands.shape[0] >= k.max(), "shape of bands is smaller than k {0} !>= {1}".format(bands.shape[0],k.max())
	assert k.min() > 0, "minimum value of k must be at least 1"
	# decrease 1 from k's elements for turning it to index values
	k -= 1

	datas = []

	for i in range(bands[0].shape[0]):
		image = []
		for x in range(bands[0].shape[1]):
			row = []
			for y in range(bands[0].shape[2]):
				pixel = []
				for ks in k:
					pixel.append(bands[ks][i,x,y])
				row.append(pixel)
			image.append(np.array(row))
		datas.append(np.array(image))

	return np.array(datas,dtype = np.float64)



def k_band(image_size_x, image_size_y,load_path,class_type,bands = [2,3,4]):
	band = []
	for i in bands:
		k = divide(image_size_x, image_size_y, load_path + "/" + class_type + ".txd", load_path + "/k"+ str(i) +"b.tif")
		band.append(k)
	# k2b = divide(image_size_x, image_size_y, load_path + "/" + class_type + ".txd", load_path + "/k2b.tif")
	# k3b = divide(image_size_x, image_size_y, load_path + "/" + class_type + ".txd", load_path + "/k3b.tif")
	# k4b = divide(image_size_x, image_size_y, load_path + "/" + class_type + ".txd", load_path + "/k4b.tif")

	return np.array(band)
