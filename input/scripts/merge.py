import os
import numpy as np

'''
R = band 4
G = band 3
B = band 2
'''

def merge(load_path,save_path):

	agri = []
	build = []
	tree = []
	water = []

	agri_np_k2b = np.load(load_path + "/agri_np_k2b.npy")
	build_np_k2b = np.load(load_path + "/build_np_k2b.npy")
	tree_np_k2b = np.load(load_path + "/tree_np_k2b.npy")
	water_np_k2b = np.load(load_path + "/water_np_k2b.npy")

	agri_np_k3b = np.load(load_path + "/agri_np_k3b.npy")
	build_np_k3b = np.load(load_path + "/build_np_k3b.npy")
	tree_np_k3b = np.load(load_path + "/tree_np_k3b.npy")
	water_np_k3b = np.load(load_path + "/water_np_k3b.npy")

	agri_np_k4b = np.load(load_path + "/agri_np_k4b.npy")
	build_np_k4b = np.load(load_path + "/build_np_k4b.npy")
	tree_np_k4b = np.load(load_path + "/tree_np_k4b.npy")
	water_np_k4b = np.load(load_path + "/water_np_k4b.npy")

	for i in range(agri_np_k2b.shape[0]):
		elem = []
		'''R'''
		elem.append(agri_np_k4b[i])
		'''G'''
		elem.append(agri_np_k3b[i])
		'''B'''
		elem.append(agri_np_k2b[i])

		elem = np.array(elem)
		agri.append(elem)

	for i in range(build_np_k2b.shape[0]):
		elem = []
		'''R'''
		elem.append(build_np_k4b[i])
		'''G'''
		elem.append(build_np_k3b[i])
		'''B'''
		elem.append(build_np_k2b[i])

		elem = np.array(elem)
		build.append(elem)
	
	for i in range(tree_np_k2b.shape[0]):
		elem = []
		'''R'''
		elem.append(tree_np_k4b[i])
		'''G'''
		elem.append(tree_np_k3b[i])
		'''B'''
		elem.append(tree_np_k2b[i])

		elem = np.array(elem)
		tree.append(elem)

	for i in range(water_np_k2b.shape[0]):
		elem = []
		'''R'''
		elem.append(water_np_k4b[i])
		'''G'''
		elem.append(water_np_k3b[i])
		'''B'''
		elem.append(water_np_k2b[i])

		elem = np.array(elem)
		water.append(elem)



	agri = np.array(agri)
	build = np.array(build)
	tree = np.array(tree)
	water = np.array(water)

	np.save(save_path + "/agri/agri",agri)
	np.save(save_path + "/build/build",build)
	np.save(save_path + "/tree/tree",tree)
	np.save(save_path + "/water/water",water)

