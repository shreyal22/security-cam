import cv2
import winsound
import numpy as np
cam=cv2.VideoCapture(0)
while True:
     ret,frame1=cam.read()

     col=cv2.cvtColor(frame1,cv2.COLOR_BGR2HSV)
         # Red color
     low_red = np.array([161, 155, 84])
     high_red = np.array([179, 255, 255])
     red_mask = cv2.inRange(col, low_red, high_red)
     red = cv2.bitwise_and(frame1, frame1, mask=red_mask)
     

     if cv2.waitKey(10)==ord('q'):
         break
     #cv2.imshow('jarvis eye',frame1)
     cv2.imshow('red',red)
