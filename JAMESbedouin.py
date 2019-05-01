# James Bedouin

from matplotlib import pyplot as plt
from PIL import Image, ImageFilter
from skimage import filters, img_as_ubyte
from scipy import misc
import numpy as np
import math
import random
import skimage


black = [0,0,0]
white = [1,1,1]
blue = [0,0,1]
blonde = [.98,.941,.745]
sblonde = [.97,.91,.83]
pink = [.8,.38,.56]
jamesHouse = np.zeros((500,500,3))



m = jamesHouse.shape[0] # Rows
n = jamesHouse.shape[1] # Columns

# Makes a circle with center located at center, color of color, and radius of rad
# if pixel is less than rad pixels from the center

def makeCircle(rad,center,color):
	for i in range(center[0]-rad,center[0]+rad):
		for j in range(center[1]-rad,center[1]+rad):
			if (math.ceil(math.pow((i-center[0])**2 + (j-center[1])**2,.5)) <= rad):
				jamesHouse[i,j] = color

# Makes a rectangnle with height, width, and color centered at coordinates of center 	

def makeRect(height,width,color,center):
	for i in range(center[0]-height,center[0]+height):
		for j in range(center[1]-width,center[1]+width):
			jamesHouse[i,j]=color


# Creates a background color of white

def averagemask(rowstart,colstart,width,factor=1.0/9.0,t=1):
	for i in range(0,t):
		for i in range(rowstart,rowstart+width):
			for j in range(colstart,colstart+width):
				jamesHouse[i,j] = factor*(jamesHouse[i,j]+jamesHouse[i+1,j]+jamesHouse[i-1,j]+jamesHouse[i,j-1]+jamesHouse[i+1,j-1]+jamesHouse[i-1,j-1]+jamesHouse[i,j+1]+jamesHouse[i+1,j+1]+jamesHouse[i-1,j+1])






for i in range(0,m):
	for j in range(0,n):
		jamesHouse[i,j] = [random.uniform(0,1)/2,0,random.uniform(0,1)/2]


makeCircle(60,[150,250],[.8,.71,.54])		# Head



## Hair Section VVV VVV VVV VVV VVV VVV VVV VVV VVV
for z in range(0,4):
	for j in range(0,5):
		x_0 = 110-5*z
		y_0 = 210+j*20
		d = 5
		for i in range(0,1000):
			xi = random.uniform(0,1)
			th = random.uniform(0,1)*2*math.pi
			r = d*math.sqrt(xi/(1-xi))
			x = int(x_0+r*math.cos(th))
			y = int(y_0+r*math.sin(th))

			if (x>= 0 and x<500 and  y >= 0 and y < 500):
				jamesHouse[int(x),int(y)] = blonde

x_0 = 80
y_0 = 250
d = 5
for i in range(0,1000):
	xi = random.uniform(0,1)
	th = random.uniform(0,1)*2*math.pi
	r = d*math.sqrt(xi/(1-xi))
	x = int(x_0+r*math.cos(th))
	y = int(y_0+r*math.sin(th))

	if (x>= 0 and x<500 and  y >= 0 and y < 500):
		jamesHouse[int(x),int(y)] = blonde



x_0 = 122
y_0 = 198
d = 5
for i in range(0,1000):
	xi = random.uniform(0,1)
	th = random.uniform(0,1)*2*math.pi
	r = d*math.sqrt(xi/(1-xi))
	x = int(x_0+r*math.cos(th))
	y = int(y_0+r*math.sin(th))

	if (x>= 0 and x<500 and  y >= 0 and y < 500):
		jamesHouse[int(x),int(y)] = blonde


x_0 = 122
y_0 = 298
d = 5
for i in range(0,1000):
	xi = random.uniform(0,1)
	th = random.uniform(0,1)*2*math.pi
	r = d*math.sqrt(xi/(1-xi))
	x = int(x_0+r*math.cos(th))
	y = int(y_0+r*math.sin(th))

	if (x>= 0 and x<500 and  y >= 0 and y < 500):
		jamesHouse[int(x),int(y)] = blonde


