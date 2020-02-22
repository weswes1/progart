

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

[.210,.180,.140]
# Create the background color. it will be light brown.

# # # # # # # # # # # # # # # # # # # # # # # #  
for i in range(0,m):
	for j in range(0,n):
		image[i,j]=[0,.100,.203]
# # # # # # # # # # # # # # # # # # # # # # # # 


# JD's loop using probability density functions, the CDF, and a random variable
x_0 = 78
y_0 = 41
d = 75

for i in range(0,10000):
	xi = random.uniform(0,1)
	th = random.uniform(0,1)*2*math.pi
	r = d*math.sqrt(xi/(1-xi))
	x = int(x_0+r*math.cos(th))
	y = int(y_0+r*math.sin(th))

	if (x>= 0 and x<500 and  y >= 0 and y < 500):
		image[int(x),int(y)]=[1,1,0]




# carpeting in bottom left hand corner of the screen 

for i in range(0,37):
	for j in range(0,446):
			image[495-i,18+i+j]=[1,0,0]

# Carpeting design -- looping for center of circle A to center of circle B etcetera
# 469, 58 

	for j in range(0,40):
		for i in range(0,3):

			centerx = 469+10*i
			centery = 55+10*j

			for pix in range(centerx-5,5+centerx):
				for nutherpix in range(centery-5,5+centery):
					if (math.floor(math.pow((centerx-pix)**2+(centery-nutherpix)**2,.5)) < 5 ):
						image[pix-2,nutherpix+4]=[1,0,0]
					else:
						pass


	for j in range(0,40):
		for i in range(0,3):

			centerx = 469+10*i
			centery = 55+10*j

			for pix in range(centerx-5,5+centerx):
				for nutherpix in range(centery-5,5+centery):
					if (math.floor(math.pow((centerx-pix)**2+(centery-nutherpix)**2,.5)) < 4 ):
						image[pix-2,nutherpix+4]=[0,1,0]
					else:
						pass

	for j in range(0,40):
		for i in range(0,3):

			centerx = 469+10*i
			centery = 55+10*j

			for pix in range(centerx-5,5+centerx):
				for nutherpix in range(centery-5,5+centery):
					if (math.floor(math.pow((centerx-pix)**2+(centery-nutherpix)**2,.5)) < 3 ):
						image[pix-2,nutherpix+4]=[0,0,1]
					else:
						pass

	for j in range(0,40):
		for i in range(0,3):
			centerx = 469+10*i
			centery = 55+10*j

			for pix in range(centerx-5,5+centerx):
				for nutherpix in range(centery-5,5+centery):
					if (math.floor(math.pow((centerx-pix)**2+(centery-nutherpix)**2,.5)) < 2 ):
						image[pix-2,nutherpix+4]=[0,0,0]
					else:
						pass

for i in range(0,37):
	for j in range(0,3):
			image[495-i,i+20+2*j]=[0,0,0]
			image[495-i,462+i-2*j]=[0,0,0]

for i in range(0,20):
	for j in range(0,3):
			image[495-i,30+2*j+i]=[0,0,1]
			image[495-i,420+30+2*j+i]=[0,0,1]


# Creating some depth in the portrait

for z in range(0,3):
	for i in range(0,50):
		for i in range(0,50):
			image[499-i,i+z]=[0,0,0]

for z in range(0,3):
	for i in range(0,450):
		image[451-i,49+z]=[0,0,0]
		image[451+z,49+i]=[0,0,0]



# Making the torso
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
for i in range(220,500):
	for j in range(90,430):
		image[i,j]=[.1,.1,.1]
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# Creating the arm sleaves
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
for i in range(300,500):
	for col in range(353,360):
		image[i,col]=[0,0,.140]
		image[i,col-193]=[0,0,.140]
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 


## Boarder for the flower portrait ##
#####################################


for i in range(55,125):
	for j in range(405,475):
		image[i,j]=[.5,0,0]

		
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

for j in range(0,30):
	for i in range(0,5):
		image[123-j,440+i]=[0.3,0,0.8]
#####################################


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



# Japanese Kanji for DANCE/MAI

#####
for i in range(0,75):
	for j in range(0,50):
		image[i+10,95+j]=[.95,.95,.8]
