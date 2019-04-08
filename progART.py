

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


# Create the background color. it will be light brown.

# # # # # # # # # # # # # # # # # # # # # # # #  
for i in range(0,m):
	for j in range(0,n):
		image[i,j]=[0,.100,.203]
# # # # # # # # # # # # # # # # # # # # # # # # 


# JD's loop using 
x_0 = 78
y_0 = 41
d = 75

for i in range(0,10000):
	xi = random.uniform(0,1)
	th = random.uniform(0,1)*2*math.pi
	r = d*math.sqrt(xi/(1-xi))
	x = int(x_0+r*math.cos(th))
	y = int(y_0+r*math.sin(th))

	if (x>= 0 and x<500 and  y>=0 and y<500):
		image[int(x),int(y)]=[1,1,0]



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
guh = 0

while colstart < 250 :
	for pixel in range(0,lengthcurl):
		image[rowstart+random.randint(-10,10),colstart+random.randint(-2,2)]=[0,0,0]
		image[126-rowstart+random.randint(-10,10),122+colstart+random.randint(-2,2)]=[0,0,0]
	rowstart-=1
	colstart+=1


for row in range(0,75):
	for t in range(-1,guh):
		image[row+random.randint(-10,10),250-row+2*t+random.randint(-10,10)] = [0,0,0]
		image[row+random.randint(-10,10),250-row+2*t+random.randint(-10,10)] = [0,0,0]
	guh+=1


############################################ 
# Working on the EYES





##########################################



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


# Pupils:

for i in range(0,4):
	for j in range(0,4):
		image[103+i,303+j]=[0,0,0]

for i in range(0,4):
	for j in range(0,4):
		image[103+i,203+j]=[0,0,0]





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

for i in range(0,5):
	for j in range(0,10):
		image[110+i,300+j]=[0,0,0]
		image[110+i,200+j]=[0,0,0]

image[100,209]=[1,1,1]
image[100,309]=[1,1,1]

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 


# Making the mouth
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 


for i in range(0,40):
	for j in range(0,5):
		image[180+j,240+i]=[0,0,0]


for count in range(0,5):
	for i in range(0,7):
			image[182-i,280+i+count]=[0,0,0]

for i in range(0,5):
	for j in range(0,5):
		image[180+i,280+j]=[0,0,0]


# col start at 278
# row starts at 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 


# Making the nose
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
for i in range(0,7):
	for j in range(0,7):
		image[140+i,260+j]=[0,0,0]

for i in range(0,7):
	for j in range(0,7):
		image[140+i,267+j]=[0,0,0]

for i in range(0,7):
	for j in range(0,7):
		image[133+i,267+j]=[0,0,0]

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 



## Making the Flower portrait in the back right corner of the screen ##



for i in range(20,100):
	image[30+i,400]=[1,1,1]
	image[30+i,480]=[1,1,1]
	image[130,380+i]=[1,1,1]
	image[50,380+i]=[1,1,1]

for i in range(20,100):
	image[30+i,405]=[1,1,1]
	image[30+i,475]=[1,1,1]
	image[125,380+i]=[1,1,1]
	image[55,380+i]=[1,1,1]

for i in range(55,125):
	for j in range(405,475):
		image[i,j]=[0,0.5,0.5]

for j in range(0,30):
	for i in range(0,5):
		image[123-j,440+i]=[0.3,0,0.8]


# Rose petals

count = 1;
level = 0;

# starting point will be (level,)


while count <= 40:
	print(int(math.ceil(count/2)))
	for index in range(0,int(math.ceil(count/2))):
			image[level+60,442+index]=[.8**count,.5**index,03]
			image[level+60,442-index]=[0,.180,.5**index]
			image[100-level-2,442+index]=[.210,.12*index,.140]
			image[100-level-2,442-index]=[.210,.5**index,.140]
	level+=1;
	count+=2;



count = 1;
level = 0;

while count <= 40:
	for index in range(0,int(math.ceil(count/2))):
			image[level+80,442+index]=[.5**index,0,0]
			image[level+90,442-index]=[.5**index,.5**index,.5**index]
	level+=1;
	count+=2;


count = 1;
level = 0;


while count <= 40:
	for index in range(0,int(math.ceil(count/2))):
			image[level+90,430-index]=[.2**index,.1**index,0]
	level+=1;
	count+=2;

	


# Making a chain for the lanter lantern

for i in range(0,55):
	for j in range(40,45):
		image[i,j]=[0,0,0]

# Making the container of the candle

for i in range(50,55):
	for j in range(10,80):
		image[i+5,j]=[0,0,0]
		image[i+80,j]=[0,0,0]
		image[50+j,i+25]=[0,0,0]
		image[50+j,64-i]=[0,0,0]


for i in range(46,50):
	for j in range(34,50):
		image[i+80,j]=[0,0,0]


# Candle
for i in range(80,126):
	for j in range(40,45):
		image[i,j]=[1,.3,.4]


# Candle Fire
for i in range(75,85):
	for j in range(35,50):
		image[i,j]=[1,0,0]

for i in range(78,82):
	for j in range(40,45):
		image[i,j]=[1,1,0]

for x in range(0,10):
	image[74,38+x]=[1,1,0]

for x in range(0,8):
	image[73,39+x]=[1,1,0]

for x in range(0,3):
	image[72,42+x]=[1,1,0]


# Lantern glass effect
for z in range(0,5):
	for i in range(0,10):
		for j in range(0,20):
			image[129-z-i,13+j]=[0,0,0]
			image[129-z-i,75-j]=[0,0,0]
			image[58+z+i,13+j]=[0,0,0]
			image[58+z+i,75-j]=[0,0,0]



gaussianBlur = skimage.filters.gaussian(image,sigma=2)
plt.imshow(gaussianBlur, interpolation='nearest')
plt.show()

#plt.imshow(image, interpolation='nearest')
#plt.show()
