import numpy as np
import cv2
from matplotlib import pyplot as plt
import matplotlib.image as mpimg
import time
from array import *

height=400
width=400
img = np.zeros((height,width,3), np.uint8)
col1, row1, n = img.shape
print (row1, col1)

for y1 in range(0,width):
    for x1 in range(0,height//2):
        img[x1,y1] = [255,0,0]

for y1 in range(0,width):
    for x1 in range(height//2,height):
        img[x1,y1] = [255,255,255]

res = cv2.resize(img,None,fx=0.1, fy=0.1, interpolation=cv2.INTER_CUBIC)
col2, row2, n = res.shape
print (row2,col2)

plt.subplot(1,2,1), plt.imshow(img)
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(1,2,2), plt.imshow(img)
plt.title('Resize'), plt.xticks([]), plt.yticks([])
plt.show()