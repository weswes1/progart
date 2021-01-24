import numpy as np
from matplotlib import pyplot as plt
from PIL import Image 
from numpy import asarray
from artToolsUpdated import *
jioandjed = np.zeros((500,500,3))
for i in range(0,500):
	for j in range(0,500):
		jioandjed[i,j]=[1,1,1]
for k in range(0,350):
	count = 0;
	for i in range(0,300):
		if (i%2==0):
			count+=1;
		jioandjed[499-i,count+k]=[.6,1,.6]
for k in range(0,200):
	count = 0;
	for i in range(0,300):
		if (i%2==0):
			count+=1;
		jioandjed[499-i-k,count]=[173/256,216/256,230/256]
makeRect(150,150,[.6,1,.6],[350,350],jioandjed);
makeRect(100,250,[173/256,216/256,230/256],[100,75],jioandjed);
makeRect(50,50,[173/256,216/256,230/256],[250,50],jioandjed);
def tvTable():
	azup=0;
	az=0;

	for i in range(0,15):
		if (i%2==0):
			azup+=1;
		jioandjed[200+i,200+azup]=[.81,.62,0.44];

	for j in range(0,93):
		azup=0;
		for i in range(0,15):
			if (i%2==0):
				azup+=1;
			jioandjed[200+i,201+azup+j]=[.81,.62,0.44];

	for j in range(0,93):
		for i in range(0,2):
			jioandjed[214+i,209+j]=[.81,.62,0.44];

	for j in range(0,93):
		for i in range(0,2):
			jioandjed[214+i,209+j]=[.81,.62,0.44];
			jioandjed[245+i,209+j]=[.81,.62,0.44];

	for i in range(0,95):
		for j in range(0,2):
			jioandjed[200+j,200+i]=[.81,.62,0.44];

	for j in range(0,30):
		for i in range(0,2):
			jioandjed[200+j,200+i] = [.81,.62,0.44];

	for j in range(0,30):
		for i in range(0,2):
			jioandjed[215+j,210+i] = [.81,.62,0.44];

	for k in range(0,45):
		for j in range(0,30):
			for i in range(0,2):
				jioandjed[215+j,300+i-2*k] = [.81,.62,0.44];

	for l in range(0,40):
		for k in range(0,10):
			jioandjed[238+k-l,200+k]=[.81,.62,0.44];