x_0 = 82
y_0 = 227
d = 5
for i in range(0,1000):
	xi = random.uniform(0,1)
	th = random.uniform(0,1)*2*math.pi
	r = d*math.sqrt(xi/(1-xi))
	x = int(x_0+r*math.cos(th))
	y = int(y_0+r*math.sin(th))

	if (x>= 0 and x<500 and  y >= 0 and y < 500):
		jamesHouse[int(x),int(y)] = blonde

x_0 = 82
y_0 = 273
d = 5
for i in range(0,1000):
	xi = random.uniform(0,1)
	th = random.uniform(0,1)*2*math.pi
	r = d*math.sqrt(xi/(1-xi))
	x = int(x_0+r*math.cos(th))
	y = int(y_0+r*math.sin(th))

	if (x>= 0 and x<500 and  y >= 0 and y < 500):
		jamesHouse[int(x),int(y)] = blonde



makeRect(30,20,[.8,.71,.54],[200,250])		# Neck

makeCircle(30,[259,150],pink)				# Shoulder pad 1
makeCircle(30,[259,350],pink)				# Shoulder pad 2
makeRect(135,90,pink,[365,250])			# Making the man's garb
makeRect(90,20,pink,[350,140])			# Making the man's sleeve
makeRect(90,20,pink,[350,360])			# Making the man's sleeve

makeRect(75,75,[0,0,0],[100,400])			# Making the frame for the arabic calligraphy
makeRect(65,65,[.95,.95,.8],[100,400])			# """""""""""""""""""""""""""""""""""""""""""

# VVVVVV Creating the painting --- It will be made using many circles VVVVVVV ---

makeCircle(3,[105,355],black)
makeCircle(4,[109,352],black)
makeCircle(5,[112,353],black)
makeCircle(5,[116,352],black)
makeCircle(5,[119,355],black)
makeCircle(5,[121,358],black)
makeCircle(5,[121,360],black)
makeCircle(5,[119,362],black)
makeCircle(5,[117,364],black)
makeCircle(5,[114,366],black)
makeCircle(5,[111,368],black)
makeCircle(5,[108,370],black)
makeCircle(5,[105,372],black)
makeCircle(5,[102,374],black)
makeCircle(5,[102,376],black)
makeCircle(4,[104,376],black)
makeCircle(4,[106,377],black)
makeCircle(3,[108,377],black)
makeCircle(3,[110,378],black)
makeCircle(3,[112,378],black)

makeCircle(4,[114,377],black)
makeCircle(4,[116,377],black)
makeCircle(4,[118,377],black)
makeCircle(4,[118,377],black)
makeCircle(4,[120,377],black)
makeCircle(4,[122,377],black)
makeCircle(4,[124,377],black)
makeCircle(4,[126,377],black)
makeCircle(4,[128,377],black)
makeCircle(4,[130,377],black)
makeCircle(4,[132,377],black)
makeCircle(4,[134,377],black)

makeCircle(4,[136,377],black)
makeCircle(4,[138,377],black)
makeCircle(4,[140,377],black)
makeCircle(5,[142,379],black)
makeCircle(6,[144,381],black)

makeCircle(6,[144,383],black)
makeCircle(5,[143,386],black)
makeCircle(5,[141,389],black)
makeCircle(5,[139,392],black)
makeCircle(4,[138,393],black)
makeCircle(4,[137,394],black)
makeCircle(5,[135,394],black)



for i in range(0,20):
	makeCircle(4,[133-2*i,395],black)


makeCircle(5,[137,395],black)
makeCircle(5,[138,396],black)
makeCircle(5,[139,397],black)
makeCircle(5,[140,398],black)
makeCircle(5,[141,399],black)
makeCircle(5,[142,400],black)

makeCircle(6,[143,400],black)
makeCircle(5,[143,401],black)
makeCircle(5,[144,402],black)
makeCircle(5,[145,403],black)
makeCircle(5,[146,404],black)
makeCircle(5,[146,404],black)
makeCircle(5,[146,405],black)
makeCircle(5,[146,406],black)

