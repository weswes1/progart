
import numpy as np
from matplotlib import pyplot as plt
from artTools import *
import random


pirates = np.zeros((500,500,3))

for i in range(0,500):
	for j in range(0,500):
		pirates[i,j]=[.5,.5,1]


for i in range(0,12):
	for j in range(0,50):
		pirates[j+190,280-j-i]=[.39,.26,.12]






for i in range (0,120):
	if random.random() <=.5:
		makeCircle(40,[250+int(210*random.random()),250+int(210*random.random())],[.4,.4,.9],pirates)
		makeCircle(40,[250-int(210*random.random()),250+int(210*random.random())],[.4,.4,.9],pirates)
		makeCircle(40,[250-int(210*random.random()),250-int(210*random.random())],[.4,.4,.9],pirates)
		makeCircle(40,[250+int(210*random.random()),250-int(210*random.random())],[.4,.4,.9],pirates)
	else:
		makeCircle(40,[250+int(210*random.random()),250+int(210*random.random())],[.5,.5,1],pirates)
		makeCircle(40,[250-int(210*random.random()),250+int(210*random.random())],[.5,.5,1],pirates)
		makeCircle(40,[250+int(210*random.random()),250-int(210*random.random())],[.5,.5,1],pirates)
		makeCircle(40,[250-int(210*random.random()),250-int(210*random.random())],[.5,.5,1],pirates)


makeEllipse(50,100,[250,150],[.39,.26,.12],pirates)
makeEllipse(50,100,[230,150],[5,.34,.2],pirates)

makeEllipse(50,100,[200,150],[.5,.5,1],pirates)
makeEllipse(10,50,[300,150],[.5,.5,1],pirates)

lightEffect([250,250],1000,10000,[1,1,1],pirates)
lightEffect([250,250],1000,100000,[.4,.4,.9],pirates)



makeRect(24,7,[.39,.26,.12],[230,150],pirates)
makeRect(22,4,[.39,.26,.12],[220,210],pirates)
makeRect(22,4,[.39,.26,.12],[220,90],pirates)
equaliteralTriange(150,[205,80],[.94,.86,.51],pirates)
equaliteralTriange(75,[215,60],[.80,.76,.4],pirates)
equaliteralTriange(75,[215,180],[.80,.76,.4],pirates)
makeEllipse(8,50,[230,150],[.7,.7,.5],pirates)
equaliteralTriange(30,[197,258],[.80,.76,.4],pirates)
makeEllipse(3,20,[220,207],[.80,.76,.6],pirates)
makeEllipse(3,20,[220,90],[.80,.76,.6],pirates)

for i in range(0,22):
	for j in range(0,8):
		pirates[200+i,260-i+j] = [.39,.26,.12]



for k in range(0,12):
	makeCircle(40,[250-20*k,458-22*k],[.4,.4,.9],pirates)
	makeCircle(40,[265-20*k,448-22*k],[.5,.5,1],pirates)

for k in range(0,12):
	lightEffect([230-20*k,478-22*k],1,100,[1,1,1],pirates)

for k in range(0,12):
	lightEffect([220-20*k,468-22*k],1,100,[1,1,1],pirates)


makeRect(15,20,[0,0,0],[115,136],pirates)
makeRect(11,1,[0,0,0],[120,155],pirates)

makeCircle(9,[110,135],[1,1,1],pirates)
makeCircle(2,[108,132],[0,0,0],pirates)
makeCircle(2,[108,138],[0,0,0],pirates)
makeCircle(4,[115,135],[0,0,0],pirates)

for i in range(0,8):
	pirates[120+i,139-i]=[1,1,1]
	pirates[126-i,136-i]=[1,1,1]



for count in range(0,100):
	for i in range(0,100-count):
		pirates[499-i,100-i-count]=[0,0,0]









plt.imshow(pirates, interpolation='nearest')
plt.show()