def giovanni():
	makeEllipse(30,7,[350,191],[0,0,.5],jioandjed);
	makeEllipse(30,7,[350,209],[0,0,.5],jioandjed);
	makeEllipse(40,20,[300,200],[0,0,.5],jioandjed);
	makeCircle(5,[280,190],[0,1,0],jioandjed);
	makeCircle(3,[280,190],[0,0,.5],jioandjed);
	makeRect(7,5,[0,1,0],[281,201],jioandjed)
	makeRect(3,3,[0,0,.5],[280,201],jioandjed)
	makeRect(3,3,[0,0,.5],[287,204],jioandjed)

	for i in range(0,3):
		jioandjed[284+i,203+i] = [0,1,0];
		jioandjed[284+i,204+i] = [0,1,0];
		jioandjed[284+i,205+i] = [0,1,0];
		jioandjed[284+i,206+i] = [0,1,0];

	makeCircle(5,[280,211],[0,1,0],jioandjed);
	makeCircle(3,[280,213],[0,0,.5],jioandjed);
	makeRect(6,4,[0,1,0],[295,190],jioandjed);
	makeCircle(3,[298,190],[0,0,.5],jioandjed);
	makeCircle(3,[290,190],[0,0,.5],jioandjed);
	makeRect(6,4,[0,1,0],[295,202],jioandjed);
	makeRect(2,2,[0,0,0.5],[292,204],jioandjed);
	makeRect(2,2,[0,0,0.5],[298,204],jioandjed);
	makeCircle(4,[292,212],[0,1,0],jioandjed);
	makeCircle(3,[292,214],[0,0,.5],jioandjed);
	makeCircle(4,[297,212],[0,1,0],jioandjed);
	makeCircle(3,[297,210],[0,0,.5],jioandjed);
	makeRect(6,6,[0,1,0],[309,193],jioandjed);
	makeRect(4,4,[0,0,.5],[311,197],jioandjed);
	makeRect(4,4,[0,0,.5],[311,185],jioandjed);
	makeRect(7,5,[0,1,0],[310,205],jioandjed)
	makeRect(3,3,[0,0,.5],[309,205],jioandjed)
	makeRect(3,3,[0,0,.5],[316,208],jioandjed)

	for i in range(0,3):
		jioandjed[313+i,207+i] = [0,1,0];
		jioandjed[313+i,208+i] = [0,1,0];
		jioandjed[313+i,209+i] = [0,1,0];
		jioandjed[313+i,210+i] = [0,1,0];


	makeRect(7,5,[0,1,0],[326,202],jioandjed)
	makeRect(3,3,[0,0,.5],[324,202],jioandjed)
	makeRect(3,3,[0,0,.5],[333,202],jioandjed)

	makeEllipse(8,5,[254,200],[198/256,134/256,66/256],jioandjed);
	makeEllipse(16,10,[245,200],[198/256,134/256,66/256],jioandjed);

	illuminate(230,200,[0,0,0],1,100,jioandjed)
	illuminate(235,200,[0,0,0],1,100,jioandjed)
	illuminate(235,195,[0,0,0],1,100,jioandjed)
	illuminate(235,205,[0,0,0],1,100,jioandjed)

	makeEllipse(3,4,[243,195],[1,1,1],jioandjed);
	makeEllipse(3,4,[243,205],[1,1,1],jioandjed);

	makeEllipse(2,2,[243,195],[0,0,0],jioandjed);
	makeEllipse(2,2,[243,205],[0,0,0],jioandjed);

	makeEllipse(3,6,[253,200],[1,0,0],jioandjed);
	makeEllipse(4,5,[250,200],[198/256,134/256,66/256],jioandjed);

	for i in range(0,8):
		for j in range(0,30):
			jioandjed[267+i,155+j]=[198/256,134/256,66/256];
			jioandjed[267+i,215+j]=[198/256,134/256,66/256];

	for i in range(0,8):
		for j in range(0,50):
			jioandjed[271-j,165-i]=[198/256,134/256,66/256];
			jioandjed[271-j,240-i]=[198/256,134/256,66/256];


	makeRect(3,70,[192/256,192/256,192/256],[225,200],jioandjed);
	makeCircle(25,[225,270],[0,0,0],jioandjed);
	makeCircle(25,[225,128],[0,0,0],jioandjed);

	makeCircle(10,[265,175],[198/256,134/256,66/256],jioandjed);
	makeCircle(10,[265,223],[198/256,134/256,66/256],jioandjed);


	makeRect(10,3,[1,1,1],[225,257],jioandjed);
	makeCircle(9,[225,270],[1,1,1],jioandjed);
	makeCircle(6,[225,270],[0,0,0],jioandjed);


	makeCircle(9,[225,140],[1,1,1],jioandjed);
	makeCircle(6,[225,140],[0,0,0],jioandjed);

	makeCircle(9,[225,125],[1,1,1],jioandjed);
	makeCircle(6,[225,125],[0,0,0],jioandjed);

	makeCircle(9,[225,283],[1,1,1],jioandjed);
	makeCircle(6,[225,283],[0,0,0],jioandjed);

	makeRect(10,3,[1,1,1],[225,110],jioandjed);

	makeCircle(8,[245,165],[198/256,134/256,66/256],jioandjed);
	makeCircle(8,[245,233],[198/256,134/256,66/256],jioandjed);
	makeCircle(4,[225,161],[198/256,134/256,66/256],jioandjed);
	makeCircle(4,[225,236],[198/256,134/256,66/256],jioandjed);
def TV():
	makeEllipse(5,10,[205,250],[0,0,0],jioandjed)
	makeRect(10,5,[0,0,0],[193,250],jioandjed)
	makeRect(20,40,[0,0,0],[175,250],jioandjed)
	makeRect(18,38,[1,0,0],[175,250],jioandjed)

	for i in range(0,11):
		if (i%2==0):
			makeCircle(11-i,[175,225+5*i],[1,1,1],jioandjed)
		else:
			makeCircle(11-i,[175,225+5*i],[0,1,0],jioandjed)
def table():
	for k in range(0,250):
		for i in range(0,50):
			jioandjed[375+i,100+i+k]=[.81,.62,0.44];
			makeRect(15,5,[.81,.62,0.44],[435,390],jioandjed)
			makeRect(15,5,[.81,.62,0.44],[435,150],jioandjed)
			makeRect(15,5,[.81,.62,0.44],[391,105],jioandjed)