####



###########################################
##
for i in range(0,5):
	image[17-i,107+i]=[0,0,0]
for i in range(0,5):
	image[26-i,107+i]=[0,0,0]
for i in range(0,7):
	image[30-i,109+i]=[0,0,0]
for i in range(0,3):
	image[24+i,111+i]=[0,0,0]
###


###

for i in range(0,15):
	image[23,110+i]=[0,0,0]

for i in range(0,10):
	image[26,116+i]=[0,0,0]
###



for i in range(0,3):
	image[23+i,118]=[0,0,0]

for i in range(0,8):
	image[21+i,121]=[0,0,0]

for z in range(0,4):
	for i in range(0,7):
		image[15+i,112+3*z]=[0,0,0]




#####
# Math Kanji


for i in range(0,5):
	image[38+i,107]=[0,0,0]
	image[40,105+i]=[0,0,0]
	image[45,105+i]=[0,0,0]

for i in range(0,5):
	image[42-i,105+i]=[0,0,0]
	image[42-i,109-i]=[0,0,0]

for i in range(0,5):
	image[45+i,109-i]=[0,0,0]


for i in range(0,3):
	image[45+i,107-i]=[0,0,0]

image[48,108]=[0,0,0]
image[44,107]=[0,0,0]

for i in range(0,6):
	image[43-i,111+i]=[0,0,0]

for i in range(0,6):
	image[41,113+i]=[0,0,0]

for i in range(0,7):
	image[41+i,113+i]=[0,0,0]

for i in range(0,8):
	image[41+i,117-i]=[0,0,0]




for i in range(0,10):
	image[40,120+i]=[0,0,0]
	image[45,120+i]=[0,0,0]

for i in range(0,6):
	image[42,122+i]=[0,0,0]

for i in range(0,3):
	image[48,122+i]=[0,0,0]

for i in range(0,5):
	image[48-i,124]=[0,0,0]

image[41,120]=[0,0,0]
image[41,129]=[0,0,0]

for i in range(0,3):
	image[44-i,124+i]=[0,0,0]


for i in range(0,3):
	image[40-i,127+i]=[0,0,0]

for i in range(0,3):
	image[40-i,126-i]=[0,0,0]


for i in range(0,3):
	image[40-i,123-i]=[0,0,0]


##############################
# Music Kanji
##############################

image[59,110]=[0,0,0]

for i in range(0,10):
	image[60,106+i]=[0,0,0]
for i in range(0,12):
	image[63,105+i]=[0,0,0]
for i in range(0,8):
	image[65,107+i]=[0,0,0]
for i in range(0,8):
	image[67,107+i]=[0,0,0]

for i in range(0,8):
	image[69,107+i]=[0,0,0]

for j in range(0,6):
	image[65+j,107]=[0,0,0]
	image[65+j,114]=[0,0,0]

for i in range(0,4):
	image[63-i,110-i]=[0,0,0]
	image[63-i,111+i]=[0,0,0]

###############################



for i in range(0,10):
	image[60,106+i]=[0,0,0]
for i in range(0,12):
	image[63,105+i]=[0,0,0]
for i in range(0,8):
	image[65,107+i]=[0,0,0]
for i in range(0,8):
	image[67,107+i]=[0,0,0]



for i in range(0,6):
	image[60,122+i]=[0,0,0]
for i in range(0,6):
	image[62,122+i]=[0,0,0]
for i in range(0,6):
	image[64,122+i]=[0,0,0]

for i in range(0,6):
	image[64,122+i]=[0,0,0]

for j in range(0,5):
	image[60+j,122]=[0,0,0]
	image[60+j,127]=[0,0,0]

for j in range(0,5):
	image[66+j,124]=[0,0,0]

for j in range(0,10):
	image[67,120+j]=[0,0,0]

for i in range(0,5):
	image[67+i,124-i]=[0,0,0]
	image[67+i,124+i]=[0,0,0]


for i in range(0,3):
	image[62+i,129+i]=[0,0,0]
	image[62-i,129+i]=[0,0,0]

for i in range(0,3):
	image[62+i,120-i]=[0,0,0]
	image[62-i,120-i]=[0,0,0]






