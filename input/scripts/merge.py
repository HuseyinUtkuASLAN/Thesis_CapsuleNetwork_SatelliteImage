"""Routine for merging divided classes and putting them in folders"""
import numpy as np

'''
R = band 4
G = band 3
B = band 2
'''

def merge(load_path,save_path, test = False):
	"""Merges divided files. Saves every class to appropriate folder

	Recommendation: Run divide before running merging operation

	Args:
		load_path: path to divided input file
		save_path: where to save merged data
		test: if test is false, train data is merged, else test is merged.

	Returns:
		None

	"""

	dtype = "np"
	if test:
		dtype = "tst"

	agri = []
	build = []
	tree = []
	water = []

	agri_np_k2b = np.load(load_path + "/agri_{0}_k2b.npy".format(dtype))
	build_np_k2b = np.load(load_path + "/build_{0}_k2b.npy".format(dtype))
	tree_np_k2b = np.load(load_path + "/tree_{0}_k2b.npy".format(dtype))
	water_np_k2b = np.load(load_path + "/water_{0}_k2b.npy".format(dtype))

	agri_np_k3b = np.load(load_path + "/agri_{0}_k3b.npy".format(dtype))
	build_np_k3b = np.load(load_path + "/build_{0}_k3b.npy".format(dtype))
	tree_np_k3b = np.load(load_path + "/tree_{0}_k3b.npy".format(dtype))
	water_np_k3b = np.load(load_path + "/water_{0}_k3b.npy".format(dtype))

	agri_np_k4b = np.load(load_path + "/agri_{0}_k4b.npy".format(dtype))
	build_np_k4b = np.load(load_path + "/build_{0}_k4b.npy".format(dtype))
	tree_np_k4b = np.load(load_path + "/tree_{0}_k4b.npy".format(dtype))
	water_np_k4b = np.load(load_path + "/water_{0}_k4b.npy".format(dtype))

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

	dtype = "train"
	if test:
		dtype = "test"

	np.save(save_path + "/{0}/agri/agri".format(dtype),agri)
	np.save(save_path + "/{0}/build/build".format(dtype),build)
	np.save(save_path + "/{0}/tree/tree".format(dtype),tree)
	np.save(save_path + "/{0}/water/water".format(dtype),water)

