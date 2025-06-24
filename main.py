import cv2
from vision.hand_detection import HandDetector
from vision.face_detection import FaceDetector
from vision.finger_tracking import FingerTracker

cap = cv2.VideoCapture(0)
detector_hand = HandDetector()
detector_face = FaceDetector()
detector_finger = FingerTracker()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = detector_hand.detect(frame)
    frame = detector_face.detect(frame)
    frame = detector_finger.track(frame)

    cv2.imshow("Pi Vision", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

