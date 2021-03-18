import numpy as np
import cv2

blank = np.zeros((500,500,3), dtype='uint8')

# Menampilkan Blank Screen
# cv2.imshow('Blank', blank)

# Menggambar Warna tertentu
# blank[100:300, 100:400] = 0,0,255
# cv2.imshow('Red', blank)

# Menulis Sebuah Kalimat
cv2.putText(blank, 'NRP saya 2103187016', 
(50,200), cv2.FONT_HERSHEY_TRIPLEX, 1.0, (51,255,255), 2)
cv2.imshow('Text', blank)

cv2.waitKey(0)

