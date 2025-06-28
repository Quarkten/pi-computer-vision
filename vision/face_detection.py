import cv2

class FaceDetector:
    def __init__(self):
        # Use LBP for faster grayscale face detection
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'lbpcascade_frontalface.xml')

    def detect(self, frame_gray, frame_color):
        faces = self.face_cascade.detectMultiScale(frame_gray, scaleFactor=1.1, minNeighbors=5)
        for (x, y, w, h) in faces:
            cv2.rectangle(frame_color, (x, y), (x + w, y + h), (255, 0, 0), 2)
        return frame_color