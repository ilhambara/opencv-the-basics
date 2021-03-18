import cv2

image = cv2.imread('img/logo2.jpg')
resize_image = cv2.resize(image, (200,200))

cv2.imshow('Original', image)
cv2.imshow('Frame Rescale', resize_image)

cv2.waitKey(0)