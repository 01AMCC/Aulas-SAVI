import cv2 as cv
import sys
img = cv.imread("lake.jpg")
cv.imshow("Display window", img)
cv.waitKey(0)