def tableStuff():
	makeRect(2,10,[0,1,0],[400,230],jioandjed)
	makeRect(2,10,[0,1,0],[398,231],jioandjed)
	makeRect(10,2,[0,1,0],[400,235],jioandjed)
	makeRect(10,2,[0,1,0],[398,233],jioandjed)
	makeRect(10,2,[0,1,0],[395,228],jioandjed)
	makeRect(10,2,[0,1,0],[392,228],jioandjed)
	makeRect(2,10,[0,1,0],[392,228],jioandjed)
def coasters():
	makeCircle(10,[400,250],[.61,.5,0.3],jioandjed)
	makeCircle(3,[400,255],[0,0,0],jioandjed)
	makeCircle(3,[400,245],[0,0,0],jioandjed)
	makeCircle(3,[405,250],[0,0,0],jioandjed)
	makeCircle(3,[395,250],[0,0,0],jioandjed)
	makeCircle(2,[400,255],[.61,.5,0.3],jioandjed)
	makeCircle(2,[400,245],[.61,.5,0.3],jioandjed)
	makeCircle(2,[405,250],[.61,.5,0.3],jioandjed)
	makeCircle(2,[395,250],[.61,.5,0.3],jioandjed)
	makeCircle(1,[400,255],[0,0,0],jioandjed)
	makeCircle(1,[400,245],[0,0,0],jioandjed)
	makeCircle(1,[405,250],[0,0,0],jioandjed)
	makeCircle(1,[395,250],[0,0,0],jioandjed)
	makeCircle(10,[400,265],[.61,.5,0.3],jioandjed)
	makeCircle(3,[400,270],[0,0,0],jioandjed)
	makeCircle(3,[400,260],[0,0,0],jioandjed)
	makeCircle(3,[405,265],[0,0,0],jioandjed)
	makeCircle(3,[395,265],[0,0,0],jioandjed)
	makeCircle(2,[400,270],[.61,.5,0.3],jioandjed)
	makeCircle(2,[400,260],[.61,.5,0.3],jioandjed)
	makeCircle(2,[405,265],[.61,.5,0.3],jioandjed)
	makeCircle(2,[395,265],[.61,.5,0.3],jioandjed)
	makeCircle(1,[400,275],[0,0,0],jioandjed)
	makeCircle(1,[400,260],[0,0,0],jioandjed)
	makeCircle(1,[405,265],[0,0,0],jioandjed)
	makeCircle(1,[395,265],[0,0,0],jioandjed)
def coffeeCup():
	makeCircle(6,[405,167],[0,0,1],jioandjed);
	makeCircle(4,[405,167],[.81,.62,0.44],jioandjed);

	for i in range(0,8):
		if (i%2==0):
			makeCircle(8,[407-i,177],[0,0,1],jioandjed);
		else:
			makeCircle(8,[407-i,177],[0,0,.5],jioandjed);

	makeCircle(6,[400,177],[.435,.306,.216],jioandjed);
def laTrains():
	makeRect(40,60,[0,0,0],[90,205],jioandjed);
	makeRect(38,58,[1,1,1],[90,205],jioandjed);
	makeRect(2,30,[0,1,0],[95,200],jioandjed);
	makeRect(2,30,[0,1,0],[95,205],jioandjed);
	makeRect(30,2,[0,1,0],[95,205],jioandjed);
	makeRect(25,2,[1,0,0],[95,220],jioandjed);
	makeRect(25,2,[1,0,0],[95,180],jioandjed);
	makeRect(2,25,[1,0,1],[105,200],jioandjed);
	makeRect(2,25,[1,0,1],[115,175],jioandjed);

	for i in range(0,60):
		for j in range(0,3):
			jioandjed[120-i+j,210-i]=[1,1,0];

	for i in range(0,60):
		for j in range(0,3):
			jioandjed[60+i+j,230-i]=[0,1,1];

	for i in range(0,60):
		for j in range(0,3):
			jioandjed[120-i+j,200+i]=[0,.5,1];
def outlines():


	for k in range(0,200):
		jioandjed[k,145]=[0,0,0];
		jioandjed[k,146]=[0,0,0];

	
	for i in range(0,20):
		makeCircle(25,[465-i,26],[0,0,0],jioandjed);
		makeCircle(25,[465-i,475],[0,0,0],jioandjed);

	makeRect(24,350,[0,0,0],[476,105],jioandjed);



	for i in range(0,60):
		for j in range(0,5):
			jioandjed[60-i,415+i-j]=[0,0,0];
			jioandjed[60-i,470-i-j]=[0,0,0];

	for i in range(0,80):
		for j in range(0,5):
			jioandjed[30+j,400+i]=[0,0,0];
