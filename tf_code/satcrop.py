import os
import numpy as np
import random
import PIL
import glob
from PIL import Image
import sys




##########get floder

path_arg = sys.argv[1]
path_today = str(path_arg) + "/satimage"
path_today_save = str(path_arg) + "/satcrop"


print(path_today)
os.chdir(path_today)





file_today = []	
for file in glob.glob("*.jpg"):
	file_today.append(file)

print ("xxx")
print (file_today)



for eachtime in range(0,len(file_today)):


	save_image = file_today[eachtime]

	img = Image.open(file_today[eachtime])
	img2 = img.crop((322, 322, 1314, 962))

	os.chdir(path_today_save)
	img2.save(save_image)

	os.chdir(path_today)



file_today = []





