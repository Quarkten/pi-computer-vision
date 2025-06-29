import cv2
import mediapipe as mp

class HandDetector:
    def __init__(self, max_num_hands=1):
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(
            static_image_mode=False,
            max_num_hands=max_num_hands,
            min_detection_confidence=0.6,
            min_tracking_confidence=0.5,
        )
        self.mp_draw = mp.solutions.drawing_utils

    def detect(self, frame):
        # Resize to lower res for performance
        small = cv2.resize(frame, (320, 240))
        rgb_small = cv2.cvtColor(small, cv2.COLOR_BGR2RGB)
        results = self.hands.process(rgb_small)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                # Scale landmarks back to original frame
                for lm in hand_landmarks.landmark:
                    x = int(lm.x * frame.shape[1])
                    y = int(lm.y * frame.shape[0])
                    cv2.circle(frame, (x, y), 2, (0, 255, 0), -1)

        return frame
