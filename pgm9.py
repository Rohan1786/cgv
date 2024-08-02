import cv2
import numpy as np

path = "brain.webp"
img = cv2.imread(path)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

edges = cv2.Canny(gray, 100, 200)

kernel = np.ones((5,5), np.float32)

texture = cv2.filter2D(gray, -1, kernel)

cv2.imshow("original",img)
cv2.imshow("edges",edges)
cv2.imshow("texture",texture)

cv2.waitKey(0)
cv2.destroyAllWindows()