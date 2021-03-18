import numpy as np
import cv2
from matplotlib import pyplot as plt
import matplotlib.image as mpimg
import time
from array import *

height=500
width=500
blank_image = np.zeros((height,width,3), np.uint8)
blank_image[:,0:width//2] = (0,128,255)
blank_image[:,width//2:width] = (255,51,51)

cv2.imshow('Gambar', blank_image)
cv2.waitKey(0)