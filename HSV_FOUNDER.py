import cv2
import numpy as np

cap = cv2.VideoCapture("Downloads//s.mp4")
def bos(x):
    pass
cv2.namedWindow("Trackbar")
cv2.resizeWindow("Trackbar",300,300)
cv2.createTrackbar("Lower-H","Trackbar",0,180,bos)
cv2.createTrackbar("Lower-S","Trackbar",0,255,bos)
cv2.createTrackbar("Lower-V","Trackbar",0,255,bos)
cv2.createTrackbar("Upper-H","Trackbar",0,180,bos)
cv2.createTrackbar("upper-S","Trackbar",0,255,bos)
cv2.createTrackbar("upper-V","Trackbar",0,255,bos)
while True:
    ret,frame = cap.read()
    frame = cv2.resize(frame, (500, 500))
    if ret == False:
        break
    frames = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    lh = cv2.getTrackbarPos("Lower-H","Trackbar")
    ls = cv2.getTrackbarPos("Lower-S","Trackbar")
    lv = cv2.getTrackbarPos("Lower-V","Trackbar")
    uh = cv2.getTrackbarPos("Upper-H","Trackbar")
    us = cv2.getTrackbarPos("upper-S","Trackbar")
    uv = cv2.getTrackbarPos("upper-V","Trackbar")
    lowers = np.array([lh,ls,lv])
    uppers = np.array([uh,us,uv])
    mask = cv2.inRange(frames,lowers,uppers)
    cv2.imshow("Frame",frame)
    cv2.imshow("Mask",mask)
    if cv2.waitKey(100) & 0xFF==ord("q"):
        break

cap.release()
cv2.destroyAllWindows()