makeCircle(5,[146,404],black)
makeCircle(5,[146,404],black)
makeCircle(5,[146,405],black)
makeCircle(5,[146,406],black)
makeCircle(5,[145,407],black)
makeCircle(5,[144,407],black)
makeCircle(5,[143,408],black)
makeCircle(5,[142,409],black)
makeCircle(4,[141,410],black)
makeCircle(5,[140,411],black)
makeCircle(4,[139,412],black)

for i in range(0,23):
	makeCircle(4,[142-2*i,412],black)

makeCircle(3,[96,415],black)
makeCircle(3,[98,417],black)
makeCircle(3,[100,419],black)
makeCircle(3,[102,421],black)
makeCircle(3,[104,421],black)

makeCircle(2,[106,421],black)
makeCircle(2,[108,421],black)
makeCircle(1,[110,421],black)


for i in range(0,33):
	makeCircle(4,[141-2*i,432],black)

for i in range(0,5):
	makeCircle(4,[88+2*i,433+2*i],black)

makeCircle(3,[100,443],black)
makeCircle(2,[103,443],black)

for i in range(0,12):
	makeCircle(2,[83-i,363+i],black)

makeCircle(2,[70,375],black)
makeCircle(2,[68,375],black)
makeCircle(2,[66,374],black)
makeCircle(2,[64,373],black)
makeCircle(2,[64,372],black)
makeCircle(2,[64,370],black)
makeCircle(2,[64,368],black)

makeCircle(2,[66,366],black)
makeCircle(2,[68,364],black)

makeCircle(2,[70,364],black)
makeCircle(2,[72,366],black)
makeCircle(2,[74,368],black)
makeCircle(2,[76,370],black)
makeCircle(2,[78,372],black)
makeCircle(2,[80,374],black)


for i in range(0,10):
	makeCircle(2,[73+i,395],black)
	makeCircle(2,[73+i,387],black)
	makeCircle(2,[73+i,403],black)

makeCircle(2,[79,391],black)
makeCircle(2,[80,389],black)


makeCircle(2,[79,398],black)
makeCircle(2,[80,399],black)

for i in range(0,8):
	makeCircle(1,[63-i,393],black)

for i in range(0,3):
	makeCircle(1,[55+i,393+i],black)


for i in range(0,15):
	makeCircle(1,[80-i,418+i],black)

makeCircle(1,[81,376],black)
makeCircle(1,[81,377],black)

# ^^^^^^^^ ^^^^^^^^ ^^^^^^^^ ^^^^^^^^ ^^^^^^^^ ^^^^^^^^ Making the portrait
# ^^^^^^^^ ^^^^^^^^ ^^^^^^^^ ^^^^^^^^ ^^^^^^^^ ^^^^^^^^ Making the portrait
# ^^^^^^^^ ^^^^^^^^ ^^^^^^^^ ^^^^^^^^ ^^^^^^^^ ^^^^^^^^ Making the portrait


# VVVVVVVVVVVVVV Sunset Painting

makeRect(55,55,black,[151,99])
makeRect(50,51,[.06,.08,.38],[150,99])

makeCircle(10,[120,70],[.96,.94,.76])
makeCircle(10,[120,75],[.06,.08,.38])

for  i in range(100,165):
	for j in range(50,150):
		if (random.uniform(0,1)<.05):
			jamesHouse[i,j]=[1,1,1]



x_0 = 160
y_0 = 100
d = 5

for i in range(0,15000):
	xi = random.uniform(0,1)
	th = random.uniform(0,1)*2*math.pi
	r = d*math.sqrt(xi/(1-xi))
	x = int(x_0+r*math.cos(th))
	y = int(y_0+r*math.sin(th))

	if (x >= 0 and x <500 and  y >= 0 and y < 500):
		jamesHouse[int(x),int(y)] = [1,0,0]

x_0 = 160
y_0 = 100
d = 5

