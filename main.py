import cv2
import subprocess
import numpy as np
import time

from vision.hand_detection import HandDetector
from vision.face_detection import FaceDetector

WIDTH, HEIGHT = 640, 480

command = [
    "libcamera-vid",
    "-t", "0",
    "--width", str(WIDTH),
    "--height", str(HEIGHT),
    "--codec", "yuv420",
    "-n",
    "-o", "-",
]

proc = subprocess.Popen(command, stdout=subprocess.PIPE, bufsize=WIDTH * HEIGHT * 3)

hand_detector = HandDetector()
face_detector = FaceDetector()

prev_time = time.time()
frame_count = 0
skip_rate = 3

while True:
    yuv_size = WIDTH * HEIGHT * 3 // 2
    raw_frame = proc.stdout.read(yuv_size)
    if not raw_frame:
        print("❌ No frame received.")
        break

    yuv = np.frombuffer(raw_frame, dtype=np.uint8).reshape((HEIGHT * 3 // 2, WIDTH))
    frame_color = cv2.cvtColor(yuv, cv2.COLOR_YUV2BGR_I420)
    frame_gray = cv2.cvtColor(frame_color, cv2.COLOR_BGR2GRAY)

    frame_count += 1
    if frame_count % skip_rate == 0:
        frame_color = face_detector.detect(frame_gray, frame_color)
        frame_color = hand_detector.detect(frame_gray, frame_color)

    curr_time = time.time()
    fps = 1 / (curr_time - prev_time)
    prev_time = curr_time

    cv2.putText(frame_color, f"FPS: {fps:.2f}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
    cv2.imshow("Pi BW Camera Feed", frame_color)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
proc.terminate()