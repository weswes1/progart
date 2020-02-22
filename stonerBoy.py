
import numpy as np
from matplotlib import pyplot as plt
import random
from artTools import *

stonerBoy = np.zeros((500,500,3))

for i in range(0,500):
	for j in range(0,500):
		stonerBoy[i,j]=[.26,.27,.29]


for i in range(0,500):
	for j in range(0,150):
		stonerBoy[j,i]=[.98,.38,.1]



makeCircle(90,[200,80],[.26,.27,.29],stonerBoy)
makeCircle(90,[220,120],[.26,.27,.29],stonerBoy)
makeCircle(90,[220,400],[.26,.27,.29],stonerBoy)
makeCircle(20,[150,480],[.26,.27,.29],stonerBoy)



for l in range(0,300):
	for j in range(0,300-2*l):
		stonerBoy[450-l,200+j+l]=[random.random()/1.5,random.random()/1.5,random.random()/1.5]



count = 100;
for k in range(0,200):
	if k%3==0:
		count-=5;
	for l in range(0,count):
		stonerBoy[200-k,200+l]=[random.random()/2.0,0,0]
 
count = 100;
for k in range(0,200):
	if k%3==0:
		count-=5;
	for l in range(0,count):
		stonerBoy[200-k,200-l]=[random.random()/2.0,0,0]
 


count = 100;
for k in range(0,200):
	if k%3==0:
		count-=2;
	for l in range(0,count):
		stonerBoy[400-k,100+l]=[count/200.0,count/200.0,count/200.0]
 
count = 100;
for k in range(0,200):
	if k%3==0:
		count-=2;
	for l in range(0,count):
		stonerBoy[400-k,100-l]=[(k/200.0)*.26,(k/200.0)*.27,(k/200.0)*.29]
 

makeCircle(40,[265,350],[0,0,0],stonerBoy)


count = 100;
for k in range(0,200):
	if k%3==0:
		count-=1;
	for l in range(0,count):
		stonerBoy[250-k,400+l]=[0,0,k/200.0]
 
count = 100;
for k in range(0,200):
	if k%3==0:
		count-=1;
	for l in range(0,count):
		stonerBoy[250-k,400-l]=[0,0,k/200.0]
 

makeEllipse(25,100,[250,400],[.26,.27,.29],stonerBoy)
makeCircle(45,[80,400],[.98,.38,.1],stonerBoy)
makeEllipse(25,100,[220,200],[.26,.27,.29],stonerBoy)
makeEllipse(25,100,[220,200],[.26,.27,.29],stonerBoy)
makeCircle(30,[350,300],[.26,.27,.29],stonerBoy)
makeCircle(30,[350,395],[.26,.27,.29],stonerBoy)
makeCircleFADETWO(50,[50,200],[0,0,0],stonerBoy)

lightEffect([50,200],5,10000,[1,1,1],stonerBoy)
lightEffect([50,200],5,10000,[0,0,0],stonerBoy)

for i in range(0,60):
	for j in range(0,50):
		stonerBoy[i+400,j+320]=[0,(math.fabs(math.sin(math.degrees(i/60.0)))),0]

lightEffect([0,500],50,100000,[0,0,0],stonerBoy)
lightEffect([0,0],50,100000,[0,0,0],stonerBoy)

for i in range(0,10):
	makeCircleFADE(30-3*i,[240-24*i,360+15*i],[1,0,0],stonerBoy)


count = 100;
for k in range(0,200):
	if k%3==0:
		count-=2;
	for l in range(0,count):
		stonerBoy[300-k,250-l]=[math.sin(k/200.0),0,0]

count = 100;
for k in range(0,200):
	if k%3==0:
		count-=2;
	for l in range(0,count):
		stonerBoy[325-k,275-l]=[0,math.sin(k/200.0),0]

count = 100;
for k in range(0,200):
	if k%3==0:
		count-=2;
	for l in range(0,count):
		stonerBoy[350-k,300-l]=[1,0,math.sin(k/200.0)]

for i in range(0,10):
	if i%2==0:
		makeCircleFADETWO(30-3*i,[250-25*i,50],[0,.50,0],stonerBoy)
	else:
		makeCircleFADE(30-3*i,[250-25*i,50],[0,.50,0],stonerBoy)


for i in range(0,20):
	makeCircleFADETWO(20-i,[475,350-15*i],[0,0,1],stonerBoy)

for i in range(0,20):
	makeCircleFADETWO(20-i,[50,450-15*i],[0,0,1],stonerBoy)


# Scales the entire figure
for i in range(0,500):
	for j in range(0,500):
		stonerBoy[i,j]=[stonerBoy[i,j][0]*i/250,stonerBoy[i,j][1]*i/250,stonerBoy[i,j][2]*i/250]
plt.imshow(stonerBoy, interpolation='nearest')
plt.show()