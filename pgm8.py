import cv2
import numpy as np

path = "IMG_20220608_195024.jpg"
img = cv2.imread(path)

height, width, _ = img.shape

rotmat = cv2.getRotationMatrix2D((width/2, height/2), 45, 1)
scmat = np.float32([[1.5,0,0],[0,1.5,0]])
tramat = np.float32([[1,0,100],[0,1,50]])

rotate = cv2.warpAffine(img, rotmat, (height,width))
scale = cv2.warpAffine(img, scmat, (int(height*1.5),int(width*1.5)))
translate = cv2.warpAffine(img, tramat, (height,width))

cv2.imshow("or",img)
cv2.imshow("rotate",rotate)
cv2.imshow("scale", scale)
cv2.imshow("translate", translate)
cv2.waitKey(0)
cv2.destroyAllWindows()