for i in range(15,30):
	image[15,95+i]=[0,0,0]
	image[21,95+i]=[0,0,0]

for i in range(13,32):
	image[18,93+i]=[0,0,0]




################################
################################
################################
################################
################################
################################
################################
################################






# Working on the EYES


for i in range(0,10):
	for j in range(0,10):
		image[100+i,200+j]=[.210,.180,.140]
		image[100+i,300+j]=[.210,.180,.140]


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





# Rose petals

count = 1;
level = 0;

# starting point will be (level,)


while count <= 40:
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


# Coloring the glass of the lantern

for i in range(60,130):
	for j in range(15,75):
		image[i,j]=[0,.4,1]


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
	image[84,38+x]=[1,1,0]

for x in range(0,8):
	image[73,39+x]=[1,1,0]
	image[85,39+x]=[1,1,0]

for x in range(0,3):
	image[72,42+x]=[1,1,0]
	image[86,41+x]=[1,1,0]


# Lantern glass effect

for z in range(0,5):
	for i in range(0,10):
			image[129-z-i,13+i]=[0,0,0]
			image[129-z-i,75-i]=[0,0,0]
			image[58+z+i,13+i]=[0,0,0]
			image[58+z+i,75-i]=[0,0,0]

for i in range(0,55):
	for j in range(0,4):
		image[120-i,20+j]=[0,0,0]
		image[120-i,65+j]=[0,0,0]

for i in range(0,45):
	for j in range(0,4):
		image[67+j,65-i]=[0,0,0]
		image[117+j,65-i]=[0,0,0]





# Second painting-- Oranges
#####################################
##################################### 
#####################################

for i in range(20,80):
	image[130+i,390]=[1,1,1]
	image[130+i,450]=[1,1,1]
	image[210,370+i]=[1,1,1]
	image[150,370+i]=[1,1,1]

for i in range(20,80):
	image[130+i,395]=[1,1,1]
	image[130+i,445]=[1,1,1]
	image[205,370+i]=[1,1,1]
	image[155,370+i]=[1,1,1]

for i in range(157,204):
	for j in range(396,445):
		image[i,j]=[0,.2,.5]


for i in range(160,195):
	for j in range(400,435):
		image[i,j]=[0,0,0]


for i in range(163,192):
	for j in range(401,432):
		image[i,j]=[1,1,0]


for z in range(0,2):
	for i in range(0,5):
		image[195+i+z,400+i]=[0,0,0]
		image[195+i+z,434+i]=[0,0,0]
		image[195+i+z,434+i]=[0,0,0]
		image[160+i+z,434+i]=[0,0,0]



# Flower patterns
coljump = 0

while coljump<=28:
	rowjump = 0
	while rowjump <=20:
		for i in range(0,3):
			image[167+rowjump,404+i+coljump]=[0,rowjump/20,.5]
			image[167-i+rowjump,404-i+coljump]=[0,.5,.5]
			image[167-i+rowjump,404+i+coljump]=[rowjump/20,.5,.5]
			image[167+i+rowjump,404-i+coljump]=[0,.5,.5]
			image[167+rowjump,404-i+coljump]=[0,.5,.5]
			image[167+i+rowjump,404+coljump]=[rowjump/20,.5,.5]
			image[167-i+rowjump,404+coljump]=[0,.5,rowjump/20]
			image[167+i+rowjump,404+i+coljump]=[0,.5,rowjump/20]
		rowjump+=10
	coljump+=8









for z in range(0,2):
	for i in range(0,5):
		image[i,z]=[0,.3,.2]


# Center of the triangle is (420,179)

# If distance from pixel to (420,179) is less than radius, not filled


for i in range(157,204):
	for j in range(396,445):
		if (math.pow((420-j)**2+(179-i)**2,.5) < 4 ):
			image[i,j]=[1,.3,0]
		if (math.floor(math.pow((420-j)**2+(179-i)**2,.5)) == 4 ):
			image[i,j]=[0,0,0]
		else:
			pass

