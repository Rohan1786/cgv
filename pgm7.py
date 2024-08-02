import cv2
import numpy as np

path = "IMG_20220608_195024.jpg"
img = cv2.imread(path)

height , width, _ = img.shape

ul = img[0:height//2, 0:width//2]
ur = img[0:height//2, width//2:width]
dl = img[height//2:height, 0:width//2]
dr = img[height//2:height, width//2:width]

cv2.imshow("ul",ul)
cv2.waitKey(0)
cv2.imshow("ur",ur)
cv2.waitKey(0)
cv2.imshow("dl",dl)
cv2.waitKey(0)
cv2.imshow("dr",dr)
cv2.waitKey(0)

cv2.destroyAllWindows()