import cv2 as cv
import numpy as np
img = cv.imread r'‪C:\Users\dell\Pictures\miguel_angel.png',0
kernel = np.ones((5,5),np.uint8)
erosion = cv.erode(img,kernel,iterations = 1)