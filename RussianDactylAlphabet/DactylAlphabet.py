import cv2
import HandTrackingModule as htm
import RecognizeAlphabet as alph

#   Camera parameters
wCam, hCam = 1280, 720
#   Camera capture
cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
#   Hands detector creation
detector = htm.handDetector()

while True:
    success, img = cap.read()
    detector.findHands(img)
#   Landmarks List creation
    lmList = detector.findPosition(img, draw=False)
#   Using of alphabet recognition function
    if len(lmList) != 0:
        cv2.putText(img, alph.alphabet(lmList), (50, 150), cv2.FONT_HERSHEY_COMPLEX, 3, (0, 0, 0), 5)

    cv2.imshow('Russian dactyl alphabet', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