for i in range(157,204):
	for j in range(396,445):
		if (math.pow((420-j)**2+(179-i)**2,.5) < 4 ):
			image[i+4,j+3]=[1,.3,0]
		if (math.floor(math.pow((420-j)**2+(179-i)**2,.5)) == 4 ):
			image[i+4,j+3]=[0,0,0]
		else:
			pass

for i in range(157,204):
	for j in range(396,445):
		if (math.pow((420-j)**2+(179-i)**2,.5) < 4 ):
			image[i+3,j-3]=[1,.3,0]
		if (math.floor(math.pow((420-j)**2+(179-i)**2,.5)) == 4 ):
			image[i+3,j-3]=[0,0,0]
		else:
			pass

# White cat in the bottom right corner of the painting 



# center of the circle is (460,460)

for i in range(430,490):
	for j in range(430,490):
		if (math.pow((460-j)**2+(460-i)**2,.5) < 23 ):
			image[i+3,j-3]=[1,1,1]
		if (math.floor(math.pow((460-j)**2+(460-i)**2,.5)) == 23 ):
			image[i+3,j-3]=[0,0,0]
		else:
			pass



for i in range(430,490):
	for j in range(430,490):
		if (math.pow((443-j)**2+(478-i)**2,.5) < 6 ):
			image[i+3,j-3]=[1,1,1]
		if (math.floor(math.pow((443-j)**2+(478-i)**2,.5)) == 6 ):
			image[i+3,j-3]=[0,0,0]
		else:
			pass



for i in range(430,490):
	for j in range(430,490):
		if (math.pow((460-j)**2+(460-i)**2,.5) < 6 ):
			image[i+12,j+20]=[1,1,1]
		if (math.floor(math.pow((460-j)**2+(460-i)**2,.5)) == 6 ):
			image[i+12,j+20]=[0,0,0]
		else:
			pass



for i in range(430,490):
	for j in range(430,490):
		if (math.pow((460-j)**2+(460-i)**2,.5) < 13 ):
			image[i-15,j-3]=[1,1,1]
		if (math.floor(math.pow((460-j)**2+(460-i)**2,.5)) == 13 ):
			image[i-15,j-3]=[0,0,0]
		else:
			pass

# Cat ears

for i in range(0,4):
	image[432-i,464-i]=[1,1,1]
	image[432-i,451+i]=[1,1,1]
	image[429+i,461-i]=[1,1,1]
	image[430+i,455+i]=[1,1,1]



for i in range(0,2):
	image[442-i,464-i]=[0,0,0]
	image[442-i,451+i]=[0,0,0]
	image[441+i,462-i]=[0,0,0]
	image[441+i,453+i]=[0,0,0]

for i in range(0,2):
	for j in range(0,2):
		image[450+i,456+j]=[0,0,0]

for z in range(0,3):
	for i in range(0,7):
		if i%2==0:
			image[458-i-z,478+i] = [1,1,1]
			image[451+i-z,484+i]=[1,1,1]
		else:
			image[458-i-z,478+i] = [0,1,0]
			image[4+i-z,484+i]=[0,1,0]



# FILTERING section


"""

for i in range(1,499):
		for j in range(1,499):
			image[i,j]=(image[i+1,j]+image[i,j]+image[i-1,j]+image[i,j+1]+image[i,j-1]+image[i+1,j+1]+image[i-1,j-1]+image[i+1,j-1]+image[i-1,j+1])*1/9
for z in range(0,4):
	for i in range(70,87):
		for j in range(35,50):
			image[i,j]=(image[i+1,j]+image[i,j]+image[i-1,j]+image[i,j+1]+image[i,j-1]+image[i+1,j+1]+image[i-1,j-1]+image[i+1,j-1]+image[i-1,j+1])*1/9




#gaussianBlur = skimage.filters.gaussian(image,sigma=1)
#plt.imshow(gaussianBlur, interpolation='nearest')
#plt.show()



This is an interacrive history lesson called history quest with Peter Rouseau. Peter Rouseau is an arts affecionado and studied 
the Heian period of Japan for many years. The scroll you see on the wall of his room was a result of his attempt at japanese calligrpahy.
Recently, he has spent a lot of time decoding and stu
 
"""





"""
for pixel in range



"""







plt.imshow(image, interpolation='nearest')
plt.show()
