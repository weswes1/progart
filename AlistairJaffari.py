
import numpy as np
import math
import random
from matplotlib import pyplot as plt
from artTools import *

AllistairJaffari = np.zeros((500,500,3))

for i in range(0,500):
	for j in range(0,500):
		d = ((0-i)**2+(500-j)**2)**.5
		AllistairJaffari[j,i]=[.5,.5,1-j/500.0]




# generate coordinates of the trees
for j in range(0,200):
	xi = random.uniform(0,1)*200
	xi = int(xi)
	yi = random.uniform(0,1)*499
	yi = int(yi)
	for k in range(0,30):
		AllistairJaffari[499-xi-k,yi]=[0,.1,0]
		if k==29:
			lightEffect([499-xi-k,yi],4,500,[0,.4,0],AllistairJaffari)
			lightEffect([515-xi-k,yi],2,500,[0,.4,0],AllistairJaffari)


makeRect(20,20,[0,.2,0],[460,100],AllistairJaffari)

makeCircle(30,[274,133],[0,.2,0],AllistairJaffari)
makeCircle(25,[232,153],[0,.2,0],AllistairJaffari)
makeCircle(20,[200,180],[0,.2,0],AllistairJaffari)
makeCircle(15,[200,200],[0,.2,0],AllistairJaffari)
makeCircle(10,[180,210],[0,.2,0],AllistairJaffari)
makeCircle(8,[170,220],[0,.2,0],AllistairJaffari)
makeCircle(7,[160,230],[0,.2,0],AllistairJaffari)


for i in range(0,8):
	makeCircle(50-i*15,[409-100*i,100+int(math.pow(4*i,2))],[0,.2,0],AllistairJaffari)
	makeCircle(50-i*15,[450-100*i,80+int(math.pow(4*i,2))],[0,.2,0],AllistairJaffari)
	makeCircle(45-i*15,[409-100*i,100+int(math.pow(4*i,2))],[0,.3,0],AllistairJaffari)
	makeCircle(45-i*15,[450-100*i,80+int(math.pow(4*i,2))],[0,.3,0],AllistairJaffari)

lightEffect([450,80],20,10000,[0,.2,0],AllistairJaffari)
lightEffect([370,100],20,10000,[0,.2,0],AllistairJaffari)
lightEffect([276,133],15,10000,[0,.2,0],AllistairJaffari)
lightEffect([225,158],10,5000,[0,.2,0],AllistairJaffari)




for j in range(0,3):
	for i in range(0,25):
		AllistairJaffari[430-int(math.pow(100*i,.5))-j,i+130]=[0,.8,0]
		AllistairJaffari[430-i-j,int(math.pow(100*i,.5))+130]=[0,.8,0]
		AllistairJaffari[357+int(math.pow(100*i,.5))+j,200-i]=[0,.8,0]
		AllistairJaffari[357+i+j,200-int(math.pow(100*i,.5))]=[0,.8,0]

for j in range(0,3):
	for i in range(0,40):
		AllistairJaffari[480-int(math.pow(100*i,.5))-j,i+80]=[0,.8,0]
		AllistairJaffari[480-i-j,int(math.pow(100*i,.5))+80]=[0,.8,0]
		AllistairJaffari[407+int(math.pow(100*i,.5))+j,150-i]=[0,.8,0]
		AllistairJaffari[407+i+j,150-int(math.pow(100*i,.5))]=[0,.8,0]



for j in range(0,3):
	for i in range(0,10):
		AllistairJaffari[380-int(math.pow(100*i,.5))-j,i+130]=[0,.8,0]
		AllistairJaffari[380-i-j,int(math.pow(100*i,.5))+130]=[0,.8,0]
		AllistairJaffari[330+int(math.pow(100*i,.5))+j,175-i]=[0,.8,0]
		AllistairJaffari[330+i+j,175-int(math.pow(100*i,.5))]=[0,.8,0]



for k in range(0,10):
	for j in range(0,5):
		for i in range(0,25):
			AllistairJaffari[i+400+k,int(math.pow(100*i,.5))-j+k]=[0,.8,0]
			AllistairJaffari[int(math.pow(100*i,.5))-j+405+k,i+k]=[0,.8,0]



for k in range(0,5):
	for j in range(0,2):
		for i in range(0,25):
			AllistairJaffari[i+250+k,int(math.pow(100*i,.5))-j+k+60]=[0,.8,0]
			AllistairJaffari[int(math.pow(100*i,.5))-j+250+k,i+k+60]=[0,.8,0]

for k in range(0,8):
	for j in range(0,2):
		for i in range(0,25):
			AllistairJaffari[i+300+k,int(math.pow(100*i,.5))-j+k+40]=[0,.8,0]
			AllistairJaffari[int(math.pow(100*i,.5))-j+300+k,i+k+40]=[0,.8,0]



for j in range(0,7):
	for i in range(0,8):
		AllistairJaffari[270-j-int(math.pow(i,2)),200+i]=[0,.8,0]
		AllistairJaffari[270-j-int(math.pow(i,2)),200-i]=[0,.8,0]
		AllistairJaffari[130-j+int(math.pow(i,2)),180+i]=[0,.8,0]
		AllistairJaffari[130-j+int(math.pow(i,2)),180-i]=[0,.8,0]

for j in range(0,5):
	for i in range(0,20):
		AllistairJaffari[i+340,int(math.pow(100*i,.5))-j+30]=[0,.8,0]
		AllistairJaffari[int(math.pow(100*i,.5))-j+350,i+30]=[0,.8,0]


for j in range(0,5):
	for i in range(0,15):
		AllistairJaffari[i+240,int(math.pow(100*i,.5))-j+90]=[0,.8,0]
		AllistairJaffari[int(math.pow(100*i,.5))-j+240,i+90]=[0,.8,0]
		AllistairJaffari[int(math.pow(100*i,.5))-j+230,i+180]=[0,.8,0]


lightEffect([440,37],10,5000,[0,.6,0],AllistairJaffari)
lightEffect([366,68],10,5000,[0,.6,0],AllistairJaffari)
lightEffect([280,106],10,5000,[0,.6,0],AllistairJaffari)
lightEffect([219,134],10,5000,[0,.6,0],AllistairJaffari)
lightEffect([485,125],10,5000,[0,.6,0],AllistairJaffari)
lightEffect([485,55],10,5000,[0,.6,0],AllistairJaffari)
lightEffect([485,55],10,5000,[0,.6,0],AllistairJaffari)

lightEffect([283,158],10,5000,[0,.6,0],AllistairJaffari)
lightEffect([368,127],10,5000,[0,.6,0],AllistairJaffari)
makeCircle(40,[100,400],[.9,.95,.94],AllistairJaffari)
lightEffect([100,400],10,8000,[.9,.95,.94],AllistairJaffari)


averagemask(0,0,499,AllistairJaffari,factor=1.0/9.0,t=2)


plt.imshow(AllistairJaffari, interpolation='nearest')
plt.show()
