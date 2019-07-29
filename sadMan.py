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

green = [0,.6,0]
green_two = [0,.7,0]
green_three=[0,.5,0]
sadMan = np.zeros((500,500,3))

m=500

# Make entire background white VVV
for i in range(0,m):
	for j in range(0,m):
		sadMan[i,j]=[0,0,.75]
# Make entire background white ^^^

# Make some background dark brown 

for i in range(240,500):
	for j in range(0,500):
		sadMan[i,j]=[0,.3,0]


# Making the lake in the park VVV
makeEllipse(100,200,[350,250],[0,1,1],sadMan)
# Making the lake in the park ^^^


# Wave effects VVV
for i in range(0,99):
	if i%2==0:
		makeEllipse(100-i,200-2*i,[350,250],[0,1,1],sadMan)
	else:
		makeEllipse(100-i,200-2*i,[350,250],[0,.9,.9],sadMan)

for i in range(0,99):
	if i%2==0:
		makeEllipse(105-i,202-2*i,[352,253],[0,1,1],sadMan)
	else:
		makeEllipse(105-i,202-2*i,[352,251],[0,.9,.9],sadMan)

# Wave effects ^^^





# Making some clouds VVV

for i in range(0,80):
	for j in range(0,500):
		sadMan[i,j]=[.9,.9,.9]

makeEllipse(100,130,[100,370],[0,0,0],sadMan)
makeEllipse(100,130,[99,369],[.9,.9,.9],sadMan)

makeEllipse(80,101,[78,100],[0,0,0],sadMan)
makeEllipse(79,100,[78,100],[.9,.9,.9],sadMan)

makeEllipse(60,40,[121,401],[0,0,0],sadMan)
makeEllipse(60,40,[120,400],[.9,.9,.9],sadMan)

makeEllipse(60,40,[120,400],[0,0,0],sadMan)
makeEllipse(60,40,[120,400],[.9,.9,.9],sadMan)

makeEllipse(51,101,[70,250],[0,0,0],sadMan)
makeEllipse(50,100,[70,250],[.9,.9,.9],sadMan)

makeEllipse(31,91,[80,200],[0,0,0],sadMan)
makeEllipse(30,90,[80,200],[.9,.9,.9],sadMan)

makeEllipse(31,70,[50,430],[0,0,0],sadMan)
makeEllipse(30,69,[50,430],[.9,.9,.9],sadMan)


makeEllipse(15,60,[80,380],[0,0,0],sadMan)
makeEllipse(15,60,[79,379],[.9,.9,.9],sadMan)

# Making some storm clouds ^^^

# Tree Section

makeRect(60,5,[0,.2,0],[325,30],sadMan)
makeRect(3,30,[0,.2,0],[345,30],sadMan)
makeRect(2,25,[0,.2,0],[325,30],sadMan)
makeRect(2,15,[0,.2,0],[305,30],sadMan)
makeRect(1,10,[0,.2,0],[285,30],sadMan)


"""
lightEffect([270,105],3,1000,[.85,.6,.6],sadMan)
lightEffect([260,100],2,500,[.85,.6,.6],sadMan)
lightEffect([260,95],1,100,[.85,.6,.6],sadMan)
lightEffect([260,90],2,500,[.9,.64,.55],sadMan)
lightEffect([250,85],1,100,[.9,.64,.55],sadMan)
lightEffect([250,80],3,1000,[.9,.64,.55],sadMan)
lightEffect([250,75],2,500,[.85,.6,.6],sadMan)
lightEffect([235,70],1,100,[.9,.64,.55],sadMan)
lightEffect([235,65],2,500,[.85,.6,.6],sadMan)
lightEffect([235,60],1,100,[.9,.64,.55],sadMan)
lightEffect([220,55],2,100,[.9,.64,.55],sadMan)
lightEffect([220,50],2,100,[.85,.6,.6],sadMan)
lightEffect([220,45],2,100,[.85,.6,.6],sadMan)
"""


lightEffect([345,30],8,1000,[0,.9,0],sadMan)
lightEffect([345,30],8,1000,[0,.9,0],sadMan)
lightEffect([345,30],8,1000,[0,.9,0],sadMan)
lightEffect([325,30],8,1000,[0,.9,0],sadMan)
lightEffect([325,30],5,500,[0,.9,0],sadMan)
lightEffect([325,30],5,500,[0,.9,0],sadMan)
lightEffect([305,30],8,1000,[0,.9,0],sadMan)
lightEffect([285,30],8,1000,[0,.9,0],sadMan)
lightEffect([265,30],3,1000,[0,.9,0],sadMan)

makeRect(40,2,[0,.2,0],[435,50],sadMan)
lightEffect([445,50],7,1000,[0,.85,0],sadMan)
lightEffect([419,50],6,500,[0,.85,0],sadMan)
lightEffect([395,50],5,100,[0,.85,0],sadMan)

