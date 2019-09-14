
import numpy as np
from matplotlib import pyplot as plt
from artTools import *

Kimono = np.zeros((500,500,3))

for i in range(0,500):
	for j in range(0,500):
		Kimono[i,j]=[.95,.95,.8]





for l in range(0,220):
	aj=0
	for i in range(0,220-l):
		if i%5==0:
			aj+=1
			Kimono[250+i+l,154-aj]=[.6,.6,.9]


for l in range(0,150):
	aj=0
	for i in range(0,150-l):
		if i%5==0:
			aj+=1
			Kimono[310+i+l,150-aj]=[.8,.8,1]











for l in range(0,220):
	aj=0
	for i in range(0,220-l):
		if i%4==0:
			aj+=1
			Kimono[250+i+l,246+aj]=[.6,.6,.9]


for l in range(0,150):
	aj=0
	for i in range(0,150-l):
		if i%4==0:
			aj+=1
			Kimono[310+i+l,254+aj]=[.8,.8,1]



makeCircle(20,[160,225],[0,0,0],Kimono)
makeCircle(20,[160,175],[0,0,0],Kimono)

makeEllipse(20,10,[470,175],[1,1,1],Kimono)
makeEllipse(20,10,[470,223],[1,1,1],Kimono)

makeEllipse(100,50,[285,200],[.75,.75,1],Kimono)
makeRect(100,50,[.75,.75,1],[370,200],Kimono)

makeEllipse(90,40,[285,200],[.6,.6,.9],Kimono)
makeRect(90,40,[.6,.6,.9],[370,200],Kimono)

makeEllipse(50,25,[175,200],[1,1,1],Kimono)


for i in range(0,10):
	makeCircle(1,[480-i,175+i],[0,0,0],Kimono)
	makeCircle(1,[480-i,225+i],[0,0,0],Kimono)
	makeCircle(1,[480-i,175-i],[0,0,0],Kimono)
	makeCircle(1,[480-i,225-i],[0,0,0],Kimono)


makeCircle(13,[130,220],[0,0,0],Kimono)
makeCircle(25,[140,200],[0,0,1],Kimono)
makeCircle(25,[150,200],[0,0,0],Kimono)


makeCircle(6,[182,188],[0,0,0],Kimono)
makeCircle(6,[182,208],[0,0,0],Kimono)

makeCircle(6,[180,188],[1,1,1],Kimono)
makeCircle(6,[180,208],[1,1,1],Kimono)

makeEllipse(3,6,[210,200],[1,0,0],Kimono)

makeCircle(6,[180,188],[1,1,1],Kimono)
makeCircle(5,[198,200],[0,0,0],Kimono)
makeCircle(5,[198,202],[1,1,1],Kimono)


vars=0
for i in range(0,60):
	if i%3==0:
		vars+=1
	Kimono[130+vars,170+i]=[1,1,0]
	Kimono[134+vars,170+i]=[1,1,0]

makeRect(8,8,[0,0,0],[140,200],Kimono)
makeRect(25,25,[.6,.7,.9],[300,200],Kimono)
makeRect(20,20,[.5,.5,.9],[300,200],Kimono)


makeCircle(8,[298,197],[.95,.95,.8],Kimono)
makeCircle(8,[298,205],[.95,.95,.8],Kimono)



cars=0
for i in range(0,20):
	if i%2==0:
		cars+=1
	makeCircle(8,[290-3*i,195-3*cars],[.75,.75,1],Kimono)
	makeCircle(8,[235+3*i,239-3*cars],[.75,.75,1],Kimono)



for i in range(0,10):
	if i%2==0:
		makeEllipse(20-i,10-i,[438,218],[1-i/10.0,.647,0],Kimono)
	else:
		makeEllipse(10-i,20-i,[438,218],[1-i/10.0,0,0],Kimono)


for i in range(0,5):
	if i%2==0:
		makeEllipse(10-i,5-i,[438,189],[1-i/10.0,.647,0],Kimono)
	else:
		makeEllipse(5-i,10-i,[438,189],[1-i/10.0,0,0],Kimono)


for i in range(0,5):
	if i%2==0:
		makeEllipse(10-i,5-i,[407,218],[1-i/10.0,.647,0],Kimono)
	else:
		makeEllipse(5-i,10-i,[407,218],[1-i/10.0,0,0],Kimono)



for i in range(0,5):
	if i%2==0:
		makeEllipse(10-i,5-i,[420,200],[1-i/10.0,.647,0],Kimono)
	else:
		makeEllipse(5-i,10-i,[420,200],[1-i/10.0,0,0],Kimono)


for i in range(0,5):
	if i%2==0:
		makeEllipse(10-i,5-i,[390,230],[1-i/10.0,.647,0],Kimono)
	else:
		makeEllipse(5-i,10-i,[390,230],[1-i/10.0,0,0],Kimono)


for i in range(0,5):
	if i%2==0:
		makeEllipse(10-i,5-i,[447,170],[1-i/10.0,.647,0],Kimono)
	else:
		makeEllipse(5-i,10-i,[447,170],[1-i/10.0,0,0],Kimono)



for j in range(0,9):
	for i in range(0,3):
		if i%2==0:
			makeEllipse(6-i,3-i,[365+8*j,230-8*j],[1-i/10.0,.647,0],Kimono)
		else:
			makeEllipse(3-i,6-i,[365+8*j,230-8*j],[1-i/10.0,0,0],Kimono)


for i in range(0,10):
	if i%2==0:
		makeCircle(3,[345+8*i,235-8*i],[1,0,0],Kimono)
	else:
		makeCircle(3,[345+8*i,235-8*i],[1,.647,0],Kimono)

for i in range(0,10):
	if i%2==0:
		makeCircle(2,[338+8*i,235-8*i],[1,0,0],Kimono)
	else:
		makeCircle(2,[338+8*i,235-8*i],[1,.647,0],Kimono)

for i in range(0,10):
	if i%2==0:
		makeCircle(1,[334+8*i,235-8*i],[1,0,0],Kimono)
	else:
		makeCircle(1,[334+8*i,235-8*i],[1,.647,0],Kimono)


for i in range(0,10):
	if i%2==0:
		makeEllipse(20-i,10-i,[355,180],[0,0,1-i/10.0],Kimono)
	else:
		makeEllipse(10-i,20-i,[355,180],[1-i/10.0,0,0],Kimono)



for i in range(0,10):
	if i%2==0:
		makeEllipse(10-i,5-i,[345,208],[0,0,1-i/10.0],Kimono)
	else:
		makeEllipse(5-i,10-i,[345,208],[1-i/10.0,0,0],Kimono)


for i in range(0,10):
	if i%2==0:
		makeEllipse(10-i,5-i,[390,170],[0,0,1-i/10.0],Kimono)
	else:
		makeEllipse(5-i,10-i,[390,170],[1-i/10.0,0,0],Kimono)



plt.imshow(Kimono, interpolation='nearest')
plt.show()