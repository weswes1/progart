
import math

def makeCircle(rad,center,color,jamesHouse):
	for i in range(center[0]-rad,center[0]+rad):
		for j in range(center[1]-rad,center[1]+rad):
			if (math.ceil(math.pow((i-center[0])**2 + (j-center[1])**2,.5)) <= rad):
				jamesHouse[i,j] = color

# Makes a rectangnle with height, width, and color centered at coordinates of center 	


def makeEllipse(a,b,center,color,image):
	for i in range(center[0]-a,center[0]+a):
		for j in range(center[1]-b,center[1]+b):
			if (math.ceil(math.pow(i-center[0],2)/math.pow(a,2)+math.pow(j-center[1],2)/math.pow(b,2)) == 1):
				image[i,j]=color
				print(i,j)



def makeRect(height,width,color,center,image):
	for i in range(center[0]-height,center[0]+height):
		for j in range(center[1]-width,center[1]+width):
			image[i,j]=color


def makeTriangle(base,height):
	pass
# Creates a background color of white

def averagemask(rowstart,colstart,width,factor=1.0/9.0,t=1):
	for i in range(0,t):
		for i in range(rowstart,rowstart+width):
			for j in range(colstart,colstart+width):
				jamesHouse[i,j] = factor*(jamesHouse[i,j]+jamesHouse[i+1,j]+jamesHouse[i-1,j]+jamesHouse[i,j-1]+jamesHouse[i+1,j-1]+jamesHouse[i-1,j-1]+jamesHouse[i,j+1]+jamesHouse[i+1,j+1]+jamesHouse[i-1,j+1])

