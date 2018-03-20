"""Routine for dividing input image into smaller images accoring to the class"""

from PIL import Image
import numpy as np

image_size_x = 32
image_size_y = 32

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

	x_size = image_size_x / 2
	y_size = image_size_y / 2

	array = []

	for line in file:
		line = line.split(' ')
		x = int(line[0].strip()) - 16
		y = int(line[1].strip()) - 16
		
		


		if int(line[0].strip()) + 16 > imarray.shape[0]: 
			print (file.name ,"x out of bound ", x , "\tpivot moved")
			x = imarray.shape[0] - 16
		if int(line[0].strip()) - 16 < 0:
			print (file.name ,"x out of bound ", x , "\tpivot moved")
			x = 16

		

		if int(line[1].strip()) + 16 > imarray.shape[1]: 
			print (file.name ,"y out of bound ", y , "\tpivot moved")
			y = imarray.shape[0] - 16
		if int(line[1].strip()) - 16 < 0:
			print (file.name ,"y out of bound ", y , "\tpivot moved")
			y = 16
		
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

	x_size = image_size_x / 2
	y_size = image_size_y / 2

	array = []
	labels = []

	label_def = ["agri","tree","build","water","unclassified"]

	
	for line in file:
		line = line.split(' ')
		x = int(line[0].strip()) - 16
		y = int(line[1].strip()) - 16
		# labels of test classes // validation has 3 columns
		l = int(line[2].strip())
		

		if l == 5 and not unclassified:
			continue


		if int(line[0].strip()) + 16 > imarray.shape[0]: 
			print (file.name ,"x out of bound ", x , "\tpivot moved")
			x = imarray.shape[0] - 16
		if int(line[0].strip()) - 16 < 0:
			print (file.name ,"x out of bound ", x , "\tpivot moved")
			x = 16

		

		if int(line[1].strip()) + 16 > imarray.shape[1]: 
			print (file.name ,"y out of bound ", y , "\tpivot moved")
			y = imarray.shape[0] - 16
		if int(line[1].strip()) - 16 < 0:
			print (file.name ,"y out of bound ", y , "\tpivot moved")
			y = 16
		
		img = imarray[x:x+image_size_x,y:y+image_size_y]
		array.append(img)

		label = label_def[l-1]
		labels.append(label)


	array = np.array(array)
	labels = np.array(labels)
	return array, labels

		
def divide_and_save_by_band_RGB(load_path, save_path):
	"""Divides big image into smaller parts corresponds to given coordinates and saves them as npy.

	Recommendation: Run divide before running merging operation.
		Creates a pivot that postions itself to top right of the croped image.
		If croped image is not in the boundaries of original image, pivot is shifted to fit in the original image. 
		Band 4 is Red, band 3 is Green and band 2 is Blue

	Args:
		load_path: file path where original image and coordinates folder should be
		save_path: path where bands wants to be saved


	Returns:
		None

	"""

	'''
	R = band 4
	G = band 3
	B = band 2
	'''
	
	agri_np_k3b = divide(image_size_x, image_size_y, load_path + "/agriculture.txd", load_path + "/k3b.tif")

	build_np_k3b = divide(image_size_x, image_size_y, load_path + "/biultup.txd", load_path + "/k3b.tif")

	tree_np_k3b = divide(image_size_x, image_size_y, load_path + "/treeCover.txd", load_path + "/k3b.tif")

	water_np_k3b = divide(image_size_x, image_size_y, load_path + "/waterBodies.txd", load_path + "/k3b.tif")

	np.save(save_path + "/agri_np_k3b",agri_np_k3b)
	np.save(save_path + "/build_np_k3b",build_np_k3b)
	np.save(save_path + "/tree_np_k3b",tree_np_k3b)
	np.save(save_path + "/water_np_k3b",water_np_k3b)

	agri_np_k4b = divide(image_size_x, image_size_y, load_path + "/agriculture.txd", load_path + "/k4b.tif")

	build_np_k4b = divide(image_size_x, image_size_y, load_path + "/biultup.txd", load_path + "/k4b.tif")

	tree_np_k4b = divide(image_size_x, image_size_y, load_path + "/treeCover.txd", load_path + "/k4b.tif")

	water_np_k4b = divide(image_size_x, image_size_y, load_path + "/waterBodies.txd", load_path + "/k4b.tif")

	np.save(save_path + "/agri_np_k4b",agri_np_k4b)
	np.save(save_path + "/build_np_k4b",build_np_k4b)
	np.save(save_path + "/tree_np_k4b",tree_np_k4b)
	np.save(save_path + "/water_np_k4b",water_np_k4b)

	agri_np_k2b = divide(image_size_x, image_size_y, load_path + "/agriculture.txd", load_path + "/k2b.tif")

	build_np_k2b = divide(image_size_x, image_size_y, load_path + "/biultup.txd", load_path + "/k2b.tif")

	tree_np_k2b = divide(image_size_x, image_size_y, load_path + "/treeCover.txd", load_path + "/k2b.tif")

	water_np_k2b = divide(image_size_x, image_size_y, load_path + "/waterBodies.txd", load_path + "/k2b.tif")

	np.save(save_path + "/agri_np_k2b",agri_np_k2b)
	np.save(save_path + "/build_np_k2b",build_np_k2b)
	np.save(save_path + "/tree_np_k2b",tree_np_k2b)
	np.save(save_path + "/water_np_k2b",water_np_k2b)

	test_k2b_x, test_k2b_y = divide_test(image_size_x, image_size_y, load_path + "/validationPoints.txd", load_path + "/k2b.tif")
	test_k3b_x, test_k3b_y = divide_test(image_size_x, image_size_y, load_path + "/validationPoints.txd", load_path + "/k3b.tif")
	test_k4b_x, test_k4b_y = divide_test(image_size_x, image_size_y, load_path + "/validationPoints.txd", load_path + "/k4b.tif")

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

		return agri, tree, water, build


	agri_tst_k2b, tree_tst_k2b, water_tst_k2b, build_tst_k2b = test_array(test_k2b_x,test_k2b_y)
	agri_tst_k3b, tree_tst_k3b, water_tst_k3b, build_tst_k3b = test_array(test_k3b_x,test_k3b_y)
	agri_tst_k4b, tree_tst_k4b, water_tst_k4b, build_tst_k4b = test_array(test_k4b_x,test_k4b_y)

	np.save(save_path + "/agri_tst_k2b",agri_tst_k2b)
	np.save(save_path + "/build_tst_k2b",build_tst_k2b)
	np.save(save_path + "/tree_tst_k2b",tree_tst_k2b)
	np.save(save_path + "/water_tst_k2b",water_tst_k2b)

	np.save(save_path + "/agri_tst_k3b",agri_tst_k3b)
	np.save(save_path + "/build_tst_k3b",build_tst_k3b)
	np.save(save_path + "/tree_tst_k3b",tree_tst_k3b)
	np.save(save_path + "/water_tst_k3b",water_tst_k3b)

	np.save(save_path + "/agri_tst_k4b",agri_tst_k4b)
	np.save(save_path + "/build_tst_k4b",build_tst_k4b)
	np.save(save_path + "/tree_tst_k4b",tree_tst_k4b)
	np.save(save_path + "/water_tst_k4b",water_tst_k4b)
