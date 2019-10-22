import numpy as np
from matplotlib import pyplot as plt
from artTools import *

afroChiller = np.zeros((500,500,3))

for i in range(0,500):
	for j in range(0,500):
		afroChiller[i,j]=[1,0,1-i/500.0]



makeCircle(30,[64,250],[0,1,0],afroChiller)
makeCircle(25,[64,250],[1,0,.9],afroChiller)


for i in range(0,8):
	makeCircle(10,[50+5*i,50+5*i],[0,1,0],afroChiller)
	makeCircle(10,[50+5*i,50-5*i],[0,1,0],afroChiller)
	makeCircle(5,[80,33+5*i],[0,1,0],afroChiller)
	makeCircle(10,[50+5*i,115],[0,1,0],afroChiller)
	makeCircle(8,[48,115+5*i],[0,1,0],afroChiller)
	makeCircle(8,[70,115+5*i],[0,1,0],afroChiller)
	makeCircle(8,[50+5*i,174],[0,1,0],afroChiller)
	makeCircle(5,[47,174+5*i],[0,1,0],afroChiller)
	makeCircle(5,[66,174+5*i],[0,1,0],afroChiller)
	makeCircle(5,[50+2*i,210],[0,1,0],afroChiller)
	makeCircle(5,[70+3*i,183+3*i],[0,1,0],afroChiller)

makeCircleFADE(100,[200,100],[0,0,1],afroChiller)


makeEllipse(23,12,[130,250],[.396,.263,.129],afroChiller)
makeEllipse(14,12,[130,250],[.396,.263,.129],afroChiller)


for i in range(0,20):
	makeCircle(10,[175+5*i,250-5*i],[.396,.263,.129],afroChiller)
	makeCircle(10,[175+5*i,250+5*i],[.396,.263,.129],afroChiller)



makeEllipse(23,12,[130,250],[.396,.263,.129],afroChiller)
makeCircle(25,[115,250],[.396,.263,.129],afroChiller)

makeEllipse(75,15,[375,270],[1,0,.5],afroChiller)
makeEllipse(75,15,[375,230],[1,0,.5],afroChiller)

makeEllipse(100,50,[250,250],[.5,0,.3],afroChiller)

makeEllipse(7,14,[460,230],[1,.3,.5],afroChiller)
makeEllipse(7,14,[460,270],[1,.3,.5],afroChiller)

makeEllipse(5,10,[470,230],[1,.3,.5],afroChiller)
makeEllipse(5,10,[470,270],[1,.3,.5],afroChiller)

makeEllipse(10,20,[450,230],[1,0,.5],afroChiller)
makeEllipse(10,20,[450,270],[1,0,.5],afroChiller)


makeCircle(50,[380,420],[1,0,.9],afroChiller)

makeCircle(25,[380,460],[1,0,.3],afroChiller)
makeCircle(25,[380,380],[1,0,.3],afroChiller)
makeCircle(3,[413,440],[0,0,0],afroChiller)
makeCircle(3,[405,440],[0,0,0],afroChiller)
makeCircle(3,[410,430],[0,0,0],afroChiller)
makeRect(100,12,[1,0,.9],[250,420],afroChiller)
makeRect(6,12,[1,0,0],[360,420],afroChiller)

makeRect(100,1,[1,.8,1],[250,417],afroChiller)
makeRect(100,1,[1,.8,1],[250,423],afroChiller)
makeRect(100,1,[1,.8,1],[250,411],afroChiller)
makeRect(100,1,[1,.8,1],[250,429],afroChiller)

makeCircle(25,[380,460],[1,0,.3],afroChiller)


makeCircle(4,[110,260],[.9,.9,.9],afroChiller)
makeCircle(4,[110,240],[.9,.9,.9],afroChiller)
makeCircle(4,[120,250],[.1,.5,.5],afroChiller)

makeCircle(2,[110,260],[0,0,0],afroChiller)
makeCircle(2,[110,240],[0,0,0],afroChiller)



