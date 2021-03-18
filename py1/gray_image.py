import numpy as np
import cv2
from matplotlib import pyplot as plt
import matplotlib.image as mpimg
import time
from array import *

original = mpimg.imread('img/omen.jpg')
grays = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
ret, biner = cv2.threshold(grays, 127, 255, cv2.THRESH_BINARY)

plt.subplot(3,1,1), plt.imshow(original, cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])

plt.subplot(3,1,2), plt.imshow(grays, cmap = 'gray')
plt.title('Grayscale'), plt.xticks([]), plt.yticks([])

plt.subplot(3,1,3), plt.imshow(biner, cmap = 'gray')
plt.title('Biner'), plt.xticks([]), plt.yticks([])

plt.show()

