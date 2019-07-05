from matplotlib import pyplot as plt
from PIL import Image, ImageFilter
from skimage import filters, img_as_ubyte
from scipy import misc

import numpy as np
import math
import random
import skimage
import matplotlib.animation as animation
from artTools import *


wesleyGuergah = np.zeros((500,500,3))


# Makes the walls and colors them light blue
for i in range(0,500):			
	for j in range(0,500):
		if i > 350:
			wesleyGuergah[i,j]=[.93,.77,.57]
		else:
			wesleyGuergah[i,j] = [.9,.9,.98]

# Carpeting 

makeEllipse(75,200,[425,280],[.4,.4,.9],wesleyGuergah)

makeRect(35,5,[0,0,.3],[415,445],wesleyGuergah) # Leg
makeRect(35,5,[0,0,.3],[415,425],wesleyGuergah) # Leg
#

# Wren Painting


makeEllipse(75,50,[150,115],[.4,.26,.12],wesleyGuergah)
makeEllipse(70,45,[150,115],[.8,.7,1],wesleyGuergah)
makeRect(50,30,[1,.41,.7],[150,115],wesleyGuergah) 
makeEllipse(25,20,[150,115],[.89,.85,.60],wesleyGuergah)
makeEllipse(10,10,[116,115],[.89,.85,.60],wesleyGuergah)

for i in range(0,10): 											# Wren Arms
	makeCircle(5,[180-5*i,130-4*i],[.89,.85,.60],wesleyGuergah)
	makeCircle(5,[180-5*i,100+4*i],[.89,.85,.60],wesleyGuergah)

makeCircle(18,[156,114],[1,1,1],wesleyGuergah)
makeCircle(18,[145,114],[.89,.85,.60],wesleyGuergah)
makeCircle(2,[112,112],[1,1,1],wesleyGuergah)
makeCircle(2,[112,118],[1,1,1],wesleyGuergah)
makeCircle(1,[112,112],[0,0,1],wesleyGuergah)
makeCircle(1,[112,118],[0,0,1],wesleyGuergah)
makeCircle(2,[120,115],[1,.41,.7],wesleyGuergah)

for i in range(0,10):
	equaliteralTriange(8,[103,83+6*i],[0,0,.9],wesleyGuergah)
	equaliteralTriange(8,[200,83+6*i],[0,0,.9],wesleyGuergah) 




count=0

count0=0


for j in range(0,149):
	for i in range(0,149):
		wesleyGuergah[498-i-j,count0]=[.9,.9,.98]
		if i%3==0:
			count0+=1
	count0=0



# Making the wall/floor lines
for i in range(0,150):
	wesleyGuergah[499-i,count]=[0,0,0]
	if i%3==0:
		count+=1



for i in range(0,450):
	wesleyGuergah[350,50+i]=[0,0,0]

for i in range(0,350):
	wesleyGuergah[350-i,50]=[0,0,0]

# Making the Man's Torso


 # Couch

for i in range(0,20):
	for j in range(0,5):
		wesleyGuergah[350+i,355+j]=[0,0,0]
		wesleyGuergah[345+i,363+j]=[0,0,0]
		wesleyGuergah[350+i,455+j]=[0,0,0]
		wesleyGuergah[345+i,460+j]=[0,0,0]


for j in range(0,100):
	count2=50
	for i in range(0,28):
		wesleyGuergah[350-i,305+count2+j]=[.39,.26,.13]
		if i%1==0:
			count2+=1

for j in range(0,100):
	for i in range(0,30):
		wesleyGuergah[300+i,370+j]=[0.2,0.4,.8]

for i in range(0,10):
	makeCircle(10,[320+2*i,370-2*i],[0,0,.3],wesleyGuergah)
	makeCircle(10,[320+2*i,480-2*i],[0,0,.3],wesleyGuergah)

for i in range(0,10):
	makeCircle(8,[320+2*i,370-2*i],[1,1,.4],wesleyGuergah)
	makeCircle(8,[320+2*i,480-2*i],[1,1,.4],wesleyGuergah)


# Table Legs
makeRect(35,5,[.71,.39,.11],[431,131],wesleyGuergah)
makeRect(35,5,[.71,.39,.11],[431,297],wesleyGuergah)
makeRect(35,5,[.71,.39,.11],[336,330],wesleyGuergah)

