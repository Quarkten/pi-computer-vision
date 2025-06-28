import cv2
import os

class FaceDetector:
    def __init__(self):
        path = "/usr/share/opencv4/lbpcascades/lbpcascade_frontalface.xml"
        if not os.path.exists(path):
            raise FileNotFoundError("Cascade not found at " + path)
        self.face_cascade = cv2.CascadeClassifier(path)

    def detect(self, frame_gray, frame_color):
        faces = self.face_cascade.detectMultiScale(frame_gray, scaleFactor=1.1, minNeighbors=5)
        for (x, y, w, h) in faces:
            cv2.rectangle(frame_color, (x, y), (x + w, y + h), (255, 0, 0), 2)
        return frame_color
