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

jamesHouse = np.zeros((500,500,3))



m = jamesHouse.shape[0] # Rows
n = jamesHouse.shape[1] # Columns


# Creates a background color of white
for i in range(0,m):
	for j in range(0,n):
		jamesHouse[i,j] = white


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




makeCircle(60,[150,250],[.8,.71,.54])		# Head
makeRect(30,20,[.8,.71,.54],[200,250])		# Neck
makeCircle(30,[259,150],black)			# Shoulder pad 1
makeCircle(30,[259,350],black)			# Shoulder pad 2
makeRect(120,90,[0,0,0],[350,250])			# Making the man's garb
makeRect(75,75,[0,0,0],[100,400])			# Making the frame for the arabic calligraphy
makeRect(65,65,[1,1,1],[100,400])			# """""""""""""""""""""""""""""""""""""""""""

# VVVVVV Creating the painting -- It will be made using many circles VVVVVVV
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


plt.imshow(jamesHouse, interpolation='nearest')
plt.show()

