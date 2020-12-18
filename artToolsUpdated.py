import math
import random


def makeCircle(rad,center,color,image):
	for i in range(center[0]-rad,center[0]+rad):
		for j in range(center[1]-rad,center[1]+rad):
			if (math.ceil(math.pow((i-center[0])**2 + (j-center[1])**2,.5)) <= rad):
				image[i,j] = color

# Makes a rectangnle with height, width, and color centered at coordinates of center 	


def makeEllipse(a,b,center,color,image):
	for i in range(center[0]-a,center[0]+a):
		for j in range(center[1]-b,center[1]+b):
			if (math.ceil(math.pow(i-center[0],2)/math.pow(a,2)+math.pow(j-center[1],2)/math.pow(b,2)) == 1):
				image[i,j]=color


def equaliteralTriange(sideLength,point,color,image):
	while sideLength > 0:
		for i in range(0,sideLength):
			image[point[0],point[1]+i]=color
		point = [point[0]-1,point[1]+1]
		sideLength-=2


def makeRect(height,width,color,center,image):
	for i in range(center[0]-height,center[0]+height):
		for j in range(center[1]-width,center[1]+width):
			image[i,j]=color;


def illuminate(centerx,centery,color,density,iterations,image):
	for i in range(0,iterations):
		xi = random.uniform(0,1)
		th = random.uniform(0,1)*2*math.pi
		r = density*math.sqrt(xi/(1-xi))
		x = centerx+r*math.cos(th)
		y = centery+r*math.sin(th)
		if (x >= 0 and x < 500 and  y >= 0 and y < 500):
			image[int(x),int(y)] = color

def averagemask(rowstart,colstart,width,factor,t,image):
	for i in range(0,t):
		for i in range(rowstart,rowstart+width):
			for j in range(colstart,colstart+width):
				image[i,j] = factor*(image[i,j]+image[i+1,j]+image[i-1,j]+image[i,j-1]+image[i+1,j-1]+image[i-1,j-1]+image[i,j+1]+image[i+1,j+1]+image[i-1,j+1])

def diagnol(startx,starty,length,depth,color,image):
	for j in range(0,length):
		for k in range(0,depth):
			image[startx+j+k,starty+j]=color;
