import cv2
import os
import mediapipe as mp

class ObjectDetector:
    def __init__(self):
        # Load face cascade
        path = "/usr/share/opencv4/lbpcascades/lbpcascade_frontalface.xml"
        if not os.path.exists(path):
            raise FileNotFoundError("Cascade not found at " + path)
        self.face_cascade = cv2.CascadeClassifier(path)

        # Setup MediaPipe Hands (lightweight)
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(static_image_mode=False,
                                         max_num_hands=1,
                                         min_detection_confidence=0.6,
                                         min_tracking_confidence=0.5)
        self.mp_draw = mp.solutions.drawing_utils

    def detect(self, gray_frame, color_frame):
        # Face detection
        faces = self.face_cascade.detectMultiScale(gray_frame, scaleFactor=1.2, minNeighbors=5)
        for (x, y, w, h) in faces:
            cv2.rectangle(color_frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        # Hand detection (once per frame)
        frame_rgb = cv2.cvtColor(color_frame, cv2.COLOR_BGR2RGB)
        results = self.hands.process(frame_rgb)
        if results.multi_hand_landmarks:
            for handLms in results.multi_hand_landmarks:
                self.mp_draw.draw_landmarks(color_frame, handLms, self.mp_hands.HAND_CONNECTIONS)

        return color_frame