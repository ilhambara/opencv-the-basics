import numpy as np
import cv2
from matplotlib import pyplot as plt
import matplotlib.image as mpimg

img = mpimg.imread("img/child.jpg")
row,col,n = img.shape
img1 = np.zeros((row, col, 3), np.uint8)
img2 = np.zeros((row, col, 3), np.uint8)
img3 = np.zeros((row, col, 3), np.uint8)
img4 = np.zeros((row, col, 3), np.uint8)
img5 = np.zeros((row, col, 3), np.uint8)

a = 64 #threshold
b = int(256/a)
print("a1=",b)
for y in range(0,col-1):
    for x in range(0,row-1):
        R,G,B=img[x,y]
        b=int(256/a)
        R=b*int(R/b)
        G=b*int(G/b)
        B=b*int(B/b)
        img1[x,y]=[R,G,B]

a = 32 #threshold
b = int(256/a)
print("a2=",b)
for y in range(0,col-1):
    for x in range(0,row-1):
        R,G,B=img[x,y]
        b=int(256/a)
        R=b*int(R/b)
        G=b*int(G/b)
        B=b*int(B/b)
        img2[x,y]=[R,G,B]

a = 16 #threshold
b = int(256/a)
print("a3=",b)
for y in range(0,col-1):
    for x in range(0,row-1):
        R,G,B=img[x,y]
        b=int(256/a)
        R=b*int(R/b)
        G=b*int(G/b)
        B=b*int(B/b)
        img3[x,y]=[R,G,B]

a = 8 #threshold
b = int(256/a)
print("a4=",b)
for y in range(0,col-1):
    for x in range(0,row-1):
        R,G,B=img[x,y]
        b=int(256/a)
        R=b*int(R/b)
        G=b*int(G/b)
        B=b*int(B/b)
        img4[x,y]=[R,G,B]

a = 2 #threshold
b = int(256/a)
print("a5=",b)
for y in range(0,col-1):
    for x in range(0,row-1):
        R,G,B=img[x,y]
        b=int(256/a)
        R=b*int(R/b)
        G=b*int(G/b)
        B=b*int(B/b)
        img5[x,y]=[R,G,B]

titles = ['Original', 'Th = 64', 'Th = 32', 'Th = 16', 'Th = 8', 'Th = 2']
images = [img, img1, img2, img3, img4, img5]
for i in range(6):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray',vmin=0,vmax=255)
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()
