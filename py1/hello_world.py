import cv2

original = cv2.imread("img/logo1.jpg")
resize = cv2.resize(original, (400, 400))
rotate_180 = cv2.rotate(resize, cv2.ROTATE_180)

# menampilkan gambar
cv2.imshow("My Logo", original)
cv2.imshow("Resized Logo", resize)
cv2.imshow("Rotated Logo", rotate_180)

# menyimpan gambar
cv2.imwrite("img/logo2.jpg", resize)
cv2.imwrite("img/logo3.jpg", rotate_180)

cv2.waitKey(0)
