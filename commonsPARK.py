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


commonsPark = np.zeros((500,500,3))

for i in range(0,500):
	for j in range(0,500):
		commonsPark[i,j]=[0,0,.33]

for j in range(0,20):
	for i in range(0,10):
		makeCircle(100-10*i-j*5,[400-40*i,400-i*i],[.5-.05*i,.5-.05*i,.5],commonsPark)

for i in range(0,10):
	makeCircleFADETWO(30-3*i,[100+40*i,100+i*i],[0,0,i/10],commonsPark)

for i in range(0,10):
	makeCircleFADE(30-3*i,[100+40*i,100-i*i],[0,0,1-i/10.0],commonsPark)


for j in range(0,20):
	for i in range(0,5):
		makeRect(80-10*i,50-10*i,[.8-.066*i,0,0],[250+j,220+j],commonsPark)

for j in range(0,20):
	for i in range(0,10):
		equaliteralTriange(75-10*i,[480+j,20+5*i-j],[0,0,1-.1*i],commonsPark)
		equaliteralTriange(75-10*i,[480+j,70+5*i-j],[0,1-.1*i,0],commonsPark)
		equaliteralTriange(75-10*i,[480+j,120+5*i-j],[1-.1*i,0,0],commonsPark)


# $$$ Han Giru $$$



for i in range(0,12):
	makeCircle(4,[42-2*i,206+2*i],[1,i/20.0,0],commonsPark)


for i in range(0,10):
	makeCircle(5,[10+5*i,90+i],[1,i/20.0,0],commonsPark)
	makeCircle(5,[10+5*i,160+i],[1,0,i/20.0],commonsPark)
	makeCircle(5,[10+5*i,16],[1,.3,i/30.0],commonsPark)
	makeCircle(5,[10+5*i,36],[1,.3,i/30.0],commonsPark)
	makeCircle(5,[30,20+2*i],[1,.3,i/30.0],commonsPark)

	

for i in range(0,15):
	makeCircle(4,[20,150+2*i],[1,i/20.0,0],commonsPark)
	makeCircle(4,[20,200+2*i],[1,i/20.0,0],commonsPark)
	makeCircle(4,[35,152+2*i],[1,i/20.0,0],commonsPark)



makeCircle(2,[10,180],[0,1,0],commonsPark)
makeCircle(2,[10,185],[0,1,0],commonsPark)

makeCircle(5,[40,98],[0,0,1],commonsPark)
makeCircle(5,[35,105],[1,0,0],commonsPark)
makeCircle(5,[38,110],[0,0,1],commonsPark)
makeCircle(5,[45,115],[1,0,0],commonsPark)
makeCircle(5,[50,120],[1,0,1],commonsPark)
makeCircle(5,[53,125],[1,0,0],commonsPark)
makeCircle(5,[50,128],[1,0,1],commonsPark)

makeCircle(15,[50,64],[1,0,0],commonsPark)
makeCircle(13,[50,64],[0,0,.33],commonsPark)

makeCircle(5,[60,80],[1,0,0],commonsPark)
makeCircle(3,[60,80],[0,0,.33],commonsPark)


makeCircle(16,[54,216],[1,0,0],commonsPark)
makeCircle(13,[54,213],[0,0,.33],commonsPark)
makeCircle(5,[62,208],[1,0,0],commonsPark)
makeCircle(4,[62,210],[0,0,.33],commonsPark)

plt.imshow(commonsPark, interpolation='nearest')
plt.show()

