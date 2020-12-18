import numpy as np
from matplotlib import pyplot as plt
from PIL import Image 
from numpy import asarray
from artToolsUpdated import *

#[247/255,193/255,155/255]

### Background 
gandj = np.zeros((500,500,3))
for i in range(0,500):
	for j in range(0,500):
		gandj[i,j] = [(500-i)/500,(500-i)/500,(500-i)/500]




def facialFeatures():
	makeRect(6,1,[147/255,93/255,55/255],[252,374],gandj)
	makeRect(6,1,[147/255,93/255,55/255],[262,373],gandj)
	makeRect(4,1,[147/255,93/255,55/255],[272,372],gandj)
	makeCircle(5,[270,372],[147/255,93/255,55/255],gandj)
	makeCircle(5,[271,372],[247/255,193/255,155/255],gandj)

	makeEllipse(7,15,[284,372],[255/255,193/255,155/255],gandj)
	makeEllipse(7,15,[284,372],[255/255,93/255,55/255],gandj)
	makeEllipse(4,12,[284,372],[255/255,43/255,5/255],gandj)
	makeEllipse(2,6,[284,372],[255/255,40/255,3/255],gandj)
	makeEllipse(7,15,[290,372],[247/255,193/255,155/255],gandj)
	makeEllipse(7,15,[274,377],[247/255,193/255,155/255],gandj)
	makeEllipse(7,15,[274,367],[247/255,193/255,155/255],gandj)
	makeCircle(5,[249,390],[1,1,1],gandj)
	makeCircle(5,[249,355],[1,1,1],gandj)
	makeCircle(3,[249,390],[165/255,42/255,42/255],gandj)
	makeCircle(3,[249,355],[165/255,42/255,42/255],gandj)
	makeCircle(2,[249,390],[0,0,0],gandj)
	makeCircle(2,[249,355],[0,0,0],gandj)
def makeGlasses():
	makeRect(12,12,[0,0,0],[250,390],gandj);
	makeRect(10,10,[247/255,193/255,155/255],[250,390],gandj);
	makeRect(12,12,[0,0,0],[250,356],gandj);
	makeRect(10,10,[247/255,193/255,155/255],[250,356],gandj);
	makeRect(2,7,[0,0,0],[250,373],gandj);
	diagnol(239,335,10,3,[0,0,0],gandj);
	for i in range(0,3):
		for k in range(0,10):
			gandj[248-k,401+i+k]=[0,0,0]
def bodyandclothes():
	makeRect(49,49,[1,1,1],[451,375],gandj)
	makeEllipse(100,50,[390,375],[1,1,1],gandj)
	makeEllipse(130,28,[350,378],[.95,.95,.95],gandj)
	makeRect(8,16,[0,0,0],[350,372],gandj)
	makeRect(7,15,[1,1,1],[350,372],gandj)
	makeCircle(18,[350,335],[.9,.9,.9],gandj)
	makeCircle(18,[350,415],[.9,.9,.9],gandj)
	makeRect(80,15,[.9,.9,.9],[420,415],gandj)
	diagnol(330,340,100,37,[.9,.9,.9],gandj)
	makeEllipse(80,40,[250,375],[247/255,193/255,155/255],gandj)
	makeRect(21,15,[.5,.5,.5],[440,455],gandj)
	makeRect(18,13,[.5,.5,.5],[458,455],gandj)
	makeEllipse(10,16,[428,455],[0,0,1],gandj)
	makeEllipse(3,9,[440,447],[247/255,193/255,155/255],gandj)
	makeEllipse(3,9,[446,447],[247/255,193/255,155/255],gandj)
	makeEllipse(3,9,[452,447],[247/255,193/255,155/255],gandj)
	makeEllipse(3,9,[458,447],[247/255,193/255,155/255],gandj)

	for i in range(0,5):
		gandj[345+i,362]=[0,0,0]

	for i in range(0,3):
		gandj[347+i,362+i]=[0,0,0]
		gandj[347-i,362+i]=[0,0,0]

	for i in range(0,3):
		gandj[348-i,368+i]=[0,0,0]
		gandj[348-i,368-i]=[0,0,0]
		gandj[348-i,372+i]=[0,0,0]
		gandj[348-i,372-i]=[0,0,0]

	for i in range(0,4):
		gandj[346+i,378+i]=[0,0,0]
		gandj[346+i,378-i]=[0,0,0]

	for i in range(0,4):
		gandj[348,376]=[0,0,0]
def makeHair():
	makeCircle(32,[200,375],[0,0,0],gandj)
	for i in range(0,8):
		makeEllipse(20,2,[215,360+7*i],[0,0,0],gandj)

	for i in range(0,5):
		makeEllipse(20,2,[200,358+7*i],[0,0,0],gandj)

	for i in range(0,3):
		makeEllipse(20,2,[190,358+7*i],[0,0,0],gandj)
	#########

	for i in range(0,8):
		makeEllipse(20,2,[215,360+7*i],[0,0,0],gandj)

	for i in range(0,5):
		makeEllipse(20,2,[200,358+7*i],[0,0,0],gandj)

	for i in range(0,3):
		makeEllipse(20,2,[190,358+7*i],[0,0,0],gandj)




	for i in range(0,8):
		makeEllipse(20,2,[215,360+7*i],[0,0,0],gandj)

	for i in range(0,5):
		makeEllipse(20,2,[200,360+7*i],[0,0,0],gandj)

	for i in range(0,3):
		makeEllipse(20,2,[190,360+7*i],[0,0,0],gandj)

	for i in range(0,8):
		makeEllipse(20,3,[215,358+7*i],[0,0,0],gandj)

	for i in range(0,5):
		makeEllipse(20,3,[200,358+7*i],[0,0,0],gandj)

	for i in range(0,3):
		makeEllipse(20,3,[190,358+7*i],[0,0,0],gandj)





	#######
	for l in range(0,18):
		for k in range(0,2):
			for i in range(0,18-l):
				gandj[200+i+3*l,360-k-2*l]=[0,0,0]

	for l in range(0,16):
		for k in range(0,2):
			for i in range(0,14-l):
				gandj[190+i+3*l,360-k-2*l]=[0,0,0]

	for l in range(0,14):
		for k in range(0,2):
			for i in range(0,14-l):
				gandj[180+i+3*l,360-k-2*l]=[0,0,0]

	##### Hair Section 