for i in range(0,5000):
	xi = random.uniform(0,1)
	th = random.uniform(0,1)*2*math.pi
	r = d*math.sqrt(xi/(1-xi))
	x = int(x_0+r*math.cos(th))
	y = int(y_0+r*math.sin(th))

	if (x >= 0 and x <500 and  y >= 0 and y < 500):
		jamesHouse[int(x),int(y)] = [1,.64,0]



x_0 = 160
y_0 = 100
d = 5

for i in range(0,1000):
	xi = random.uniform(0,1)
	th = random.uniform(0,1)*2*math.pi
	r = d*math.sqrt(xi/(1-xi))
	x = int(x_0+r*math.cos(th))
	y = int(y_0+r*math.sin(th))

	if (x >= 0 and x < 500 and  y >= 0 and y < 500):
		jamesHouse[int(x),int(y)] = [1,1,0]


for i in range(165,200):
	for j in range(48,150):
		jamesHouse[i,j]=[0,0,.3]


for i in range(166,200):
	for j in range(81,121):
		if (random.uniform(0,1) < .03 ):
			jamesHouse[i,j]=[1,1,1]

averagemask(100,50,100,t=3)




# ^^^^^^^^^^ Sunset
# ^^^^^^^^^^ Sunset
# ^^^^^^^^^^ Sunset

## VVV Making the eye section VVV
## VVV Making the eye section VVV
## VVV Making the eye section VVV


makeCircle(2,[136,217],black)
makeCircle(3,[136,219],black)
makeCircle(4,[136,221],black)
makeCircle(5,[136,223],black)
makeCircle(4,[136,225],black)
makeCircle(3,[136,227],black)
makeCircle(2,[136,229],black)

makeCircle(2,[136,277],black)
makeCircle(3,[136,279],black)
makeCircle(4,[136,281],black)
makeCircle(5,[136,283],black)
makeCircle(4,[136,285],black)
makeCircle(3,[136,287],black)
makeCircle(2,[136,289],black)

makeCircle(4,[136,283],white)
makeCircle(4,[136,223],white)
makeCircle(3,[136,283],blue)
makeCircle(3,[136,223],blue)
makeCircle(2,[136,283],black)
makeCircle(2,[136,223],black)

# ^^^^ Making the eye section ^^^^
## ^^^^ Making the eye section ^^^^
## ^^^^ Making the eye section ^^^^

# VVV Making the nose VVVV
# VVV Making the nose VVVV
# VVV Making the nose VVVV

makeCircle(2,[156,251],black)
makeCircle(2,[159,250],black)
makeCircle(2,[159,252],black)
makeCircle(2,[159,253],black)

makeCircle(2,[179,260],black)
makeCircle(2,[180,257],black)
makeCircle(4,[180,253],black)
makeCircle(3,[180,249],black)
makeCircle(2,[180,245],black)
makeCircle(2,[179,242],black)

## ^^^^ Making the nose section ^^^^
## ^^^^ Making the nose section ^^^^
## ^^^^ Making the nose section ^^^^

### VVVVV James' T Shirt Patterns

for k in range(0,30):
	for i in range(0,5):
		d = float(i)
		makeCircle(4*i,[375-20*i+k,250+k],[0,d/10.0,d/5])
		makeCircle(4*i,[375+20*i+k,250+k],[d/5.0,0,d/10.0])
		makeCircle(4*i,[375+k,250+10*i+k],[0,d/10.0,0])
		makeCircle(4*i,[375+k,250-10*i+k],[d/10.0,0,d/10.0])


### ^^^^ James' T Shirt patterns

# random.uniform(0,1)/2,0,random.uniform(0,1)/2]
### VVVVVV James' Beard Goatee VVVVVV

for i in range(0,10):
	makeCircle(i,[290-10*i,250],sblonde)

### ^^^ James' Beard Goatee ^^^^ ######


# Lining for the shirt

for i in range(230,442):
		jamesHouse[i,339]=black
		jamesHouse[i,160]=black


# [.8,.71,.54] color for finger

