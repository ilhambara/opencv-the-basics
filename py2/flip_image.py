import numpy as np
import cv2
from matplotlib import pyplot as plt
import matplotlib.image as mpimg

img = mpimg.imread("img/animal.jpg")
horizontal_img = cv2.flip(img, 1)
vertical_img = cv2.flip(img, 0)
both_img = cv2.flip(img, -1)

(h,w) = img.shape[:2]
print(h,w)
center = (w/2, h/2)
angle90 = 90
angle180 = 180
angle270 = 270
scale = 1.0

M = cv2.getRotationMatrix2D(center, angle90, scale)
rotated90 = cv2.warpAffine(img, M, (w,h))
horizontal_img = rotated90

M = cv2.getRotationMatrix2D(center, angle180, scale)
rotated180 = cv2.warpAffine(img, M, (w,h))
vertical_img = rotated180

M = cv2.getRotationMatrix2D(center, angle270, scale)
rotated270 = cv2.warpAffine(img, M, (w,h))
both_img = rotated270

plt.subplot(2,2,1), plt.imshow(img)
plt.title('Original'), plt.xticks([]), plt.yticks([])

plt.subplot(2,2,2), plt.imshow(horizontal_img)
plt.title('Flip Horizontal'), plt.xticks([]), plt.yticks([])

plt.subplot(2,2,3), plt.imshow(vertical_img)
plt.title('Flip Vertical'), plt.xticks([]), plt.yticks([])

plt.subplot(2,2,4), plt.imshow(both_img)
plt.title('Flip Both'), plt.xticks([]), plt.yticks([])

plt.show()