def tabletwo():
	for k in range(0,100):
		for i in range(0,50):
			jioandjed[175+i,350+i+k]=[.71,.5,0.40];

	makeRect(20,5,[.71,.5,0.40],[245,405],jioandjed);
	makeRect(20,5,[.71,.5,0.40],[245,490],jioandjed);
	makeRect(20,5,[.71,.5,0.40],[198,355],jioandjed);
	makeRect(10,5,[1,0,0],[180,425],jioandjed);
	makeRect(5,3,[1,0,0],[170,425],jioandjed);
	makeRect(3,2,[1,0,0],[165,425],jioandjed);
	makeCircle(12,[205,435],[.9,.9,.9],jioandjed);
	makeCircle(12,[194,400],[0,1,0],jioandjed);
	makeCircle(12,[186,400],[.71,.5,0.40],jioandjed);
	makeCircle(4,[204,435],[1,0,1],jioandjed);

	for k in range(0,5):
		for i in range(0,5):
			if (i%2==0):
				makeRect(25-5*i-5*k,25-5*i-5*k,[1-i/5,0,k/5],[150+5*i,385+5*i],jioandjed);
			else:
				makeRect(25-5*i-5*k,25-5*i-5*k,[k/5,1-i/5,k/5],[150+5*i,385+5*i],jioandjed);
def jed():
	makeEllipse(20,15,[315,453],[1,205/256,148/256],jioandjed);
	makeEllipse(80,40,[400,453],[.2,0,.5],jioandjed);
	makeEllipse(40,35,[275,450],[255/256,205/256,148/256],jioandjed);

	for i in range(0,15):
		makeCircle(10,[340+5*i,420-5*i],[0,1,0],jioandjed);

	makeCircle(10,[340,480],[0,1,0],jioandjed);
	makeCircle(10,[345,485],[0,1,0],jioandjed);
	makeCircle(10,[350,490],[0,1,0],jioandjed);

	for i in range(0,5):
		makeEllipse(10-2*i,15-3*i,[260,440],[(255-50*i)/256,(205-41*i)/256,(148-33*i)/256],jioandjed);
		makeEllipse(10-2*i,15-3*i,[260,465],[(255-50*i)/256,(205-41*i)/256,(148-33*i)/256],jioandjed);

	makeEllipse(5,14,[295,453],[.75,0,0],jioandjed);
	makeEllipse(4,13,[293,453],[255/256,205/256,148/256],jioandjed);
	makeCircle(4,[260,440],[1,1,1],jioandjed);
	makeCircle(4,[260,465],[1,1,1],jioandjed);
	makeCircle(3,[260,440],[150/256,75/256,0],jioandjed);
	makeCircle(3,[260,465],[150/256,75/256,0],jioandjed);
	makeCircle(2,[260,440],[0,0,0],jioandjed);
	makeCircle(2,[260,465],[0,0,0],jioandjed);

	for i in range(0,10):
		for j in range(0,3):
			jioandjed[255-i-j,475-i]=[150/256,75/256,0];
			jioandjed[248+j,435+i]=[150/256,75/256,0];

	for i in range(0,5):
		makeRect(8-2*i,8-2*i,[(255-50*i)/256,(205-41*i)/256,(148-33*i)/256],[285-5*i,453],jioandjed);

	illuminate(235,450,[150/256,75/256,0],1,500,jioandjed);
	illuminate(250,470,[150/256,75/256,0],1,500,jioandjed);
	illuminate(240,450,[150/256,75/256,0],1,500,jioandjed);
	illuminate(240,430,[150/256,75/256,0],1,500,jioandjed);
	illuminate(245,460,[150/256,75/256,0],1,500,jioandjed);
	illuminate(245,440,[150/256,75/256,0],1,500,jioandjed);
	
	makeCircle(20,[380,450],[0,1,0],jioandjed);
	makeEllipse(25,5,[405,450],[.2,0,.5],jioandjed);
	makeEllipse(25,5,[395,467],[.2,0,.5],jioandjed);
	makeEllipse(25,5,[395,433],[.2,0,.5],jioandjed);
	makeRect(5,20,[.2,0,.5],[362,450],jioandjed);
	makeRect(40,30,[1,1,1],[400,325],jioandjed);
	makeCircle(7,[375,432],[0,1,0],jioandjed);

	for i in range(0,5):
		makeCircle(5,[379+5*i,434],[.2,0,.5],jioandjed);

	makeCircle(5,[387,437],[.2,0,.5],jioandjed);
	makeCircle(10,[395,465],[0,1,0],jioandjed);
	makeCircle(7,[392,465],[.2,0,.5],jioandjed);
	makeCircle(7,[385,465],[.2,0,.5],jioandjed);
	makeCircle(7,[378,465],[.2,0,.5],jioandjed);
	makeCircle(7,[378,438],[.2,0,.5],jioandjed);
	makeEllipse(13,7,[380,322],[1,1,1],jioandjed);
	makeEllipse(10,15,[380,322],[0,0,0],jioandjed);
	makeEllipse(10,15,[382,322],[1,1,1],jioandjed);
	makeCircle(5,[375,340],[0,0,0],jioandjed);
	makeCircle(5,[373,340],[1,1,1],jioandjed);
	makeCircle(5,[375,308],[0,0,0],jioandjed);
	makeCircle(5,[373,308],[1,1,1],jioandjed);
	makeEllipse(3,6,[397,350],[1,205/256,148/256],jioandjed);


	makeCircle(5,[390,318],[0,0,0],jioandjed);
	makeCircle(3,[390,318],[1,1,1],jioandjed);
	makeRect(6,2,[0,0,0],[390,308],jioandjed);
	makeCircle(5,[390,328],[0,0,0],jioandjed);
	makeCircle(3,[390,328],[1,1,1],jioandjed);
	makeRect(6,2,[0,0,0],[400,330],jioandjed);
	makeCircle(3,[405,328],[0,0,0],jioandjed);
	makeCircle(8,[390,343],[0,0,0],jioandjed);
	makeEllipse(8,4,[390,343],[1,1,1],jioandjed);
	makeRect(5,1,[0,0,0],[390,343],jioandjed);

	for i in range(0,15):
		if (i%2==0):
			makeCircle(15-i,[425-i,330],[0,0,0],jioandjed);
		if (i%2==1):
			makeCircle(15-i,[425-i,330],[1,1,1],jioandjed);

	makeRect(20,40,[0,0,0],[473,455],jioandjed);