def roomdetails():
	for i in range(0,3):
		for k in range(0,100):
			gandj[i+k+390,100-k] = [0,0,0]
	for k in range(0,3):
			for l in range(0,390):
				gandj[390-l,100+k] = [0,0,0]
				gandj[390-k,100+l] = [0,0,0]
	for k in range(0,200):
		for i in range(0,75):
			gandj[499-i,i+k] = [128/255,128/255,128/255];
	for k in range(0,5):
		makeCircle(15,[470-6*k,100],[192/255,192/255,192/255],gandj)
	makeCircle(15,[444,100],[128/255,128/255,128/255],gandj)
	makeCircle(8,[470,100],[0,0,0],gandj)
	makeCircle(7,[470,100],[192/255,192/255,192/255],gandj)
	makeCircle(6,[470,100],[0,0,0],gandj)
	makeCircle(5,[470,100],[0,1,0],gandj)
	makeCircle(4,[470,100],[192/255,192/255,192/255],gandj)
	makeCircle(3,[470,100],[1,0,0],gandj)
	makeCircle(2,[470,100],[192/255,192/255,192/255],gandj)
	makeCircle(50,[100,160],[0,0,0],gandj)
	makeCircle(48,[100,160],[.8,.8,.8],gandj)
	makeCircle(48,[100,160],[.8,.8,.8],gandj)
	makeCircle(8,[100,160],[0,0,0],gandj)
	makeCircle(6,[100,160],[.8,.8,.8],gandj)
	makeCircle(15,[73,160],[0,0,0],gandj)
	makeCircle(15,[108,134],[0,0,0],gandj)
	makeCircle(15,[118,181],[0,0,0],gandj)
	equaliteralTriange(40,[87,155],[.8,.8,.8],gandj)
	equaliteralTriange(40,[87,125],[.8,.8,.8],gandj)
	for k in range(0,17):
		for i in range(0,17):
			gandj[115+i+k,173+i-k]=[.8,.8,.8]
			gandj[110+i+k,168+i-k]=[.8,.8,.8]
			gandj[111+i+k,168+i-k]=[.8,.8,.8]
	equaliteralTriange(30,[110,165],[.8,.8,.8],gandj)
	equaliteralTriange(40,[87,125],[.8,.8,.8],gandj)


	for k in range(0,17):
		for i in range(0,17):
			gandj[107+i+k,153+i-k]=[.8,.8,.8]
			gandj[102+i+k,148+i-k]=[.8,.8,.8]
			gandj[103+i+k,148+i-k]=[.8,.8,.8]
			gandj[108+i+k,142+i-k]=[.8,.8,.8]




	equaliteralTriange(30,[100,120],[.8,.8,.8],gandj)


def radiology():



	for x in range(0,10):
		makeCircle(3,[100-4*x,225],[0,0,0],gandj)
		makeCircle(3,[80+2*x,225+2*x],[0,0,0],gandj)
	makeCircle(12,[70,233],[0,0,0],gandj)
	makeCircle(8,[70,233],[.8,.8,.8],gandj)

	makeCircle(12,[90,256],[0,0,0],gandj)
	makeCircle(8,[90,256],[.8,.8,.8],gandj)
	makeCircle(3,[98,268],[0,0,0],gandj)
	makeCircle(12,[90,286],[0,0,0],gandj)
	makeCircle(8,[90,286],[.8,.8,.8],gandj)
	makeCircle(3,[98,298],[0,0,0],gandj)
	for i in range(0,10):
		makeCircle(3,[98-3*i,298],[0,0,0],gandj)

	for i in range(0,5):
		makeCircle(3,[98-3*i,308],[0,0,0],gandj)

	makeCircle(3,[78,308],[0,0,0],gandj)

	makeCircle(12,[91,324],[0,0,0],gandj)
	makeCircle(8,[91,324],[.8,.8,.8],gandj)

	for i in range(0,10):
		makeCircle(3,[98-3*i,339],[0,0,0],gandj)

	makeCircle(12,[91,354],[0,0,0],gandj)
	makeCircle(8,[91,354],[.8,.8,.8],gandj)

	makeCircle(12,[91,377],[0,0,0],gandj)
	makeCircle(8,[91,377],[.8,.8,.8],gandj)

	for i in range(0,8):
		makeCircle(3,[96+3*i,387],[0,0,0],gandj)

	makeCircle(12,[120,377],[0,0,0],gandj)
	makeCircle(12,[115,375],[.8,.8,.8],gandj)

	for i in range(0,5):
		makeCircle(3,[98-3*i,408-3*i],[0,0,0],gandj)

	for i in range(0,10):
		makeCircle(3,[85+3*i,421-3*i],[0,0,0],gandj)



















radiology();
roomdetails();
bodyandclothes();
makeHair();
makeGlasses();
facialFeatures();






plt.imshow(gandj, interpolation='nearest')
plt.show()