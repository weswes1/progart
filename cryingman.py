
import numpy as np
from matplotlib import pyplot as plt
from artTools import *

cryingMan = np.zeros((500,500,3))

for i in range(0,500):
	for j in range(0,500):
		d = ((0-i)**2+(500-j)**2)**.5
		cryingMan[i,j]=[1-(d/707),1-(d/707),1-(d/707)]


makeRect(80,80,[.5, 0,0],[150,150],cryingMan)

for i in range(0,10):
	makeRect(50,50,[.8, 0.76-i/10.0, 0.54],[150+2*i,150+2*i],cryingMan)
	makeRect(45,45,[0,0,.5],[150+2*i,150+2*i],cryingMan)


makeCircle(90,[128,136],[1,1,.8],cryingMan)





makeCircle(90,[200,340],[.7,0,.7],cryingMan)
equaliteralTriange(90,[320,340],[.7,0,.7],cryingMan)
makeCircle(80,[200,340],[1,1,.8],cryingMan)
equaliteralTriange(80,[320,340],[1,1,.8],cryingMan)


makeCircle(20,[180,350],[0,0,0],cryingMan)
makeCircle(15,[180,360],[1,1,.8],cryingMan)


makeCircle(15,[150,305],[0,0,0],cryingMan)
makeCircle(10,[150,315],[1,1,.8],cryingMan)

makeCircle(15,[176,320],[0,0,0],cryingMan)
makeCircle(10,[176,315],[1,1,.8],cryingMan)

makeCircle(15,[187,381],[0,0,0],cryingMan)

makeCircle(10,[180,381],[1,1,.8],cryingMan)


for i in range(0,10):
	makeRect(50,50,[.8, 0.76-i/10.0, 0.54],[150-2*i,150-2*i],cryingMan)
	makeRect(45,45,[0,0,.5],[150+2*i,150+2*i],cryingMan)

for i in range(0,10):
	makeRect(50,50,[.8, 0.76-i/10.0, 0.54],[150-2*i,150-2*i],cryingMan)
	makeRect(45,45,[0,0,.5],[150-2*i,150-2*i],cryingMan)


for i in range(90,180):
	for j in range(87,176):
		cryingMan[i,j]=[i/180.0,j/176.0,i*2.0/i*3.0]

makeCircle(10,[250,211],[.8,.8,1],cryingMan)


makeEllipse(100,200,[400,211],[.1,.05,.5],cryingMan)


for k in range(0,10):
	for i in range(0,5):
		makeCircle(10,[400+8*i,100+20*k],[i/5.0,0,0],cryingMan)
		makeCircle(10,[400-8*i,100+20*k],[i/5.0,0,0],cryingMan)
		makeCircle(10,[400,100+8*i+20*k],[0,0,i/5.0],cryingMan)
		makeCircle(10,[400,100-8*i+20*k],[0,0,i/5.0],cryingMan)

for i in range(0,5):
	for j in range(0,50):
		cryingMan[335+j,360+i]=[.6,.4,0]
		cryingMan[350+j,280+i]=[.6,.4,0]
		cryingMan[380+j,300+i]=[.6,.4,0]
		cryingMan[380+j,396+i]=[.6,.4,0]


for j in range(0,100):
	count = 0
	for i in range(0,50):
		if i%2==0:
			count+=1
		cryingMan[330+i,275+count+j]=[.1,.4,.5]

for k in range(0,433):
	cryingMan[300,k]=[0,0,0]

for k in range(0,300):
	cryingMan[300-k,433]=[0,0,0]

for i in range(0,5):
	for j in range(0,100):
		cryingMan[250+j,300+i]=[.6,.4,0]
		cryingMan[250+j,100+i]=[.6,.4,0]
		cryingMan[350+j,150+i]=[.6,.4,0]
		cryingMan[350+j,345+i]=[.6,.4,0]


equaliteralTriange(28,[400,235],[1,.5,.2],cryingMan)
equaliteralTriange(28,[370,235],[1,.5,.2],cryingMan)

for j in range(0,15):
	acr=0;
	for i in range(0,80):
		if i%4==0:
			acr+=1;
		cryingMan[390-i+acr+j,250+i]=[0,0,1];


for j in range(0,15):
	acr=0;
	for i in range(0,80):
		if i%2==0:
			acr+=1;
		cryingMan[360-i+acr+j,250+i]=[0,0,1];



