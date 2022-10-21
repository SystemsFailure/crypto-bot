import cv2
import mediapipe as mp
import numpy
import HandTrackingModule
import time

pTime = 0
detector = HandTrackingModule.handDetector(maxHands=1)

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)


def getFPS(pTime=None):
    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime
    return fps, pTime


while cap.isOpened():
    success, image = cap.read()
    image = detector.findHands(image)
    lmList, bbox = detector.findPosition(img=image, handNo=0)

    fps, pTime = getFPS(pTime)

    cv2.putText(image, str(int(fps)), (20, 50), cv2.FONT_HERSHEY_PLAIN, 1, (255,0,0), 1)
    cv2.imshow('Image', image)
    cv2.waitKey(1)






