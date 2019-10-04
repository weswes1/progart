import numpy as np
from matplotlib import pyplot as plt
from artTools import *

arabseque = np.zeros((500,500,3))

# Color the entire background white 

for i in range(0,500):
	for j in range(0,500):
		arabseque[i,j]=[1,1,1]

# Outer Ring
for i in range(0,9):
	makeCircle(25,[49+50*i,475],[0,0,0],arabseque)
	makeCircle(25,[49+50*i,25],[0,0,0],arabseque)
	makeCircle(25,[49+50*i,463],[1,1,1],arabseque)
	makeCircle(25,[49+50*i,37],[1,1,1],arabseque)
for i in range(0,9):
	makeCircle(25,[25,50+50*i],[0,0,0],arabseque)
	makeCircle(25,[475,50+50*i],[0,0,0],arabseque)
	makeCircle(25,[37,50+50*i],[1,1,1],arabseque)
	makeCircle(25,[463,50+50*i],[1,1,1],arabseque)


for i in range(0,8):
	makeCircle(12,[75+50*i,459],[0,0,0],arabseque)
	makeCircle(12,[75+50*i,40],[0,0,0],arabseque)
	makeCircle(12,[75+50*i,452],[1,1,1],arabseque)
	makeCircle(12,[75+50*i,46],[1,1,1],arabseque)
for i in range(0,8):
	makeCircle(12,[42,75+50*i],[0,0,0],arabseque)
	makeCircle(12,[458,75+50*i],[0,0,0],arabseque)
	makeCircle(12,[48,75+50*i],[1,1,1],arabseque)
	makeCircle(12,[452,75+50*i],[1,1,1],arabseque)


for i in range(0,7):
	makeCircle(6,[97+50*i,443],[0,0,0],arabseque)
	makeCircle(6,[97+50*i,60],[0,0,0],arabseque)
	makeCircle(6,[97+50*i,439],[1,1,1],arabseque)
	makeCircle(6,[97+50*i,64],[1,1,1],arabseque)

for i in range(0,7):
	makeCircle(6,[56,98+50*i],[0,0,0],arabseque)
	makeCircle(6,[436,98+50*i],[0,0,0],arabseque)
	makeCircle(6,[60,98+50*i],[1,1,1],arabseque)
	makeCircle(6,[432,98+50*i],[1,1,1],arabseque)



for i in range(0,7):
	makeCircle(3,[97+50*i,449],[0,0,0],arabseque)
	makeCircle(3,[97+50*i,66],[0,0,0],arabseque)
	makeCircle(3,[97+50*i,445],[1,1,1],arabseque)
	makeCircle(3,[97+50*i,70],[1,1,1],arabseque)

for i in range(0,7):
	makeCircle(3,[56,98+50*i],[0,0,0],arabseque)
	makeCircle(3,[436,98+50*i],[0,0,0],arabseque)
	makeCircle(3,[60,98+50*i],[1,1,1],arabseque)
	makeCircle(3,[432,98+50*i],[1,1,1],arabseque)




makeCircle(50,[262,250],[0,0,0],arabseque)
makeCircle(50,[238,250],[0,0,0],arabseque)
makeCircle(50,[250,262],[0,0,0],arabseque)
makeCircle(50,[250,238],[0,0,0],arabseque)
makeCircle(59,[250,250],[1,1,1],arabseque)
makeCircle(25,[250,250],[0,0,0],arabseque)
makeCircle(25,[275,275],[1,1,1],arabseque)
makeCircle(25,[225,225],[1,1,1],arabseque)
makeCircle(25,[275,225],[1,1,1],arabseque)
makeCircle(25,[225,275],[1,1,1],arabseque)
makeCircle(10,[250,250],[1,1,1],arabseque)



i=20;

makeCircle(25,[262,280+3*i],[0,0,0],arabseque)
makeCircle(25,[238,280+3*i],[0,0,0],arabseque)
makeCircle(25,[250,292+3*i],[0,0,0],arabseque)
makeCircle(25,[250,268+3*i],[0,0,0],arabseque)
makeCircle(34,[250,280+3*i],[1,1,1],arabseque)
makeCircle(12,[275,305+3*i],[1,1,1],arabseque)
makeCircle(12,[225,255+3*i],[1,1,1],arabseque)
makeCircle(12,[275,255+3*i],[1,1,1],arabseque)
makeCircle(12,[225,305+3*i],[1,1,1],arabseque)
makeCircle(4,[250,280+3*i],[1,1,1],arabseque)



i= -40;

makeCircle(25,[262,280+3*i],[0,0,0],arabseque)
makeCircle(25,[238,280+3*i],[0,0,0],arabseque)
makeCircle(25,[250,292+3*i],[0,0,0],arabseque)
makeCircle(25,[250,268+3*i],[0,0,0],arabseque)
makeCircle(34,[250,280+3*i],[1,1,1],arabseque)
makeCircle(12,[275,305+3*i],[1,1,1],arabseque)
makeCircle(12,[225,255+3*i],[1,1,1],arabseque)
makeCircle(12,[275,255+3*i],[1,1,1],arabseque)
makeCircle(12,[225,305+3*i],[1,1,1],arabseque)
makeCircle(4,[250,280+3*i],[1,1,1],arabseque)




makeCircle(50,[375,250],[0,0,0],arabseque)
makeCircle(40,[375,350],[0,0,0],arabseque)
makeCircle(40,[375,150],[0,0,0],arabseque)
makeCircle(50,[375,300],[1,1,1],arabseque)
makeCircle(50,[375,200],[1,1,1],arabseque)
makeCircle(40,[375,390],[1,1,1],arabseque)
makeCircle(40,[375,110],[1,1,1],arabseque)


makeCircle(50,[125,250],[0,0,0],arabseque)
makeCircle(20,[125,300],[1,1,1],arabseque)
makeCircle(20,[125,200],[1,1,1],arabseque)
makeCircle(20,[75,250],[1,1,1],arabseque)
makeCircle(20,[175,250],[1,1,1],arabseque)


makeCircle(30,[125,250],[1,1,1],arabseque)


makeCircle(25,[125,350],[0,0,0],arabseque)
makeCircle(25,[125,150],[0,0,0],arabseque)


makeCircle(20,[125,150],[1,1,1],arabseque)
makeCircle(20,[125,350],[1,1,1],arabseque)
makeCircle(10,[100,225],[1,1,1],arabseque)
makeCircle(10,[100,275],[1,1,1],arabseque)
makeCircle(10,[150,225],[1,1,1],arabseque)
makeCircle(10,[150,275],[1,1,1],arabseque)

makeCircle(15,[125,300],[0,0,0],arabseque)
makeCircle(15,[125,200],[0,0,0],arabseque)


makeCircle(15,[125,320],[1,1,1],arabseque)
makeCircle(15,[125,180],[1,1,1],arabseque)

makeCircle(15,[125,370],[1,1,1],arabseque)
makeCircle(15,[125,130],[1,1,1],arabseque)


makeCircle(15,[375,400],[0,0,0],arabseque)
makeCircle(15,[375,100],[0,0,0],arabseque)

makeCircle(15,[375,415],[1,1,1],arabseque)
makeCircle(15,[375,115],[1,1,1],arabseque)

makeCircle(15,[375,385],[1,1,1],arabseque)
makeCircle(15,[375,85],[1,1,1],arabseque)




	# Calculate distance from center of black ball to pixel at i,j (75+i,200+i)

plt.imshow(arabseque, interpolation='nearest')
plt.show()
