import cv2
import numpy as np
import pytesseract
from PIL import Image
from pytesseract import image_to_string



def get_string(img_path):
   
    img = cv2.imread("img.jpg")

    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply dilation and erosion to remove some noise
    kernel = np.ones((1, 1), np.uint8)
    img = cv2.dilate(img, kernel, iterations=1)
    img = cv2.erode(img, kernel, iterations=1)

    # noise reduction
    cv2.imwrite(src_path + "removed_noise.png", img)

    # threshold:- img to b&w 
    #img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)

    cv2.imwrite(src_path + "thres.png", img)
    
    result = pytesseract.image_to_string(Image.open(src_path + "thres.png"))

   
    return result


print('below is then text thats read')
print('-----------------------------------------------------------')
print(get_string(src_path + "cont.jpg") )
print('-----------------------------------------------------------')
print("The end")