equaliteralTriange(60,[150,393],[.5,.5,1],afroChiller)


lightEffect([85,250],1.5,10000,[0,0,0],afroChiller)
lightEffect([85,245],1.5,10000,[0,0,0],afroChiller)
lightEffect([85,255],1.5,10000,[0,0,0],afroChiller)
lightEffect([90,225],1.5,10000,[0,0,0],afroChiller)
lightEffect([90,265],1.5,10000,[0,0,0],afroChiller)
lightEffect([70,250],1.5,10000,[0,0,0],afroChiller)
lightEffect([70,240],1.5,10000,[0,0,0],afroChiller)
lightEffect([70,260],1.5,10000,[0,0,0],afroChiller)
lightEffect([73,220],1.5,10000,[0,0,0],afroChiller)
lightEffect([80,280],1.5,10000,[0,0,0],afroChiller)
lightEffect([90,280],1.5,10000,[0,0,0],afroChiller)
lightEffect([110,220],1.5,10000,[0,0,0],afroChiller)
lightEffect([110,280],1.5,10000,[0,0,0],afroChiller)
lightEffect([110,220],1.5,10000,[0,0,0],afroChiller)
lightEffect([100,290],1.5,10000,[0,0,0],afroChiller)
lightEffect([100,210],1.5,10000,[0,0,0],afroChiller)
lightEffect([102,276],1.5,10000,[0,0,0],afroChiller)
lightEffect([81,229],1.5,10000,[0,0,0],afroChiller)
lightEffect([102,223],1.5,10000,[0,0,0],afroChiller)
lightEffect([90,250],1.5,10000,[0,0,0],afroChiller)
lightEffect([90,255],1.5,10000,[0,0,0],afroChiller)
lightEffect([90,245],1.5,10000,[0,0,0],afroChiller)
lightEffect([100,265],1.5,10000,[0,0,0],afroChiller)
lightEffect([100,235],1.5,10000,[0,0,0],afroChiller)



makeCircle(25,[200,250],[0,.75,0],afroChiller)
makeCircle(20,[200,250],[0,0,1],afroChiller)



for i in range(0,13):
	makeCircle(5,[180+3*i,250],[0,.75,0],afroChiller)

for i in range(0,10):
	makeCircle(3,[195+2*i,250+2*i],[0,.75,0],afroChiller)
	makeCircle(3,[195+2*i,250-2*i],[0,.75,0],afroChiller)

for i in range(200,250):
	for j in range(200,250):
		afroChiller[i+50,j+25]=[0,i/250.0,0]

makeCircleFADETWO(25,[275,250],[0,0,1],afroChiller)
makeCircleFADETWO(20,[325,250],[0,1,0],afroChiller)
makeCircleFADE(10,[240,250],[1,0,0],afroChiller)

makeCircleFADE(10,[258,230],[1,0,0],afroChiller)
makeCircleFADE(10,[258,270],[1,0,0],afroChiller)

makeCircleFADE(10,[288,230],[1,0,0],afroChiller)
makeCircleFADE(10,[288,270],[1,0,0],afroChiller)


makeCircle(80,[400,100],[0,1,0],afroChiller)

makeCircle(40,[400,150],[1,0,.19],afroChiller)
makeCircle(40,[400,50],[1,0,.19],afroChiller)

for i in range(0,180):
	for j in range(0,40):
		afroChiller[330-i,83+j]=[0,i/120.0,0]

for k in range(0,3):
	for i in range(0,180):
		for j in range(0,6):
			afroChiller[330-i,86+k+6*j]=[1,1,1]

makeCircle(30,[140,100],[0,1,0],afroChiller)

for i in range(0,10):
	makeEllipse(50-5*i,25,[400,327],[.8,.9-i/11.0,.7],afroChiller)



plt.imshow(afroChiller, interpolation='nearest')
plt.show()