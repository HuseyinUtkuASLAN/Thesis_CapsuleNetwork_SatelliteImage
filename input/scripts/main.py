'''Script to run divide and merge operation.'''
import os
from scratch import divide, divide_test, test_array, create_3_band_array, k_band
from tensor import create_tensor
import numpy as np

def _create_folder(directory):
	if not os.path.exists(directory):
		os.makedirs(directory)

# create folders for saving datas/checkpoints
_create_folder("../inputs")
_create_folder("../inputs/train")
_create_folder("../inputs/test")
_create_folder("../train")
_create_folder("../test")

# attributes
load_path = "../raw_iputs"
divided_save_path_train = "../inputs/train/"
divided_save_path_test = "../inputs/test/"
tensor_save_path_train = "../train/"
tensor_save_path_test =  "../test/"
image_size_x = 32
image_size_y = 32

print("\n\n>>>> dividing\n\n")
# divide & create 3 band images as np arrays

test_k2b_x, test_k2b_y = divide_test(image_size_x, image_size_y, load_path + "/validationPoints.txd", load_path + "/k2b.tif")
test_k3b_x, test_k3b_y = divide_test(image_size_x, image_size_y, load_path + "/validationPoints.txd", load_path + "/k3b.tif")
test_k4b_x, test_k4b_y = divide_test(image_size_x, image_size_y, load_path + "/validationPoints.txd", load_path + "/k4b.tif")

agri_tst_k2b, tree_tst_k2b, water_tst_k2b, build_tst_k2b = test_array(test_k2b_x,test_k2b_y)
agri_tst_k3b, tree_tst_k3b, water_tst_k3b, build_tst_k3b = test_array(test_k3b_x,test_k3b_y)
agri_tst_k4b, tree_tst_k4b, water_tst_k4b, build_tst_k4b = test_array(test_k4b_x,test_k4b_y)

k2b_tree, k3b_tree, k4b_tree = k_band(image_size_x, image_size_y, load_path,"treeCover")
k2b_agri, k3b_agri, k4b_agri = k_band(image_size_x, image_size_y, load_path,"agriculture")
k2b_build, k3b_build, k4b_build = k_band(image_size_x, image_size_y, load_path,"biultup")
k2b_water, k3b_water, k4b_water = k_band(image_size_x, image_size_y, load_path,"waterBodies")

print("\n\n>>>> creating 3 band arrays\n\n")

tree = create_3_band_array(k2b_tree,k3b_tree,k4b_tree)
agri = create_3_band_array(k2b_agri,k3b_agri,k4b_agri)
build = create_3_band_array(k2b_build,k3b_build,k4b_build)
water = create_3_band_array(k2b_water,k3b_water,k4b_water)
agri_test = create_3_band_array(agri_tst_k2b, agri_tst_k3b, agri_tst_k4b)
tree_test = create_3_band_array(tree_tst_k2b, tree_tst_k3b, tree_tst_k4b)
water_test = create_3_band_array(water_tst_k2b, water_tst_k3b, water_tst_k4b)
build_test = create_3_band_array(build_tst_k2b, build_tst_k3b, build_tst_k4b)

print("\n\n>>>> saving as numpy arrays\n\n")
# save np arrays
np.save(divided_save_path_train + "tree",tree)
np.save(divided_save_path_train + "agri",agri)
np.save(divided_save_path_train + "build",build)
np.save(divided_save_path_train + "water",water)

np.save(divided_save_path_test + "tree",tree_test)
np.save(divided_save_path_test + "agri",agri_test)
np.save(divided_save_path_test + "build",build_test)
np.save(divided_save_path_test + "water",water_test)

print("\n\n>>>> creating train and test datas\n\n")

x_train, y_train, l_train = create_tensor("train",normalize = True)
x_test, y_test, l_test = create_tensor("test")


np.save(tensor_save_path_train + "x", x_train)
np.save(tensor_save_path_train + "y", y_train)
np.save(tensor_save_path_train + "label", l_train)

np.save(tensor_save_path_test + "x", x_test)
np.save(tensor_save_path_test + "y", y_test)
np.save(tensor_save_path_test + "label", l_test)

print("\n\n>>>> all done. go crazy!\n\n")