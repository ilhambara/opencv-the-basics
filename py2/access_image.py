import numpy as np
import cv2
from matplotlib import pyplot as plt

# Membalik urutan warna pada gambar saat ditampilkan
img01 = cv2.imread('img/animal.jpg')
row1, col1, n = img01.shape
print (row1, col1)

img02 = np.zeros((row1, col1, 3), np.uint8)
img03 = np.zeros((140, 200, 3), np.uint8)
img04 = np.zeros((140, 200, 3), np.uint8)

# Mengkonversi warna dari BGR menjadi RGB
img02 = cv2.cvtColor(img01, cv2.COLOR_BGR2RGB)

# Menyalin gambar ke-2 sebagai gambar ke-3
img03 = img02.copy()

# Memberikan warna pada gambar ke-4
color = (0, 0, 255)
img04 = np.full((140, 200, 3), color, np.uint8)
row4, col4, n = img04.shape
print (row4, col4)

plt.subplot(2,2,1), plt.imshow(img01)
plt.title('Image 01'), plt.xticks([]), plt.yticks([])

plt.subplot(2,2,2), plt.imshow(img02)
plt.title('Image 02'), plt.xticks([]), plt.yticks([])

plt.subplot(2,2,3), plt.imshow(img03)
plt.title('Image 03'), plt.xticks([]), plt.yticks([])

plt.subplot(2,2,4), plt.imshow(img04)
plt.title('Image 04'), plt.xticks([]), plt.yticks([])

plt.show()
