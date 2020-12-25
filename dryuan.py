import numpy as np
from matplotlib import pyplot as plt
from PIL import Image 
from numpy import asarray
from artToolsUpdated import *
dryuan = np.zeros((500,500,3))

def roomdetails():
	for i in range(0,500):
		for j in range(0,500):
			dryuan[i,j] = [(1000-i)/1000,0,(1000-i)/1000]

	for i in range(0,75):
		for j in range(75):
			dryuan[200+i,400+j] = [0,0,0]

	for i in range(0,70):
		for j in range(70):
			dryuan[200+i,400+j] = [.9,.9,.9]
	dryuan[230,450] = [.5,0,0]
	dryuan[230,425] = [.5,0,0]

	for i in range(0,5):
		makeEllipse(25-5*i,10-2*i,[230,425],[.85**i,0,0],dryuan);
		makeEllipse(25-5*i,10-2*i,[230,450],[.85**i,0,0],dryuan);
		makeCircle(int(7-7*i/5.0),[230,438],[.85**i,0,0],dryuan);
def face():
	makeEllipse(75,50,[250,250],[241/256, 194/256, 125/256],dryuan)
	makeEllipse(75,50,[250,250],[241/256, 194/256, 125/256],dryuan)
	makeEllipse(75,50,[250,250],[241/256, 194/256, 125/256],dryuan)
	makeEllipse(10,20,[235,230],[201/256, 154/256, 85/256],dryuan)
	makeEllipse(10,20,[235,270],[201/256, 154/256, 85/256],dryuan)
	makeEllipse(10,39,[235,250],[241/256, 194/256, 125/256],dryuan)
	makeEllipse(5,10,[235,270],[201/256, 154/256, 85/256],dryuan)
	makeEllipse(5,10,[235,230],[201/256, 154/256, 85/256],dryuan)
	makeCircle(5,[235,230],[1,1,1],dryuan)
	makeCircle(5,[235,270],[1,1,1],dryuan)
	makeCircle(3,[235,230],[.2,.1,0],dryuan)
	makeCircle(3,[235,270],[.2,.1,0],dryuan)
	for i in range(0,10):
		dryuan[250-i,232+i]=[201/256, 154/256, 85/256]
		dryuan[250-i,267-i]=[201/256, 154/256, 85/256]
	for i in range(0,8):
		dryuan[248-i,232+i]=[201/256, 154/256, 85/256]
		dryuan[248-i,267-i]=[201/256, 154/256, 85/256]
	for i in range(0,15):
		makeCircle(10-i,[260,250],[(241/256)*(15-i)/15, (194/256)*(15-i)/15, (125/256)*(15-i)/15],dryuan)
	for i in range(0,15):
		makeCircle(8-i,[250,250],[(241/256)*(15-i)/15, (194/256)*(15-i)/15, (125/256)*(15-i)/15],dryuan)
	illuminate(202,211,[0,0,0],1,1000,dryuan)
	illuminate(202,291,[0,0,0],1,1000,dryuan)
	illuminate(202,220,[0,0,0],1,1000,dryuan)
	illuminate(202,277,[0,0,0],1,1000,dryuan)
	illuminate(190,220,[0,0,0],1,1000,dryuan)
	illuminate(190,277,[0,0,0],1,1000,dryuan)
	illuminate(190,225,[0,0,0],1,1000,dryuan)
	illuminate(190,272,[0,0,0],1,1000,dryuan)
	makeEllipse(7,14,[280,250],[0,0,0],dryuan)
	makeEllipse(7,14,[285,250],[241/256, 194/256, 125/256],dryuan)
def clothes():
	makeRect(40,20,[1,1,1],[365,248],dryuan)
	makeRect(80,60,[.75,.75,.75],[420,248],dryuan)
	makeCircle(25,[350,295],[1,1,1],dryuan)
	makeCircle(25,[350,205],[1,1,1],dryuan)
	makeRect(30,13,[.5,.5,.5],[400,205],dryuan)
	makeRect(30,13,[.5,.5,.5],[405,290],dryuan)

	for i in range(0,50):
		for j in range(0,26):
			dryuan[384+i,225+i+j] = [.3,.3,.3]

	for i in range(0,50):
		for j in range(0,26):
			dryuan[382+i,265-i-j] = [.3,.3,.3]

	makeCircle(15,[375,250],[0,0,0],dryuan)
	makeCircle(15,[375,242],[0,0,0],dryuan)

	for i in range(0,16):
		makeCircle(16-i,[375,246],[0,1,0],dryuan)
		if i%2==0:
			makeCircle(16-i,[375,246],[0,0,0],dryuan)