makeRect(40,5,[0,.2,0],[450,100],sadMan)
lightEffect([465,100],5,10000,green,sadMan)
lightEffect([439,100],4,5000,green,sadMan)
lightEffect([415,100],3,1000,green,sadMan)

makeRect(40,5,[0,.2,0],[460,440],sadMan)
lightEffect([470,440],4,10000,green_two,sadMan)
lightEffect([440,440],3,5000,green_two,sadMan)
lightEffect([420,440],2,1000,green_two,sadMan)

makeRect(40,5,[0,.2,0],[420,340],sadMan)
lightEffect([430,340],4,10000,green_two,sadMan)
lightEffect([400,340],3,5000,green_two,sadMan)
lightEffect([380,340],2,1000,green_two,sadMan)


makeRect(40,3,[0,.2,0],[440,400],sadMan)
lightEffect([450,400],4,5000,[.2,.5,.1],sadMan)
lightEffect([420,400],3,2500,[.2,.5,.1],sadMan)
lightEffect([400,400],2,1000,[.2,.5,.1],sadMan)

makeRect(40,1,[0,.2,0],[340,50],sadMan)
lightEffect([360,50],3,2500,[.2,.5,.15],sadMan)
lightEffect([345,50],2,2500,[.2,.5,.15],sadMan)
lightEffect([330,50],2,500,[.2,.5,.15],sadMan)
lightEffect([300,50],1,1000,[.2,.5,.15],sadMan)
lightEffect([315,50],1,500,[.2,.5,.15],sadMan)

makeRect(40,3,[0,.2,0],[440,400],sadMan)
lightEffect([450,400],4,5000,[.2,.5,.1],sadMan)
lightEffect([420,400],3,2500,[.2,.5,.1],sadMan)
lightEffect([400,400],2,1000,[.2,.5,.1],sadMan)


makeRect(40,2,[0,.2,0],[250,420],sadMan)
lightEffect([260,420],4,7000,[.2,.5,.2],sadMan)
lightEffect([240,420],3,300,[.2,.5,.2],sadMan)
lightEffect([220,420],1,1000,[.2,.5,.2],sadMan)



lightEffect([470,300],3,1000,[.9,.64,.55],sadMan)
lightEffect([470,313],2,500,[.9,.64,.55],sadMan)
lightEffect([470,326],1,100,[.9,.64,.55],sadMan)
lightEffect([470,287],2,500,[.9,.64,.55],sadMan)
lightEffect([470,274],1,100,[.9,.64,.55],sadMan)
lightEffect([455,300],3,1000,[.9,.64,.55],sadMan)
lightEffect([455,310],2,500,[.9,.64,.55],sadMan)
lightEffect([455,320],1,100,[.9,.64,.55],sadMan)
lightEffect([455,290],2,500,[.9,.64,.55],sadMan)
lightEffect([455,280],1,100,[.9,.64,.55],sadMan)
lightEffect([440,305],2,100,[.9,.64,.55],sadMan)
lightEffect([440,300],2,100,[.9,.64,.55],sadMan)
lightEffect([440,295],2,100,[.9,.64,.55],sadMan)


makeRect(60,5,[0,.2,0],[325,470],sadMan)
makeRect(3,30,[0,.2,0],[345,470],sadMan)
makeRect(2,25,[0,.2,0],[325,470],sadMan)
makeRect(2,15,[0,.2,0],[305,470],sadMan)
makeRect(1,10,[0,.2,0],[285,470],sadMan)


lightEffect([345,470],8,1000,[0,.4,0],sadMan)
lightEffect([345,450],8,1000,[0,.4,0],sadMan)
lightEffect([345,490],8,1000,[0,.4,0],sadMan)
lightEffect([325,470],8,1000,[0,.4,0],sadMan)
lightEffect([325,460],5,500,[0,.4,0],sadMan)
lightEffect([325,480],5,500,[0,.4,0],sadMan)
lightEffect([305,470],8,1000,[0,.4,0],sadMan)
lightEffect([285,470],8,1000,[0,.4,0],sadMan)
lightEffect([265,470],3,1000,[0,.4,0],sadMan)


makeRect(40,3,[0,.2,0],[425,200],sadMan)
lightEffect([430,200],6,5000,[0,.7,0],sadMan)
lightEffect([410,200],4,600,[0,.7,0],sadMan)

lightEffect([395,200],6,1000,[0,.7,0],sadMan)
lightEffect([410,200],4,100,[0,.7,0],sadMan)

makeRect(40,3,[0,.2,0],[410,480],sadMan)
lightEffect([420,480],4,5000,[.2,.5,.3],sadMan)
lightEffect([390,480],3,2500,[.2,.5,.3],sadMan)
lightEffect([360,480],2,1000,[.2,.5,.3],sadMan)

# Tree Section ^^

# Black Crow VVV



# Black Crow ^^^



plt.imshow(sadMan, interpolation='nearest')
plt.show()