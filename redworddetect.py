import cv2

import numpy as np

import matplotlib.pyplot as plt

import os
%matplotlib inline

os.chdir('C:/Users/Gavin/Desktop')

img = cv2.imread('image2.jpg')


plt.imshow(img)


hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

plt.imshow(hsv)


# Range for lower red
lower_red = np.array([0,120,70])
upper_red = np.array([10,255,255])
mask1 = cv2.inRange(hsv, lower_red,upper_red)

# Range for upper range
lower_red = np.array([170,120,70])
upper_red = np.array([180,255,255])
mask2 = cv2.inRange(hsv,lower_red,upper_red)

# Generating the final mask to detect red color
mask1 = mask1+mask2

#identify text with black background
dst = cv2.bitwise_and(img, img, mask=mask1)

#identify text with grey scale image
res = cv2.bitwise_not(mask1)

plt.imshow(dst)

plt.imshow(res)

cv2.imwrite("dst.jpg", dst)

cv2.imwrite("res.jpg", res)

###############################################################################


from PIL import Image 
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

text1 = str(((pytesseract.image_to_string(Image.open("res.jpg"),lang = 'eng'))))

text2 = str(((pytesseract.image_to_string(Image.open("dst.jpg"),lang = 'eng'))))
print("text is:-")
print(text1)
print("this is secondary text:- ")
print(text2)
