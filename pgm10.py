import cv2

path = "brain.webp"
img = cv2.imread(path)

gb = cv2.GaussianBlur(img, (15,15), 0)

mb = cv2.medianBlur(img, 15)

bf = cv2.bilateralFilter(img, 15, 150, 150)

cv2.imshow("Original", img)
cv2.imshow("Guassian blur", gb)
cv2.imshow("median blur", mb)
cv2.imshow("bilateral filter", bf)

cv2.waitKey(0)
cv2.destroyAllWindows()