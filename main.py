import cv2
import subprocess
import numpy as np
import time
from vision.object_detection import HandDetector

WIDTH, HEIGHT = 640, 480
FPS_CAP = 30
FRAME_SKIP = 2  # Only process every 2nd frame

command = [
    "libcamera-vid",
    "-t", "0",
    "--width", str(WIDTH),
    "--height", str(HEIGHT),
    "--codec", "yuv420",
    "-n",
    "-o", "-"
]

proc = subprocess.Popen(command, stdout=subprocess.PIPE, bufsize=WIDTH * HEIGHT * 3)

hand_detector = HandDetector()

prev_time = time.time()
frame_idx = 0

while True:
    yuv_size = WIDTH * HEIGHT * 3 // 2
    raw_frame = proc.stdout.read(yuv_size)

    if not raw_frame:
        print("❌ No frame received.")
        break

    try:
        yuv = np.frombuffer(raw_frame, dtype=np.uint8).reshape((HEIGHT * 3 // 2, WIDTH))
        frame = cv2.cvtColor(yuv, cv2.COLOR_YUV2BGR_I420)
    except:
        continue

    # FPS limiting
    now = time.time()
    elapsed = now - prev_time
    if elapsed < 1 / FPS_CAP:
        continue
    prev_time = now

    # Skip frames
    frame_idx += 1
    if frame_idx % FRAME_SKIP != 0:
        continue

    # Process only every few frames
    frame = hand_detector.detect(frame)

    cv2.imshow("Hand Detection", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
proc.terminate()
