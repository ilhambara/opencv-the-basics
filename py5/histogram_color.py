import numpy as np
import cv2
from matplotlib import pyplot as plt
import matplotlib.image as mpimg

img1 = cv2.imread('img/animal.jpg')
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
color = ('r', 'g', 'b')
plt.subplot(1,2,1), plt.imshow(img1)
plt.title('Image')
print("enumerate =", enumerate(color))
for i,col in enumerate(color):
    histr = cv2. calcHist([img1], [i], None, [256], [0, 256])
    plt.subplot(1,2,2), plt.plot(histr, color = col), plt.xlim([0, 256])
    plt.title('Histogram Color')

plt.show()