import cv2 # import the OpenCV library
import numpy as np # import the numpy library

img_name='./ressources/img/mountain.jpg'

img_gray=cv2.imread(img_name, 0) # load an image in gray levels
img_bgr=cv2.imread(img_name, 1) # load an image in Blue Green Red

#display the matrix shapes
print("Gray levels image shape = "+str(img_gray.shape))
print("BGR image shape = "+str(img_bgr.shape))


def invert_colors_manual_slow(input_img):
    for row in range(input_img.shape[0]):
        for col in range(input_img.shape[1]):
            for channel in range(input_img.shape[2]):
                input_img[row, col, channel] = 255 - input_img[row, col, channel]
    
    return input_img

def invert_colors_manual_fast(input_img):
    return 255-input_img


#display the loaded images
# cv2.imshow("Gray levels image", img_gray)
# cv2.imshow("BGR image", img_bgr)
# cv2.imshow("Inversed image (slow)", invert_colors_manual(img_bgr))
cv2.imshow("Inversed image (fast)", invert_colors_manual_fast(img_bgr))
cv2.waitKey()