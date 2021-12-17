import cv2
cam=cv2.VideoCapture(0)
while cam.isOpened():
     ret,frame=cam.show()
     if cam.runAndWait()==ord('q'):
         break
     cv2.imshow('jarvis eye',frame)