def outsiderocks():
	des=0;
	for i in range(0,200):
		if (i%2==0):
			des+=1;
		for k in range(0,10):
			jioandjed[450-i-k,des+30]=[.75,.75,.75];


	for j in range(0,5):
		des=0;
		for i in range(0,195):
			if (i%2==0):
				des+=1;
			for k in range(0,10):
				jioandjed[440-i-k-j*10,des+30]=[.5,.5,.5];
	des=0;
	for i in range(0,100):
		if (i%3==0):
			des+=1;
		for k in range(0,10):
			jioandjed[100-des-k,30+i]=[.75,.75,.75];

	for z in range(0,5):
		des=0;
		for i in range(0,100):
			if (i%3==0):
				des+=1;
			for k in range(0,10):
				jioandjed[110-des-k+10*z,30+i]=[100/256,149/256,237/256];

	makeRect(175,5,[.75,.75,.75],[275,30],jioandjed);
	makeRect(90,5,[.75,.75,.75],[150,125],jioandjed);
	makeRect(20,30,[.5,.5,.5],[260,65],jioandjed);
	makeRect(20,30,[.5,.5,.5],[280,65],jioandjed);
	makeRect(20,30,[.5,.5,.5],[300,65],jioandjed);
	makeRect(30,10,[.5,.5,.5],[340,45],jioandjed);
	makeRect(30,10,[.5,.5,.5],[350,45],jioandjed);
	makeRect(30,10,[.5,.5,.5],[340,55],jioandjed);


	for i in range(0,5):
		equaliteralTriange(20,[150-10*i,35+15*i],[139/256,69/256,19/256],jioandjed);
		makeRect(40,10,[139/256,69/256,19/256],[190-10*i,45+15*i],jioandjed);
	makeRect(40,10,[139/256,69/256,19/256],[150,110],jioandjed);
	makeCircle(25,[250,90],[.5,.5,.5],jioandjed);


	makeEllipse(50,25,[207,85],[.13,.54,.13],jioandjed);

	makeEllipse(25,12,[175,60],[139/256,69/256,19/256],jioandjed);
	makeEllipse(25,12,[175,110],[139/256,69/256,19/256],jioandjed);
	makeEllipse(20,5,[160,85],[139/256,69/256,19/256],jioandjed);


	illuminate(220,90,[0,1,0],10,500,jioandjed);
	illuminate(220,90,[.13,.54,.13],5,500,jioandjed);
	illuminate(230,40,[.13,.54,.13],2,500,jioandjed);
	illuminate(230,50,[.13,.54,.13],2,500,jioandjed);
	illuminate(230,60,[.13,.54,.13],2,500,jioandjed);


	illuminate(100,40,[1,1,1],2,500,jioandjed);
	illuminate(110,60,[1,1,1],2,500,jioandjed);
	illuminate(120,55,[1,1,1],2,500,jioandjed);
	illuminate(110,50,[1,1,1],2,500,jioandjed);
	illuminate(120,70,[1,1,1],2,500,jioandjed);

	for k in range(0,10):
		for i in range(0,20):
			makeCircle(5,[int(250+random.uniform(0,10)*(-1)**i),int(45+random.uniform(0,20))+6*k],[random.uniform(0,10),random.uniform(0,1),random.uniform(0,1)],jioandjed);
			makeCircle(5,[int(250+random.uniform(0,10)*(-1)**i),int(45+random.uniform(0,20))+6*k],[random.uniform(0,10),random.uniform(0,1),random.uniform(0,1)],jioandjed);
			makeCircle(5,[int(250+random.uniform(0,10)*(-1)**i)+12*k,int(40+random.uniform(0,20))],[random.uniform(0,10),random.uniform(0,1),random.uniform(0,1)],jioandjed);
			makeCircle(5,[int(250+random.uniform(0,10)*(-1)**i)+12*k,int(40+random.uniform(0,20))],[random.uniform(0,10),random.uniform(0,1),random.uniform(0,1)],jioandjed);

	makeCircle(8,[185,85],[139/256,69/256,19/256],jioandjed);
	illuminate(185,85,[1,0,0],5,5000,jioandjed);
	illuminate(35,445,[0,1,0],10,5000,jioandjed);



