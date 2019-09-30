import cv2 # import the OpenCV library
import numpy as np # import the numpy library

img_name='./ressources/img/mountain.jpg'

img_gray=cv2.imread(img_name, 0) # load an image in gray levels
img_bgr=cv2.imread(img_name, 1) # load an image in Blue Green Red

#display the matrix shapes
print("Gray levels image shape = "+str(img_gray.shape))
print("BGR image shape = "+str(img_bgr.shape))

#display the loaded images
cv2.imshow("Gray levels image", img_gray)
cv2.imshow("BGR image", img_bgr)
cv2.waitKey()