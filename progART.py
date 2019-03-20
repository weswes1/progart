

from matplotlib import pyplot as plt
from PIL import Image, ImageFilter
from skimage import filters, img_as_ubyte
from scipy import misc

import numpy as np
import math
import random
import skimage

image = np.zeros((500,500,3))

m = image.shape[0] # Rows
n = image.shape[1] # Columns


# Seth Spike Hacks / Cinderlla trails




# # # # # # # # # # # # # # # # # # # # # # # # 


# Create the background color. it will be light brown.
# # # # # # # # # # # # # # # # # # # # # # # # 
for i in range(0,m):
	for j in range(0,n):
		image[i,j]=[0,.100,.203]
# # # # # # # # # # # # # # # # # # # # # # # # 



# Making the torso
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
for i in range(220,500):
	for j in range(90,430):
		image[i,j]=[0,0,0]
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# Creating the arm sleaves
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
for i in range(300,500):
	for col in range(353,360):
		image[i,col]=[0,0,.140]
		image[i,col-193]=[0,0,.140]
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 


# Creates the button pattern for the man's frock
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
alevel = 240;
while alevel<= 500:
	acount = 1;
	while acount <= 30:
		for index in range(0,int(math.ceil(acount/2))):
				image[alevel-1,250+index]=[0,0,.140]
				image[alevel-1,250-index]=[0,0,.140]
				image[240-alevel-1,250+index]=[0,0,.140]
				image[240-alevel-1,250-index]=[0,0,.140]
		alevel+=1;
		acount+=2;

	alevel+=40
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 



# Creates a diamond shape for the FACE.
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
count = 1;
level = 0;
while count <= 250:
	for index in range(0,int(math.ceil(count/2))):
			image[level-1,250+index]=[.210,.180,.140]
			image[level-1,250-index]=[.210,.180,.140]
			image[250-level-2,250+index]=[.210,.180,.140]
			image[250-level-2,250-index]=[.210,.180,.140]
	level+=1;
	count+=2;
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 









# Randomized curly hair section
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
colstart = 122
rowstart = 126
arand = 0
lengthcurl = 30

while colstart < 250 :
	for pixel in range(0,lengthcurl):
		image[rowstart+random.randint(-10,10),colstart+random.randint(-2,2)]=[0,0,0]
		image[126-rowstart+random.randint(-10,10),122+colstart+random.randint(-2,2)]=[0,0,0]

	rowstart-=1
	colstart+=1

for col in range(227,270):
	for row in range(10,40):
		image[row,col]=[0,0,0]

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 






# Working on the EYES
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 



for i in range(0,10):
	for j in range(0,10):
		image[100+i,200+j]=[0,0,255]
		image[100+i,300+j]=[0,0,255]


for i in range(0,10):
	image[100,200+i]=[1,1,1]
	image[100+i,200]=[1,1,1]
	image[109,200+i]=[1,1,1]
	image[100+i,209]=[1,1,1]

	image[100,300+i]=[1,1,1]
	image[100+i,300]=[1,1,1]
	image[109,300+i]=[1,1,1]
	image[100+i,309]=[1,1,1]



# Eyebrows
for l in range(0,2):
	for x in range(0,18):
		image[95+l,193+x]=[0,0,0]
		image[95+l,293+x]=[0,0,0]

# Eye holders / Shape

for k in range(0,2):
	for x in range(0,8):
		image[98+k,200+x]=[0,0,0]
		image[98+x+k,200-x]=[0,0,0]
		image[110+k,200+x]=[0,0,0]
		image[106+x+k,192+x]=[0,0,0]
		image[98+x+k,208+x]=[0,0,0]
		image[106+x+k,216-x]=[0,0,0]
		image[98+k,300+x]=[0,0,0]
		image[98+x+k,300-x]=[0,0,0]
		image[110+k,300+x]=[0,0,0]
		image[106+x+k,292+x]=[0,0,0]
		image[98+x+k,308+x]=[0,0,0]
		image[106+x+k,316-x]=[0,0,0]

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 


# Making the mouth
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
for i in range(4,6):
	for j in range(0,4):
		image[100+i,203+j]=[0,0,0]
		image[100+i,303+j]=[0,0,0]
for i in range(0,40):
	for j in range(0,5):
		image[180+j,240+i]=[0,0,0]



# col start at 278
# row starts at 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 


# Making the nose
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
for i in range(0,7):
	for j in range(0,7):
		image[140+i,260+j]=[0,0,0]
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 


print(image.dtype)



#gaussianBlur = img_as_ubyte(image)
gaussianBlur = skimage.filters.gaussian(image,sigma=0.4)

plt.imshow(gaussianBlur, interpolation='nearest')
plt.show()

#plt.imshow(image, interpolation='nearest')
#plt.show()