### VVV fingers VVVVVV fingers VVVVVV fingers VVVVVV fingers VVV
makeCircle(3,[442,345],[.8,.71,.54])
makeCircle(3,[446,352],[.8,.71,.54])
makeCircle(3,[442,352],[.8,.71,.54])
makeCircle(3,[446,352],[.8,.71,.54])
makeCircle(3,[442,359],[.8,.71,.54])
makeCircle(3,[446,359],[.8,.71,.54])
makeCircle(3,[442,366],[.8,.71,.54])
makeCircle(3,[446,366],[.8,.71,.54])
makeCircle(3,[442,372],[.8,.71,.54])
makeCircle(3,[446,372],[.8,.71,.54])

makeCircle(3,[442,153],[.8,.71,.54])
makeCircle(3,[446,125],[.8,.71,.54])
makeCircle(3,[442,125],[.8,.71,.54])
makeCircle(3,[446,132],[.8,.71,.54])
makeCircle(3,[442,132],[.8,.71,.54])
makeCircle(3,[446,132],[.8,.71,.54])
makeCircle(3,[442,139],[.8,.71,.54])
makeCircle(3,[446,139],[.8,.71,.54])
makeCircle(3,[442,139],[.8,.71,.54])
makeCircle(3,[446,146],[.8,.71,.54])
makeCircle(3,[442,146],[.8,.71,.54])
makeCircle(3,[446,146],[.8,.71,.54])

### ^^^^ Fingers Fingers Fingers ^^^^^^^^^^^^^^^^^^^^^^^^
### ^^^^ Fingers Fingers Fingers ^^^^^^^^^^^^^^^^^^^^^^^^
### ^^^^ Fingers Fingers Fingers ^^^^^^^^^^^^^^^^^^^^^^^^


### VV Third Portrait, trippy patterns VV
### VV Third Portrait, trippy patterns VV


makeCircle(47,[250,449],blue)
makeCircle(45,[250,449],white)
for i in range(0,10):
	if i%2==0:
		makeCircle(45-4*i,[250,449],white)
	else:
		makeCircle(45-4*i,[250,449],blue)




for k in range(0,10):
	for i in range(0,4):
			d = float(i)
			makeCircle(i,[250-8*i+k,440+k],[0,d/10.0,d/5])
			makeCircle(i,[250+8*i+k,440+k],[d/5.0,0,d/10.0])
			makeCircle(i,[250+k,440+8*i+k],[0,d/10.0,0])
			makeCircle(i,[250+k,440-8*i+k],[d/10.0,0,d/10.0])

for k in range(0,10):
	for i in range(0,4):
			d = float(i)
			makeCircle(i,[250-8*i-k,440+k],[0,d/10.0,d/5])
			makeCircle(i,[250+8*i-k,440+k],[d/5.0,0,d/10.0])
			makeCircle(i,[250-k,440+8*i+k],[0,d/10.0,0])
			makeCircle(i,[250-k,440-8*i+k],[d/10.0,0,d/10.0])

for k in range(0,10):
	for i in range(0,4):
			d = float(i)
			makeCircle(i,[250-8*i+k,450+k],[0,d/10.0,d/5])
			makeCircle(i,[250+8*i+k,450+k],[d/5.0,0,d/10.0])
			makeCircle(i,[250+k,450+8*i+k],[0,d/10.0,0])
			makeCircle(i,[250+k,450-8*i+k],[d/10.0,0,d/10.0])

for k in range(0,10):
	for i in range(0,4):
			d = float(i)
			makeCircle(i,[250-8*i-k,450+k],[0,d/10.0,0])
			makeCircle(i,[250+8*i-k,450+k],[d/5.0,0,0])
			makeCircle(i,[250-k,450+8*i+k],[0,d/10.0,0])
			makeCircle(i,[250-k,450-8*i+k],[d/10.0,0,0])




### ^^ Third Portrait, trippy patterns ^^
### ^^ Third Portrait, trippy patterns ^^

plt.imshow(jamesHouse, interpolation='nearest')
plt.show()

