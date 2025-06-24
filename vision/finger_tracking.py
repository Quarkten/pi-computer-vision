import cv2
import mediapipe as mp

class FingerTracker:
    def __init__(self):
        self.hands = mp.solutions.hands.Hands()
        self.mp_draw = mp.solutions.drawing_utils

    def track(self, frame):
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.hands.process(rgb)
        if results.multi_hand_landmarks:
            for handLms in results.multi_hand_landmarks:
                for id, lm in enumerate(handLms.landmark):
                    h, w, _ = frame.shape
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    if id in [4, 8, 12, 16, 20]:  # Fingertip landmark IDs
                        cv2.circle(frame, (cx, cy), 10, (0, 255, 0), cv2.FILLED)
                self.mp_draw.draw_landmarks(frame, handLms, mp.solutions.hands.HAND_CONNECTIONS)
        return frame