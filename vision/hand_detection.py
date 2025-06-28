import cv2
import numpy as np

class HandDetector:
    def __init__(self):
        pass  # No model, just simple thresholding

    def detect(self, frame_gray, frame_color):
        # Basic contour detection on high-contrast thresholded image
        _, thresh = cv2.threshold(frame_gray, 80, 255, cv2.THRESH_BINARY_INV)
        contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        for cnt in contours:
            if cv2.contourArea(cnt) > 1000:
                x, y, w, h = cv2.boundingRect(cnt)
                cv2.rectangle(frame_color, (x, y), (x + w, y + h), (0, 255, 0), 2)
        return frame_color