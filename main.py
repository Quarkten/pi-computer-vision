import cv2
from vision.face_detection import FaceDetector
from vision.hand_detection import HandDetector
from vision.finger_tracking import FingerTracker

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)

face_detector = FaceDetector()
hand_detector = HandDetector()
finger_tracker = FingerTracker()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = face_detector.detect(frame)
    frame = hand_detector.detect(frame)
    frame = finger_tracker.track(frame)

    cv2.imshow("Computer Vision Pi", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
