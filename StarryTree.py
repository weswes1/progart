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


starryNight = np.zeros((500,500,3))

# Background Color
for i in range(0,500):
	for j in range(0,500):
		starryNight[i,j]=[0,0,.54-.00108*i]


# More Stars
makeCircleFADETWO(5,[200,200],[0,0,.54],starryNight)
makeCircleFADETWO(4,[400,300],[0,0,.54],starryNight)
makeCircleFADETWO(3,[100,300],[0,0,.54],starryNight)
makeCircleFADETWO(2,[300,300],[0,0,.54],starryNight)
makeCircleFADETWO(6,[100,420],[0,0,.54],starryNight)
makeCircleFADETWO(4,[100,100],[0,0,.54],starryNight)
makeCircleFADETWO(4,[450,50],[0,0,.54],starryNight)
makeCircleFADETWO(5,[250,450],[0,0,.54],starryNight)

# Clouds

for j in range(0,10):
	for i in range(0,10):
		if i%2==0:
			makeCircleFADETWO(100-10*i-5*j,[100+20*i,200-20*i+20*j],[0,0,.54],starryNight)
		else:
			makeCircle(100-10*i-5*j,[100+20*i,200-20*i+20*j],[0,0,.54],starryNight)

averagemask(2,2,450,starryNight,1.0/9.0,100)

# Branch Section
lightEffect([250,250],300,100,[1,1,1],starryNight)
makeCircle(50,[450,450],[0,0,0],starryNight)
makeCircle(45,[410,410],[0,0,0],starryNight)
makeCircle(40,[370,370],[0,0,0],starryNight)
makeCircle(35,[330,340],[0,0,0],starryNight)
makeCircle(30,[280,340],[0,0,0],starryNight)
makeCircle(25,[240,320],[0,0,0],starryNight)
makeCircle(20,[220,300],[0,0,0],starryNight)
makeCircle(15,[200,290],[0,0,0],starryNight)
makeCircle(10,[190,290],[0,0,0],starryNight)
makeCircle(5,[180,290],[0,0,0],starryNight)

makeCircle(50,[450,200],[0,0,0],starryNight)
makeCircle(30,[400,200],[0,0,0],starryNight)
makeCircle(25,[375,200],[0,0,0],starryNight)
makeCircle(20,[350,200],[0,0,0],starryNight)
makeCircle(15,[325,200],[0,0,0],starryNight)
makeCircle(10,[315,200],[0,0,0],starryNight)
makeCircle(8,[300,200],[0,0,0],starryNight)

makeCircle(40,[350,40],[0,0,0],starryNight)
makeCircle(35,[330,60],[0,0,0],starryNight)
makeCircle(30,[300,90],[0,0,0],starryNight)
makeCircle(25,[270,120],[0,0,0],starryNight)
makeCircle(20,[240,120],[0,0,0],starryNight)
makeCircle(15,[210,120],[0,0,0],starryNight)
makeCircle(10,[190,130],[0,0,0],starryNight)
makeCircle(5,[177,130],[0,0,0],starryNight)

makeCircle(25,[350,475],[0,0,0],starryNight)
makeCircle(20,[325,450],[0,0,0],starryNight)
makeCircle(18,[315,430],[0,0,0],starryNight)
makeCircle(15,[300,420],[0,0,0],starryNight)
makeCircle(10,[280,420],[0,0,0],starryNight)
makeCircle(8,[280,415],[0,0,0],starryNight)
makeCircle(6,[270,415],[0,0,0],starryNight)
makeCircle(4,[270,415],[0,0,0],starryNight)
makeCircle(3,[263,415],[0,0,0],starryNight)





plt.imshow(starryNight, interpolation='nearest')
plt.show()