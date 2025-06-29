import cv2
import mediapipe as mp
import time

class ObjectDetector:
    def __init__(self):
        # MediaPipe Hands
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(static_image_mode=False,
                                         max_num_hands=1,
                                         min_detection_confidence=0.6,
                                         min_tracking_confidence=0.5)
        self.mp_draw = mp.solutions.drawing_utils
        self.last_frame_time = 0
        self.min_interval = 1.0 / 30  # Limit to 30 FPS

    def detect(self, frame):
        now = time.time()
        if now - self.last_frame_time < self.min_interval:
            return frame
        self.last_frame_time = now

        # Hand detection
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.hands.process(frame_rgb)
        if results.multi_hand_landmarks:
            for handLms in results.multi_hand_landmarks:
                self.mp_draw.draw_landmarks(frame, handLms, self.mp_hands.HAND_CONNECTIONS)

        return frame