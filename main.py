import cv2
import subprocess
import numpy as np
import time

from vision.object_detection import ObjectDetector

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

detector = ObjectDetector()

prev_time = time.time()
frame_count = 0
skip_rate = 3  # do detection every 3rd frame

while True:
    yuv_size = WIDTH * HEIGHT * 3 // 2
    raw_frame = proc.stdout.read(yuv_size)
    if not raw_frame:
        print("❌ No frame received.")
        break

    yuv = np.frombuffer(raw_frame, dtype=np.uint8).reshape((HEIGHT * 3 // 2, WIDTH))
    color_frame = cv2.cvtColor(yuv, cv2.COLOR_YUV2BGR_I420)
    gray_frame = cv2.cvtColor(color_frame, cv2.COLOR_BGR2GRAY)

    frame_count += 1
    if frame_count % skip_rate == 0:
        color_frame = detector.detect(gray_frame, color_frame)

    curr_time = time.time()
    fps = 1 / (curr_time - prev_time)
    prev_time = curr_time

    cv2.putText(color_frame, f"FPS: {fps:.2f}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)
    cv2.imshow("Pi Camera Vision", color_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
proc.terminate()
