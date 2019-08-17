from matplotlib import pyplot as plt
from PIL import Image, ImageFilter
from skimage import filters, img_as_ubyte
from scipy import misc
import numpy as np
import math
import random
import skimage
import matplotlib.animation as animation
from artTools import *


commonsPark = np.zeros((500,500,3))


for i in range(0,500):
	for j in range(0,500):
		commonsPark[i,j]=[0,0,1]


plt.imshow(commonsPark, interpolation='nearest')
plt.show()