# Table
for j in range(0,175):
	count2=125
	for i in range(0,100):
		wesleyGuergah[400-i,count2+j]=[.39,.26,.13]
		if i%3==0:
			count2+=1


# Coffee Cup
makeCircle(10,[340,290],[0,1,.3],wesleyGuergah)
makeCircle(8,[340,290],[.39,.26,.13],wesleyGuergah)


for i in range(0,10):
	makeEllipse(5,10,[332+2*i,298],[.8,.6,.3],wesleyGuergah)

makeEllipse(5,10,[333,298],[0,0,0],wesleyGuergah)

# Computer
for j in range(0,50):
	count2=200
	for i in range(0,40):
		wesleyGuergah[350-i,count2+j+5]=[.75,.75,.75]
		if i%3==0:
			count2+=1

makeRect(25,25,[.75,.75,.75],[290,243],wesleyGuergah)
makeRect(22,22,[0,0,0],[290,243],wesleyGuergah)

# Computer keys
for j in range(0,10):
	count2=200
	for i in range(0,10):
		makeRect(1,1,[0,0,0],[344-i*3,14+count2+j*4],wesleyGuergah)
		if i%3==0:
			count2+=3


# Mathematical equations

makeRect(1,3,[0,1,0],[281,230],wesleyGuergah)
makeRect(3,1,[0,1,0],[284,230],wesleyGuergah)
makeRect(1,1,[0,1,0],[283,236],wesleyGuergah)
makeCircle(4,[283,242],[0,1,0],wesleyGuergah)
makeCircle(2,[283,242],[0,0,0],wesleyGuergah)
makeCircle(4,[283,257],[0,1,0],wesleyGuergah)
makeCircle(2,[283,257],[0,0,0],wesleyGuergah)
makeRect(1,3,[0,1,0],[281,250],wesleyGuergah)
makeRect(1,3,[0,1,0],[285,250],wesleyGuergah)
makeRect(1,3,[0,1,0],[281,230],wesleyGuergah)
makeRect(3,1,[0,1,0],[284,230],wesleyGuergah)
makeRect(1,1,[0,1,0],[283,236],wesleyGuergah)
makeCircle(4,[283,242],[0,1,0],wesleyGuergah)
makeCircle(2,[283,242],[0,0,0],wesleyGuergah)
makeCircle(4,[283,258],[0,1,0],wesleyGuergah)
makeCircle(2,[283,258],[0,0,0],wesleyGuergah)
makeRect(1,3,[0,1,0],[281,250],wesleyGuergah)
makeRect(1,3,[0,1,0],[285,250],wesleyGuergah)
makeRect(1,3,[0,1,0],[293,230],wesleyGuergah)
makeRect(3,1,[0,1,0],[296,230],wesleyGuergah)
makeRect(1,1,[0,1,0],[295,236],wesleyGuergah)
makeCircle(4,[295,257],[0,1,0],wesleyGuergah)
makeCircle(2,[295,257],[0,0,0],wesleyGuergah)
makeRect(3,1,[0,1,0],[295,242],wesleyGuergah)
makeRect(1,3,[0,1,0],[293,250],wesleyGuergah)
makeRect(1,3,[0,1,0],[297,250],wesleyGuergah)






# Chair base
for j in range(0,80):
	count2=125
	for i in range(0,50):
		wesleyGuergah[455-i,45+count2+j]=[0,0,0]
		if i%3==0:
			count2+=1

makeEllipse(40,40,[375,210],[0,.75,0],wesleyGuergah)

# Back of Chair
makeRect(40,40,[1,0,0],[416,210],wesleyGuergah)



# Chair legs
makeRect(20,3,[0,0,0],[475,173],wesleyGuergah)
makeRect(20,3,[0,0,0],[475,248],wesleyGuergah)
makeRect(20,3,[0,0,0],[427,265],wesleyGuergah)

# Window Screen
makeRect(75,75,[0,0,0],[100,350],wesleyGuergah)
makeRect(70,70,[0,0,.5],[100,350],wesleyGuergah)

# Mountain outside of the Window
equaliteralTriange(140,[170,280],[0,.2,0],wesleyGuergah)
equaliteralTriange(50,[126,324],[1,1,1],wesleyGuergah)

# Cross Legged Man

