import cv2
from cvzone.HandTrackingModule import HandDetector

cam = cv2.VideoCapture(0)
detector = HandDetector(maxHands=2)

while True:
    check, frame = cam.read()
    hands, frame = detector.findHands(frame)
    cv2.imshow('video', frame)
    key = cv2.waitKey(1)
    if key == 27:
        break

cam.release()
cv2.destroyAllWindows()