outsiderocks();
outlines();
TV();
tvTable();
giovanni();
table();
tableStuff();
coffeeCup();
laTrains();
jed();
tabletwo();
coasters();


makeCircle(16,[254,340],[0,0,0],jioandjed);
makeCircle(16,[254,336],[.6,1,.6],jioandjed);


makeCircle(16,[223,342],[0,0,0],jioandjed);
makeCircle(16,[223,346],[.6,1,.6],jioandjed);

makeRect(6,1,[0,0,0],[202,342],jioandjed);
makeRect(3,4,[1,1,1],[196,342],jioandjed);
makeRect(3,4,[1,1,1],[196,342],jioandjed);


makeEllipse(30,20,[320,352],[0,0,0],jioandjed);
makeEllipse(30,20,[320,348],[.6,1,.6],jioandjed);

makeEllipse(10,7,[350,350],[0,0,0],jioandjed);
makeEllipse(6,10,[350,340],[.6,1,.6],jioandjed);


makeCircle(8,[35,450],[0,1,0],jioandjed);
makeCircle(8,[35,440],[0,1,0],jioandjed);
makeCircle(8,[28,445],[0,1,0],jioandjed);

makeRect(3,10,[.75,.75,.75],[300,270],jioandjed);
makeCircle(8,[300,260],[.75,.75,.75],jioandjed);
makeCircle(8,[300,280],[.75,.75,.75],jioandjed);

makeRect(3,10,[.75,.75,.75],[320,260],jioandjed);
makeCircle(8,[320,270],[.75,.75,.75],jioandjed);
makeCircle(8,[320,250],[.75,.75,.75],jioandjed);


makeRect(10,20,[0,0,0],[280,350],jioandjed);
makeCircle(4,[280,340],[0,1,0],jioandjed);
makeCircle(4,[280,350],[1,0,0],jioandjed);
makeCircle(4,[280,360],[0,0,1],jioandjed);
makeRect(1,20,[0,1,0],[276,350],jioandjed);

makeRect(3,50,[0,0,0],[225,200],jioandjed);






plt.imshow(jioandjed, interpolation='nearest')
plt.show()