for j in range(0,150):
	count = 0
	for i in range(0,75):
		if i%2==0:
			count+=1
		cryingMan[250+i,100+count+j]=[0,.5,.2]


for cc in range(0,20):
	for i in range(0,80):
		cryingMan[320-i+cc,320+cc]=[.4,.7,.8]



makeEllipse(19,15,[230,332],[.824,.706,.549],cryingMan)
makeEllipse(3,3,[226,324],[0,0,0],cryingMan)
makeEllipse(3,3,[226,337],[0,0,0],cryingMan)
makeEllipse(3,3,[240,330],[0,0,0],cryingMan)


for cc in range(0,40):
	for i in range(0,70):
		cryingMan[335-i+cc,360+cc]=[.3,.3,.1]




for j in range(0,200):
	count = 0
	for i in range(0,100):
		if i%2==0:
			count+=1
		cryingMan[250+i,100+count+j]=[.3,.1,0]

lightEffect([215,331],2,1000,[0,0,0],cryingMan)
lightEffect([215,322],2,500,[0,0,0],cryingMan)
lightEffect([215,340],2,500,[0,0,0],cryingMan)

for i in range(0,55):
	cryingMan[i,470]=[0,0,0]


for j in range(0,15):
	acr=0;
	for i in range(0,40):
		if i%4==0:
			acr+=1;
		cryingMan[280-i+acr+j,280+i]=[0,0,1];


for j in range(0,15):
	acr=0;
	for i in range(0,40):
		if i%2==0:
			acr+=1;
		cryingMan[300-i+acr+j,300+i]=[0,0,1];



lightEffect([75,470],50,100000,[0,1,0],cryingMan)
makeEllipse(20,30,[295,250],[.8,0,.2],cryingMan)
makeEllipse(15,25,[295,250],[.8,.7,1],cryingMan)

makeEllipse(20,10,[50,470],[0,1,0],cryingMan)

ac = 0;
for j in range(0,200):
	if j%3==0:
		ac+=1
	cryingMan[499-j,499-ac]=[0,0,0]

makeEllipse(20,8,[280,185],[.5,0,.5],cryingMan)
makeRect(10,3,[.5,0,.5],[265,185],cryingMan)
makeRect(8,8,[.5,0,.5],[295,185],cryingMan)

equaliteralTriange(25,[270,200],[.8,.8,1],cryingMan)
makeCircle(10,[250,211],[.8,.8,1],cryingMan)
makeCircle(7,[250,211],[.7,0,.7],cryingMan)

makeEllipse(7,10,[296,250],[.824,.706,.549],cryingMan)
makeEllipse(8,6,[296,250],[0,0,0],cryingMan)
makeEllipse(4,5,[296,250],[.8,0,0],cryingMan)

makeEllipse(7,7,[287,280],[.824,.706,.549],cryingMan)
makeEllipse(7,7,[305,300],[.824,.706,.549],cryingMan)

makeCircle(7,[128,136],[.7,0,.7],cryingMan)
equaliteralTriange(30,[150,123],[.7,0,.7],cryingMan)
makeCircle(4,[128,136],[1,1,.8],cryingMan)
equaliteralTriange(20,[148,127],[1,1,.8],cryingMan)


makeCircle(4,[128,110],[.7,0,.7],cryingMan)
equaliteralTriange(20,[150,98],[.7,0,.7],cryingMan)
makeCircle(2,[128,110],[1,1,.8],cryingMan)
equaliteralTriange(10,[148,100],[1,1,.8],cryingMan)



makeRect(8,8,[.5,0,.5],[295,185],cryingMan)
makeRect(50,50,[.4,.1,.2],[57,300],cryingMan)
makeRect(45,45,[1,1,1],[57,300],cryingMan)

makeCircle(18,[60,133],[0,0,0],cryingMan)
makeCircle(18,[60,150],[1,1,.8],cryingMan)
makeCircle(18,[60,116],[1,1,.8],cryingMan)

makeCircle(2,[128,110],[1,1,.8],cryingMan)



for l in range(0,10):
	for i in range(0,10-l):
		if i%2==0:
			makeCircle(8,[12+5*i+9*l,280+5*i],[1,l/10.0,1],cryingMan)
		else:
			makeCircle(8,[12+5*i+9*l,280+5*i],[1-l/10.0,1-l/10.0,1-l/10.0],cryingMan)


averagemask(0,0,499,cryingMan,factor=1.0/9.0,t=3)


plt.imshow(cryingMan, interpolation='nearest')
plt.show()

