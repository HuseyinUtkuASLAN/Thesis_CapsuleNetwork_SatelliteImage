'''Script to run divide and merge operation.'''
import os
from scratch import divide, divide_test, test_array, create_3_band_array, k_band, create_k_band_array
from tensor import create_tensor
import numpy as np

def _create_folder(directory):
	if not os.path.exists(directory):
		os.makedirs(directory)

# create folders for saving datas/checkpoints
_create_folder("../inputs")

_create_folder("../inputs/train_3band")
_create_folder("../inputs/test_3band")
_create_folder("../train_3band")
_create_folder("../test_3band")

_create_folder("../inputs/train_12band")
_create_folder("../inputs/test_12band")
_create_folder("../train_12band")
_create_folder("../test_12band")

# attributes
load_path = "../raw_iputs"

divided_save_path_train_3band = "../inputs/train_3band/"
divided_save_path_test_3band = "../inputs/test_3band/"
tensor_save_path_train_3band = "../train_3band/"
tensor_save_path_test_3band =  "../test_3band/"

divided_save_path_train_12band = "../inputs/train_12band/"
divided_save_path_test_12band = "../inputs/test_12band/"
tensor_save_path_train_12band = "../train_12band/"
tensor_save_path_test_12band =  "../test_12band/"

image_size_x = 32
image_size_y = 32

print("\n\n>>>> dividing\n\n")
# divides all & create 9 band images as np arrays
test_bands = []
for i in range(1,13):
	x,y = divide_test(image_size_x, image_size_y, load_path + "/validationPoints.txd", load_path + "/k"+ str(i) +"b.tif")
	test_bands.append((x,y))


agri_test_bands = []
tree_test_bands = []
water_test_bands = []
build_test_bands = []
for x,y in test_bands:
	agri, tree, water, build = test_array(x,y)
	agri_test_bands.append(agri)
	tree_test_bands.append(tree)
	water_test_bands.append(water)
	build_test_bands.append(build)


tree_bands = k_band(image_size_x, image_size_y, load_path,"treeCover", bands = [1,2,3,4,5,6,7,8,9,10,11,12])
agri_bands = k_band(image_size_x, image_size_y, load_path,"agriculture", bands = [1,2,3,4,5,6,7,8,9,10,11,12])
build_bands = k_band(image_size_x, image_size_y, load_path,"biultup", bands = [1,2,3,4,5,6,7,8,9,10,11,12])
water_bands = k_band(image_size_x, image_size_y, load_path,"waterBodies", bands = [1,2,3,4,5,6,7,8,9,10,11,12])


print("\n\n>>>> creating 3 band arrays\n\n")

tree_3band = create_k_band_array(tree_bands,k=[4,3,2])
agri_3band = create_k_band_array(agri_bands,k=[4,3,2])
build_3band = create_k_band_array(build_bands,k=[4,3,2])
water_3band = create_k_band_array(water_bands,k=[4,3,2])

tree_test_3band = create_k_band_array(np.array(tree_test_bands),k=[4,3,2])
agri_test_3band = create_k_band_array(np.array(agri_test_bands),k=[4,3,2])
build_test_3band = create_k_band_array(np.array(build_test_bands),k=[4,3,2])
water_test_3band = create_k_band_array(np.array(water_test_bands),k=[4,3,2])

print("\n\n>>>> creating 12 band arrays\n\n")
tree_12band = create_k_band_array(tree_bands)
agri_12band = create_k_band_array(agri_bands)
build_12band = create_k_band_array(build_bands)
water_12band = create_k_band_array(water_bands)

tree_test_12band = create_k_band_array(np.array(tree_test_bands))
agri_test_12band = create_k_band_array(np.array(agri_test_bands))
build_test_12band = create_k_band_array(np.array(build_test_bands))
water_test_12band = create_k_band_array(np.array(water_test_bands))


print("\n\n>>>> saving as numpy arrays\n\n")
# save np arrays
np.save(divided_save_path_train_3band + "tree",tree_3band)
np.save(divided_save_path_train_3band + "agri",agri_3band)
np.save(divided_save_path_train_3band + "build",build_3band)
np.save(divided_save_path_train_3band + "water",water_3band)

np.save(divided_save_path_test_3band + "tree",tree_test_3band)
np.save(divided_save_path_test_3band + "agri",agri_test_3band)
np.save(divided_save_path_test_3band + "build",build_test_3band)
np.save(divided_save_path_test_3band + "water",water_test_3band)


np.save(divided_save_path_train_12band + "tree",tree_12band)
np.save(divided_save_path_train_12band + "agri",agri_12band)
np.save(divided_save_path_train_12band + "build",build_12band)
np.save(divided_save_path_train_12band + "water",water_12band)

np.save(divided_save_path_test_12band + "tree",tree_test_12band)
np.save(divided_save_path_test_12band + "agri",agri_test_12band)
np.save(divided_save_path_test_12band + "build",build_test_12band)
np.save(divided_save_path_test_12band + "water",water_test_12band)



print("\n\n>>>> creating train and test datas\n\n")

x_train_3band, y_train_3band, l_train_3band = create_tensor("train")
x_test_3band, y_test_3band, l_test_3band = create_tensor("test")

x_train_12band, y_train_12band, l_train_12band = create_tensor("train",n_band = 12)
x_test_12band, y_test_12band, l_test_12band = create_tensor("test", n_band = 12)


np.save(tensor_save_path_train_3band + "x", x_train_3band)
np.save(tensor_save_path_train_3band + "y", y_train_3band)
np.save(tensor_save_path_train_3band + "label", l_train_3band)

np.save(tensor_save_path_test_3band + "x", x_test_3band)
np.save(tensor_save_path_test_3band + "y", y_test_3band)
np.save(tensor_save_path_test_3band + "label", l_test_3band)

np.save(tensor_save_path_train_12band + "x", x_train_12band)
np.save(tensor_save_path_train_12band + "y", y_train_12band)
np.save(tensor_save_path_train_12band + "label", l_train_12band)

np.save(tensor_save_path_test_12band + "x", x_test_12band)
np.save(tensor_save_path_test_12band + "y", y_test_12band)
np.save(tensor_save_path_test_12band + "label", l_test_12band)


print("\n\n>>>> all done. go crazy!\n\n")
