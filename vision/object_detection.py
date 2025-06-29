import cv2
import os
import mediapipe as mp

class ObjectDetector:
    def __init__(self):
        # Face detection with LBP
        path = "/usr/share/opencv4/lbpcascades/lbpcascade_frontalface.xml"
        if not os.path.exists(path):
            raise FileNotFoundError("Cascade not found at " + path)
        self.face_cascade = cv2.CascadeClassifier(path)

        # MediaPipe Hands
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(static_image_mode=False,
                                         max_num_hands=2,
                                         min_detection_confidence=0.5,
                                         min_tracking_confidence=0.5)
        self.mp_draw = mp.solutions.drawing_utils

    def detect(self, frame_gray, frame_color):
        # Detect faces
        faces = self.face_cascade.detectMultiScale(frame_gray, scaleFactor=1.1, minNeighbors=5)
        for (x, y, w, h) in faces:
            cv2.rectangle(frame_color, (x, y), (x + w, y + h), (255, 0, 0), 2)

        # Detect hands
        frame_rgb = cv2.cvtColor(frame_color, cv2.COLOR_BGR2RGB)
        results = self.hands.process(frame_rgb)
        if results.multi_hand_landmarks:
            for handLms in results.multi_hand_landmarks:
                self.mp_draw.draw_landmarks(frame_color, handLms, self.mp_hands.HAND_CONNECTIONS)

        return frame_color