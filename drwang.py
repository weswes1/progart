import numpy as np
from matplotlib import pyplot as plt
from PIL import Image 
from numpy import asarray
from artToolsUpdated import *

drwang = np.zeros((500,500,3))

def roomdetails():
	step = 0;

	for i in range(0,500):
		for j in range(0,500):
			drwang[i,j]= [1,i/250,1]

	for i in range(0,75):
		if (i%3==0):
			step += 1;
		drwang[300+i,250-step] = [0,0,0];
		drwang[225+i,175-step] = [0,0,0];
		drwang[300+i,325+step] = [0,0,0];

	for i in range(0,3):
		for j in range(0,75):
			drwang[300+i-j,250-j] = [0,0,0]

	for i in range(0,3):
		for j in range(0,75):
			drwang[300+i-j,325-j] = [0,0,0]

	for i in range(0,3):
		for j in range(0,75):
			drwang[300+i,250+j] = [0,0,0]
			drwang[225+i,176+j] = [0,0,0]


	makeEllipse(16,41,[345,150],[0,0,0],drwang)
	makeEllipse(15,40,[345,150],[192/256,192/256,192/256],drwang)
	makeEllipse(16,41,[335,150],[0,0,0],drwang)
	makeEllipse(15,40,[335,150],[192/256,192/256,192/256],drwang)
	makeRect(50,5,[192/256,192/256,192/256],[275,151],drwang)
	makeEllipse(4,6,[335,150],[0,0,0],drwang)
	makeEllipse(3,5,[335,150],[192/256,192/256,192/256],drwang)
	makeEllipse(4,6,[330,150],[0,0,0],drwang)
	makeEllipse(3,5,[330,150],[192/256,192/256,192/256],drwang)

	for i in range(0,100):
		for j in range(0,2):
			drwang[327-i,155+j] = [0,0,0]
			drwang[327-i,145+j] = [0,0,0]

	makeEllipse(6,4,[227,148],[0,0,0],drwang)
	makeEllipse(5,3,[227,148],[192/256,192/256,192/256],drwang)
	makeEllipse(6,4,[227,151],[0,0,0],drwang)
	makeEllipse(5,3,[227,153],[192/256,192/256,192/256],drwang)
	makeCircle(20,[190,200],[0,0,0],drwang)
	makeCircle(18,[190,200],[192/256,192/256,192/256],drwang)
	makeEllipse(20,20,[205,210],[1,.83,1],drwang)

	for i in range(0,50):
		for j in range(0,2):
			drwang[221-i,146+i+j] = [0,0,0]
			drwang[221-i,147+i+j] = [192/256,192/256,192/256]
			drwang[221-i,148+i+j] = [192/256,192/256,192/256]
			drwang[221-i,149+i+j] = [192/256,192/256,192/256]
			drwang[221-i,150+i+j] = [192/256,192/256,192/256]
			drwang[221-i,151+i+j] = [0,0,0]
