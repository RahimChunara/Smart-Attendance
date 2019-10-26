from imutils.perspective import four_point_transform
from imutils import contours
import numpy as np
import argparse
import imutils
import cv2

#############   resize      ######################
image = cv2.imread("test.jpg")
print(image.shape)



# scale_percent = 20 # percent of original size
# width = int(img.shape[1] * scale_percent / 100)
# height = int(img.shape[0] * scale_percent / 100)
# dim = (width, height)
# # resize image
# image = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)


# print(image.shape)
# cv2.imshow("Original", image)
# cv2.waitKey(10000)
# cv2.destroyAllWindows()

#########################################################################


gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
edged = cv2.Canny(blurred, 75, 200)

cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
docCnt = None

if len(cnts) > 0:

	cnts = sorted(cnts, key=cv2.contourArea, reverse=True)


	for c in cnts:

		peri = cv2.arcLength(c, True)
		approx = cv2.approxPolyDP(c, 0.02 * peri, True)


		if len(approx) == 4:
			docCnt = approx
			break
	else :
		print("get the picture of full image")
    
    

paper = four_point_transform(image, docCnt.reshape(4, 2))
warped = four_point_transform(gray, docCnt.reshape(4, 2))

# apply Otsu's thresholding method to binarize the warped piece of paper
thresh = cv2.threshold(warped, 0, 255,cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]

cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
questionCnts = []


for c in cnts:
	
	(x, y, w, h) = cv2.boundingRect(c)
	ar = w / float(h)

	
	if w >= 10 and h >= 20 and ar >= 0.9 and ar <= 1.1:
		questionCnts.append(c)


questionCnts = contours.sort_contours(questionCnts,method="top-to-bottom")[0]
correct = 0
roll=8312

for (q, i) in enumerate(np.arange(0, len(questionCnts), 5)):

	cnts = contours.sort_contours(questionCnts[i:i + 5])[0]
	bubbled = None
	g =0

	for (j, c) in enumerate(cnts):
		
		mask = np.zeros(thresh.shape, dtype="uint8")
		cv2.drawContours(mask, [c], -1, 255, -1)
    
		mask = cv2.bitwise_and(thresh, thresh, mask=mask)
		total = cv2.countNonZero(mask)
        
		bubbled = (total, j)
		if bubbled > (1000,0):
				g = g + 1
                
                
	score = (g / 5.0) * 100
	print(roll,":-",score) 
	roll=roll+1
        
cv2.waitKey(0)
