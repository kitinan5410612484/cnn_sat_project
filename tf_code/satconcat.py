import os
import numpy as np
import random
import PIL
import glob
from PIL import Image
import sys

##########get floder

path_arg = sys.argv[1]
path_today = str(path_arg) + "/satcrop"
path_today_save = str(path_arg) + "/satconcat"


print(path_today)
os.chdir(path_today)





file_today = []	
for file in glob.glob("*.jpg"):
	file_today.append(file)

print ("xxx")
print (file_today)



##########get name file only time hr
file_hr = [x[10:12] for x in file_today]
print (file_hr)

file_hr_int = list(map(int, file_hr))

print (file_hr_int)


os.chdir(path_today)



##########get yam 1 2 3 4
print (111)
file_hr_int_yam_1 = [i for i,v in enumerate(file_hr_int) if v < 8]

if file_hr_int_yam_1:
	file_hr_int_yam_1_index = file_hr_int_yam_1[-1]
	print (file_hr_int_yam_1_index)
print (file_hr_int_yam_1)


print (222)
file_hr_int_yam_2 = [i for i,v in enumerate(file_hr_int) if (v >= 8) & (v < 16)]

if file_hr_int_yam_2:
	file_hr_int_yam_2_index = file_hr_int_yam_2[-1]
	print (file_hr_int_yam_2_index)
print (file_hr_int_yam_2)

print (333)

file_hr_int_yam_3 = [i for i,v in enumerate(file_hr_int) if (v >= 16) & (v < 24)]

if file_hr_int_yam_3:
	file_hr_int_yam_3_index = file_hr_int_yam_3[-1]
	#print (file_hr_int_yam_3_index)
#print (file_hr_int_yam_3)


if not os.path.exists(path_today_save):
	os.makedirs(path_today_save)





for eachtime in range(0,95):

	##########get rand yam 1 2 3 4
	print ("rand")




	#####################################################################################################################have all


	rand_index_yam_1 = random.randint(0,file_hr_int_yam_1_index)
	rand_index_yam_2 = random.randint(file_hr_int_yam_1_index+1,file_hr_int_yam_2_index)
	rand_index_yam_3 = random.randint(file_hr_int_yam_2_index+1,file_hr_int_yam_3_index)

	print ("xxx")
	print (file_hr_int_yam_1_index)
	print (file_hr_int_yam_2_index)
	print (file_hr_int_yam_3_index)
	
	print ("xxx")
	########################################################################################################################con 4 image


	print (file_today[rand_index_yam_3])
	print (file_today[rand_index_yam_2])
	print (file_today[rand_index_yam_1])





	save_image = file_today[rand_index_yam_3]
	if eachtime < 10:
		save_image = save_image[:-4] + str(0) + str(eachtime) + save_image[-4:]
	else :
		save_image = save_image[:-4] + str(eachtime) + save_image[-4:]


	list_im = [file_today[rand_index_yam_3], file_today[rand_index_yam_2], file_today[rand_index_yam_1]]
	imgs    = [ PIL.Image.open(i) for i in list_im ]
	# pick the image which is the smallest, and resize the others to match it (can be arbitrary image shape here)
	min_shape = sorted( [(np.sum(i.size), i.size ) for i in imgs])[0][1]
	imgs_comb = np.vstack( (np.asarray( i.resize(min_shape) ) for i in imgs ) )

	# save that beautiful picture

	os.chdir(path_today_save)

	imgs_comb = PIL.Image.fromarray(imgs_comb)
	imgs_comb.save(save_image)

	os.chdir(path_today)



file_today = []
file_hr = []
file_hr_int = []
file_hr_int_yam_1 = []
file_hr_int_yam_2 = []
file_hr_int_yam_3 = []
file_hr_int_yam_4 = []
file_hr_int_yam_1_index = int()
file_hr_int_yam_2_index = int()
file_hr_int_yam_3_index = int()
file_hr_int_yam_4_index = int()
rand_index_yam_1 = int()
rand_index_yam_2 = int()
rand_index_yam_3 = int()
rand_index_yam_4 = int()
