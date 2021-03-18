import cv2
import numpy as np
ruta = r"C:\Users\dell\Pictures\miguel_angel.png"
im = cv2.imread(ruta, cv2.IMREAD_GRAYSCALE)
cv2.imshow('Normal', im)
a = [ [ -1.0, 0.0, 1.0 ],
           [ -1.0, 0.0, 1.0 ],
           [ -1.0, 0.0, 1.0 ] ]
kernel = np.asarray(a)
dst = cv2.filter2D(im, -1, kernel)
cv2.imshow('Convolución', dst)
cv2.waitKey(0)