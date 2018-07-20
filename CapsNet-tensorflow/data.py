import numpy as np

def turn_one_hot(Y, v_min = 1, v_max = 4):
    vectors = []
    for y in Y:
        v = np.zeros([v_max - v_min + 1])
        v[int(y - 1)] = 1
        vectors.append(v)
    return vectors

def get_data_set(name = "train",input_path = "../input/data_9x9_3band/",one_hot = False):
	
	s = "_train"
	if name == "test":
		s = "_valid"

	x = np.load(input_path + "X" + s + ".npy")
	y = np.load(input_path + "Y" + s + ".npy")

	if one_hot:
		y = turn_one_hot(y)

	return np.array(x,dtype = "float64"), np.array(y)