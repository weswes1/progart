"""
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
"""
import numpy as np
from matplotlib import pyplot as plt
from artTools import *
# rfRSUSM29p3AAJE   


Kimono = np.zeros((500,500,3))




for i in range(0,500):
	for j in range(0,500):
		Kimono[i,j]=[.95,.95,.8]

makeCircle(20,[160,225],[0,0,0],Kimono)
makeCircle(20,[160,175],[0,0,0],Kimono)

makeEllipse(20,10,[470,175],[1,1,1],Kimono)
makeEllipse(20,10,[470,223],[1,1,1],Kimono)

makeEllipse(100,50,[285,200],[.75,.75,1],Kimono)
makeRect(100,50,[.75,.75,1],[370,200],Kimono)

makeEllipse(90,40,[285,200],[.6,.6,.9],Kimono)
makeRect(90,40,[.6,.6,.9],[370,200],Kimono)





makeEllipse(50,25,[175,200],[1,1,1],Kimono)
makeCircle(25,[150,200],[0,0,0],Kimono)

for i in range(0,10):
	makeCircle(1,[480-i,175+i],[0,0,0],Kimono)
	makeCircle(1,[480-i,225+i],[0,0,0],Kimono)

	makeCircle(1,[480-i,175-i],[0,0,0],Kimono)
	makeCircle(1,[480-i,225-i],[0,0,0],Kimono)

for i in range(0,60):
	makeCircle(25,[150,200],[0,0,0],Kimono)


makeCircle(6,[182,188],[0,0,0],Kimono)
makeCircle(6,[182,208],[0,0,0],Kimono)

makeCircle(6,[180,188],[1,1,1],Kimono)
makeCircle(6,[180,208],[1,1,1],Kimono)
makeEllipse(3,6,[210,200],[1,0,0],Kimono)

makeCircle(6,[180,188],[1,1,1],Kimono)

makeCircle(5,[198,200],[0,0,0],Kimono)
makeCircle(5,[198,202],[1,1,1],Kimono)


vars=0
for i in range(0,60):
	if i%3==0:
		vars+=1
	Kimono[130+vars,170+i]=[1,1,0]
	Kimono[134+vars,170+i]=[1,1,0]

makeRect(8,8,[0,0,0],[140,200],Kimono)

makeRect(30,30,[1,0,0],[300,200],Kimono)
makeRect(25,25,[.5,0,0],[300,200],Kimono)

cars=0
for i in range(0,20):
	if i%2==0:
		cars+=1
	makeCircle(8,[290-3*i,195-3*cars],[.75,.75,1],Kimono)
	makeCircle(8,[235+3*i,239-3*cars],[.75,.75,1],Kimono)





plt.imshow(Kimono, interpolation='nearest')
plt.show()