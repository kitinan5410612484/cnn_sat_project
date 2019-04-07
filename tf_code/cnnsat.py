import os
import numpy as np
import random
import PIL
from PIL import Image
import shutil
import pandas as pd
import numpy as np
import os
import numpy as np
import random
import PIL
import glob
from PIL import Image


#os.chdir("C:/Users/OFF-PC/Desktop/appcnn")

with open("out1.txt") as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content] 

f.close()

picpre1 = []

for eachpic in range(1, len(content)):
	picpre1.append(content[eachpic][-1])
	#picpre1[eachpic] = content[eachpic][-1]

picpre1_int = list(map(int, picpre1))


picpre1_intnp = np.array(picpre1_int)

ans1 = [0,0,0,0,0,0]
ans1[0] = 0
ans1[1] = np.count_nonzero(picpre1_intnp == 1)
ans1[2] = np.count_nonzero(picpre1_intnp == 2)
ans1[3] = np.count_nonzero(picpre1_intnp == 3)
ans1[4] = np.count_nonzero(picpre1_intnp == 4)
ans1[5] = np.count_nonzero(picpre1_intnp == 5)

#print(ans1)

highest1 = ans1.index(max(ans1))

print("\n")

if highest1 == 1:
	print("The Prediction 1 day ahead is Not rain or 0 mm.")
if highest1 == 2:
	print("The Prediction 1 day ahead is Light rain or 0.1 to 10 mm.")
if highest1 == 3:
	print("The Prediction 1 day ahead is Moderate rain or 10.1 to 50 mm.")
if highest1 == 4:
	print("The Prediction 1 day ahead is Heavy rain or 50.1 to 150 mm.")
if highest1 == 5:
	print("The Prediction 1 day ahead is Very heavy rain or more than 150mm.")

print("\n")

#222222222222222222222222222222222222222222222222

with open("out2.txt") as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content] 

f.close()

picpre2 = []

for eachpic in range(1, len(content)):
	picpre2.append(content[eachpic][-1])
	#picpre2[eachpic] = content[eachpic][-1]

picpre2_int = list(map(int, picpre2))

picpre2_intnp = np.array(picpre2_int)

ans2 = [0,0,0,0,0,0]
ans2[0] = 0
ans2[1] = np.count_nonzero(picpre2_intnp == 1)
ans2[2] = np.count_nonzero(picpre2_intnp == 2)
ans2[3] = np.count_nonzero(picpre2_intnp == 3)
ans2[4] = np.count_nonzero(picpre2_intnp == 4)
ans2[5] = np.count_nonzero(picpre2_intnp == 5)

#print(ans2)

highest2 = ans2.index(max(ans2))


if highest2 == 1:
	print("The Prediction 2 days ahead is Not rain or 0 mm.")
if highest2 == 2:
	print("The Prediction 2 days ahead is Light rain or 0.1 to 10 mm.")
if highest2 == 3:
	print("The Prediction 2 days ahead is Moderate rain or 10.1 to 50 mm.")
if highest2 == 4:
	print("The Prediction 2 days ahead is Heavy rain or 50.1 to 150 mm.")
if highest2 == 5:
	print("The Prediction 2 days ahead is Very heavy rain or more than 150mm.")

print("\n")
#333333333333333333333

with open("out3.txt") as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content] 

f.close()

picpre3 = []

for eachpic in range(1, len(content)):
	picpre3.append(content[eachpic][-1])

picpre3_int = list(map(int, picpre3))

picpre3_intnp = np.array(picpre3_int)

ans3 = [0,0,0,0,0,0]
ans3[0] = 0
ans3[1] = np.count_nonzero(picpre3_intnp == 1)
ans3[2] = np.count_nonzero(picpre3_intnp == 2)
ans3[3] = np.count_nonzero(picpre3_intnp == 3)
ans3[4] = np.count_nonzero(picpre3_intnp == 4)
ans3[5] = np.count_nonzero(picpre3_intnp == 5)

#print(ans3)

highest3 = ans3.index(max(ans3))

if highest3 == 1:
	print("The Prediction 3 days ahead is Not rain or 0 mm.")
if highest3 == 2:
	print("The Prediction 3 days ahead is Light rain or 0.1 to 10 mm.")
if highest3 == 3:
	print("The Prediction 3 days ahead is Moderate rain or 10.1 to 50 mm.")
if highest3 == 4:
	print("The Prediction 3 days ahead is Heavy rain or 50.1 to 150 mm.")
if highest3 == 5:
	print("The Prediction 3 days ahead is Very heavy rain or more than 150mm.")

print("\n")