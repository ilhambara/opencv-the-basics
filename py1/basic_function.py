import cv2

# Menampilkan gambar asli
img = cv2.imread('img/valorant.jpg')
cv2.imshow('Basic Image', img)

# Menampilkan gambar grayscale
grays = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Grayscale', grays)

# Menampilkan gambar blur
blur = cv2.GaussianBlur(img, (5,5), cv2.BORDER_DEFAULT)
cv2.imshow('Gaussian Blur', blur)

# Menampilkan gambar Edge Cascade
canny = cv2.Canny(img, 125, 175)
cv2.imshow('Canny Edges', canny)

# Menampilkan gambar Melebar
dilated = cv2.dilate(img, (5,5), iterations=3)
cv2.imshow('Dilated', dilated)

# Menampilkan gambar Terkikis
eroded = cv2.erode(img, (7,7), iterations=3)
cv2.imshow('Eroded', eroded)

cv2.waitKey(0)