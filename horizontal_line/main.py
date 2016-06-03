import cv2
import numpy as np

im = cv2.imread('/Users/tatsuya/Desktop/main.jpg')
gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)

imgSplit = cv2.split(im)
flag,b = cv2.threshold(imgSplit[2],0,255,cv2.THRESH_OTSU)

element = cv2.getStructuringElement(cv2.MORPH_CROSS,(1,1))
cv2.erode(b,element)

edges = cv2.Canny(b,150,200,3,5)

img = im.copy()

lines = cv2.HoughLinesP(edges,100,np.pi/2,2, minLineLength = 620, maxLineGap = 100)[0]

for x1,y1,x2,y2 in lines:
  cv2.line(img,(x1,y1),(x2,y2),(0,255,0),1)

cv2.imshow('houghlines',img)
