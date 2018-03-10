'''Script to run divide and merge operation.'''
import os
from divide_image import divide_and_save_by_band_RGB
from merge import merge

def _create_folder(directory):
	if not os.path.exists(directory):
		os.makedirs(directory)

_create_folder("../inputs")
_create_folder("../inputs/by_bands")
_create_folder("../inputs/merged")
_create_folder("../inputs/merged/agri")
_create_folder("../inputs/merged/build")
_create_folder("../inputs/merged/tree")
_create_folder("../inputs/merged/water")

# _create_folder(save_path + "/agri")
# _create_folder(save_path + "/build")
# _create_folder(save_path + "/tree")
# _create_folder(save_path + "/water")

print "Divinding images by bands"
print "--------------------------\n\n"
divide_and_save_by_band_RGB("../raw_iputs","../inputs/by_bands")

print "\n\nImages divided by band"
print "--------------------------\n\n"

print "merging images"
print "--------------------------"

merge("../inputs/by_bands","../inputs/merged")
# merge here
print "\nMerge complete"
print "--------------------------\n\n"