def faceandhead():
	makeRect(25,20,[180/256, 210/256, 140/256],[475,440],drwang)
	makeEllipse(15,60,[485,440],[0.275, 0.312, 63.707],drwang)

	makeRect(7,59,[0.2, 0.25, 40],[493,441],drwang)

	makeEllipse(60,45,[403,440],[100/256, 130/256, 60/256],drwang)
	makeEllipse(60,45,[400,440],[180/256, 210/256, 140/256],drwang)
	makeCircle(8,[380,455],[0,0,0],drwang)
	makeCircle(8,[380,453],[180/256, 210/256, 140/256],drwang)
	makeCircle(4,[380,455],[0,0,0],drwang)
	makeCircle(4,[378,455],[180/256, 210/256, 140/256],drwang)
	makeCircle(8,[380,425],[0,0,0],drwang)
	makeCircle(8,[380,427],[180/256, 210/256, 140/256],drwang)
	makeCircle(4,[380,425],[0,0,0],drwang)
	makeCircle(4,[378,425],[180/256, 210/256, 140/256],drwang)
	makeCircle(8,[400,440],[0,0,0],drwang)
	makeCircle(11,[400,434],[180/256, 210/256, 140/256],drwang)
	for i in range(0,8):
		drwang[383+i,430-i]=[80/256, 110/256, 40/256]
		drwang[383+i,450+i]=[80/256, 110/256, 40/256]
	for i in range(0,4):
		drwang[386+i,428-i]=[40/256, 60/256, 20/256]
		drwang[386+i,452+i]=[40/256, 60/256, 20/256]
	makeEllipse(6,13,[420,440],[0,0,0],drwang)
	drwang[414,440]=[180/256, 210/256, 140/256]
	makeCircle(20,[350,440],[0,0,0],drwang)
	makeCircle(20,[350,443],[0.275, 0.312, 63.707],drwang)
	makeCircle(10,[370,398],[0,0,0],drwang)
	makeCircle(10,[370,400],[0.275, 0.312, 63.707],drwang)
	makeCircle(10,[370,480],[0,0,0],drwang)
	makeCircle(10,[370,482],[0.275, 0.312, 63.707],drwang)
	makeCircle(15,[357,415],[0.275, 0.312, 63.707],drwang)
	makeCircle(15,[357,465],[0.275, 0.312, 63.707],drwang)
	makeRect(15,20,[1,1,1],[420,440],drwang)				# Mask
	makeRect(13,18,[.75,.75,.75],[420,440],drwang)			# Mask
	makeRect(10,15,[.85,.85,.85],[420,440],drwang)			# Mask
	makeRect(7,12,[.95,.95,.95],[420,440],drwang)			# Mask
	makeRect(6,11,[1,1,1],[420,440],drwang)					# Mask
	scaler = 0;
	for i in range(0,25):
		for k in range(0,2):
			drwang[405+k-i,420-k-i]=[1,1,1]
			drwang[405+k-i,460-k+i]=[1,1,1]
	for i in range(0,50):
		for k in range(0,2):
			if (i%4==0):
				scaler+=1;
			drwang[433+k-i,423-k-scaler]=[1,1,1]
			drwang[433+k-i,458-k+scaler]=[1,1,1]



	# 0.275, 0.312, 63.707

def computer():
	makeCircle(38,[250,400],[0,0,0],drwang)
	makeCircle(38,[244,400],[1,1,1],drwang)
	makeCircle(38,[242,400],[.25,.25,.25],drwang)
	makeRect(10,50,[.5,.5,.5],[205,450],drwang)
	makeRect(30,40,[0,0,0],[200,400],drwang)
	makeRect(29,39,[.5,.5,.5],[200,400],drwang)
	makeRect(30,40,[.25,.25,.25],[205,405],drwang)
	makeRect(29,39,[.25,.25,.25],[205,405],drwang)
	makeRect(28,38,[0,0,0],[205,405],drwang)
	makeCircle(8,[190,380],[0,1,0],drwang)
	makeCircle(6,[190,380],[0,0,0],drwang)
	makeCircle(8,[203,380],[0,1,0],drwang)
	makeCircle(6,[203,380],[0,0,0],drwang)
	makeCircle(12,[198,400],[0,1,0],drwang)
	makeCircle(10,[198,400],[0,0,0],drwang)
	equaliteralTriange(30,[227,410],[0,1,0],drwang)
	equaliteralTriange(30,[230,410],[0,0,0],drwang)
	equaliteralTriange(30,[227,380],[0,1,0],drwang)
	equaliteralTriange(30,[230,380],[0,0,0],drwang)

	for j in range(0,7):
		for i in range(0,10):
			makeRect(2,2,[0,0,0],[225+6*j,375+6*i],drwang)
def thyroid():
	atim = 0;

	for l in range(0,5):
		for j in range(0,5):
			drwang[284-l,275-l-j] = [1,0,0]
	for l in range(0,25):
		for j in range(0,25):
			drwang[282-l,282-l-j] = [180/256, 210/256, 140/256]
	for i in range(0,27):
		for j in range(0,6):
			drwang[230+i+j,215+i] = [180/256, 210/256, 140/256]
			drwang[230+i+j,230+i] = [180/256, 210/256, 140/256]
	makeCircle(9,[293,275],[0,0,0],drwang)
	makeCircle(7,[291,274],[180/256, 210/256, 140/256],drwang)
	makeRect(13,2,[180/256, 210/256, 140/256],[268,280],drwang)

	for i in range(0,15):
		for j in range(0,5):
			drwang[280-i,251-2*i+j]=[180/256, 210/256, 140/256]
			drwang[280-i,253-2*i+j]=[180/256, 210/256, 140/256]





roomdetails()
faceandhead()
computer()
thyroid()

plt.imshow(drwang, interpolation='nearest')
plt.show()