def scroll():
	makeRect(81,42,[0,0,0],[100,100],dryuan)
	makeRect(80,40,[200/256,142/256,100/256],[100,100],dryuan)

	for i in range(0,13):
		makeCircle(15,[28,62+5*i],[0,0,0],dryuan)
		makeCircle(14,[28,62+5*i],[200/256,142/256,100/256],dryuan)

	for i in range(0,13):
		if (i%2==0):
			makeCircle(15-i,[28,128],[0,0,0],dryuan)
		else:
			makeCircle(15-i,[28,128],[200/256,142/256,100/256],dryuan)

	makeRect(10,16,[0,0,0],[57,100],dryuan)
	makeRect(8,14,[200/256,142/256,100/256],[57,100],dryuan)

	for i in range(0,2):
		for j in range(0,32):
			dryuan[48+j,100-i]=[0,0,0]

	for i in range(0,2):
		for j in range(0,30):
			dryuan[56+i,113-j]=[0,0,0]


	makeCircle(13,[101,100],[0,0,0],dryuan)
	makeCircle(13,[101,120],[0,0,0],dryuan)

	makeCircle(13,[98,124],[200/256,142/256,100/256],dryuan)
	makeCircle(13,[98,96],[200/256,142/256,100/256],dryuan)

	makeCircle(4,[90,110],[200/256,142/256,100/256],dryuan)
	makeCircle(4,[113,110],[200/256,142/256,100/256],dryuan)

	for i in range(0,3):
		for j in range(0,25):
			dryuan[100+i,99+j]=[0,0,0]

	for i in range(0,2):
		for j in range(0,20):
			dryuan[95+j,89-i]=[0,0,0]

	for i in range(0,3):
		for j in range(0,3):
			dryuan[96+j+i,81+j+i]=[0,0,0]

	for i in range(0,6):
		dryuan[106,82+i]=[0,0,0]


	makeCircle(10,[150,75],[0,0,0],dryuan)
	makeCircle(10,[149,73],[200/256,142/256,100/256],dryuan)

	for j in range(0,2):
		for i in range(0,8):
			dryuan[143-j,82+i]=[0,0,0]

	for j in range(0,2):
		for i in range(0,8):
			dryuan[148-j,82+i]=[0,0,0]

	for j in range(0,2):
		for i in range(0,8):
			dryuan[153-j,82+i]=[0,0,0]

	for j in range(0,2):
		for i in range(0,16):
			dryuan[143+i,90-j]=[0,0,0]




	makeRect(3,6,[0,0,0],[148,100],dryuan)
	makeRect(2,4,[200/256,142/256,100/256],[148,100],dryuan)

	for i in range(0,2):
		for j in range(0,5):
			dryuan[149-j,99+i]=[0,0,0]


	for i in range(0,6):
		for j in range(0,2):
			dryuan[140+i+j,100-i]=[0,0,0]

	for i in range(0,2):
		for j in range(0,9):
			dryuan[156+j,100+i]=[0,0,0]


	for i in range(0,6):
		dryuan[158+i,101+i]=[0,0,0]
		
	for j in range(0,2):
		for i in range(0,3):
			dryuan[159+j,95+i]=[0,0,0]

	for i in range(0,4):
		dryuan[163-i,95+i]=[0,0,0]

	for j in range(0,2):
		for i in range(0,5):
			dryuan[159+j,101+i]=[0,0,0]

	makeRect(3,3,[1,1,1],[239,230],dryuan)

	makeRect(3,3,[1,1,1],[238,273],dryuan)


roomdetails()
face()
clothes()
scroll()

plt.imshow(dryuan, interpolation='nearest')
plt.show()