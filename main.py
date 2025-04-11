import cv2 #import the respect opencv package
cam = cv2.VideoCapture(0) # declare cam used to capture video
while True:
    _,frame = cam.read()
    cv2.imshow('Eye control mouse', frame)
    cv2.waitKey(1)