makeEllipse(45,25,[350,435],[0,0,.8],wesleyGuergah) # Stomach
makeEllipse(20,10,[286,435],[.80,.70,.6],wesleyGuergah) # head
makeEllipse(2,2,[281,431],[1,1,1],wesleyGuergah) # eye
makeEllipse(2,2,[281,437],[1,1,1],wesleyGuergah) # eye
wesleyGuergah[281,431]=[0,0,0] # pupil
wesleyGuergah[281,437]=[0,0,0] # pupil
makeRect(1,3,[0,0,0],[292,436],wesleyGuergah) # Mouth


equaliteralTriange(40,[275,415],[.89,.85,.43],wesleyGuergah) # Hat
equaliteralTriange(20,[449,431],[0,0,0],wesleyGuergah) # Shoes
equaliteralTriange(20,[449,410],[0,0,0],wesleyGuergah) # Shoes


for i in range(0,40):							# Arm 1
	for j in range(0,8):
		wesleyGuergah[320+i,415+j-i]=[0,.5,1]

for i in range(0,40):							# Arm 2
	for j in range(0,6):
		wesleyGuergah[320+i,455-j]=[0,.5,1]




makeEllipse(10,30,[435,350],[0,0,0],wesleyGuergah) # Dog Torso
makeCircle(10,[428,378],[0,0,0],wesleyGuergah) # Head
makeCircle(1,[425,374],[1,1,1],wesleyGuergah) # Eye 1
makeCircle(1,[425,381],[1,1,1],wesleyGuergah) # Eye 2
equaliteralTriange(6,[419,379],[0,0,0],wesleyGuergah) # Ear 1
equaliteralTriange(6,[419,372],[0,0,0],wesleyGuergah) # Ear 2


makeRect(10,2,[0,0,0],[450,374],wesleyGuergah) # Leg
makeRect(10,2,[0,0,0],[450,369],wesleyGuergah) # Leg
makeRect(10,2,[0,0,0],[450,329],wesleyGuergah) # Leg
makeRect(10,2,[0,0,0],[450,334],wesleyGuergah) # Leg

for i in range(0,5):						   # Tail
	makeCircle(5-i,[434-3*i,325-3*i],[0,0,0],wesleyGuergah) 



equaliteralTriange(40,[275,415],[.89,.85,.43],wesleyGuergah) # Hat

for i in range(0,10):
	equaliteralTriange(10,[325+5*i,430],[0,i/10.0,0],wesleyGuergah)




# Wardrobe 
for k in range(0,100):
	for j in range(0,50):
		count2=20
		for i in range(0,50):
			wesleyGuergah[460-i-k,count2+j+10]=[.39,.26,.0]
			if i%3==0:
				count2+=1

for k in range(0,50):
	wesleyGuergah[360,k+30]=[0,0,0]
	wesleyGuergah[385,k+30]=[0,0,0]
	wesleyGuergah[410,k+30]=[0,0,0]
	wesleyGuergah[435,k+30]=[0,0,0]

for k in range(0,100):
	wesleyGuergah[460-k,80]=[0,0,0]
	wesleyGuergah[410-k,97]=[0,0,0]


anum = 0;
for i in range(0,50):	
	wesleyGuergah[360-i,80+anum]=[0,0,0]
	wesleyGuergah[455-i,80+anum]=[0,0,0]
	if i%3==0:
		anum+=1

for i in range(0,4):
	makeCircle(5,[375+23*i,55],[.8,.3,.5],wesleyGuergah)

# Wardrobe Top Painting
for i in range(0,5):
	for k in range(0,10):
		wesleyGuergah[330+k,70+k+i]=[0,0,0]

makeRect(18,18,[0,0,0],[340,60],wesleyGuergah)
makeRect(16,16,[1,.8,.8],[340,60],wesleyGuergah) 

for i in range(0,5):
	makeEllipse(10-i,10,[340+2*i,60],[0,0,i/5.0],wesleyGuergah) 
	makeCircle(5,[330+4*i,50],[0,i/5.0,0],wesleyGuergah)
	equaliteralTriange(10-i,[330,50+5*i],[i/10.0,0,0],wesleyGuergah)

"""
Peter Applebaum
"""

wesleyGuergah[410,k+30]=[0,0,0]

plt.imshow(wesleyGuergah, interpolation='nearest')
plt.show()