import numpy as np
import cv2
from matplotlib import pyplot as plt
import matplotlib.image as mpimg

img = cv2.imread('img/tree.jpg')
Z = img.reshape((-1,3))
# convert to np.float32
Z = np.float32(Z)
# define criteria, number of clusters(K) and apply kmeans()
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
K = 8
ret,label,center=cv2.kmeans(Z,K,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)
print("center", center)
print("label = ", label)
# Now convert back into uint8, and make original image
center = np.uint8(center)
res = center[label.flatten()]
res2 = res.reshape((img.shape))

plt.subplot(1,2,1), plt.imshow(img)
plt.title("Image")

plt.subplot(1,2,2), plt.imshow(res2)
plt.title("K = 8")

plt.show()