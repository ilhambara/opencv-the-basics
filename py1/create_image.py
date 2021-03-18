import numpy as np
import cv2

# Menggambar Garis dan Bentuk
my_img = np.zeros((500,500,3), dtype="uint8")

cv2.line(my_img, (300,100), (150,100), (0,20,200), 5)
cv2.rectangle(my_img, (20,20), (100,100), (255,255,240), -1)
cv2.rectangle(my_img, (150,150), (250,250), (0,200,200), 3)
cv2.circle(my_img, (400,200), 50, (255,10,10), -1)
cv2.ellipse(my_img, (300, 400), (100,50), 0, 0, 180, (0,255,0), -1)

# Menggambar Polygon
my_img2 = np.zeros((500,500,3), dtype="uint8")

pts = np.array([[80,40], [120,300], [200,20], [50,20]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(my_img2, [pts], True, (0,255,255))

cv2.imshow('Shapes', my_img)
cv2.imshow('Polygon', my_img2)

cv2.waitKey(0)