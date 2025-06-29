import cv2
import subprocess
import numpy as np

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

while True:
    yuv_size = WIDTH * HEIGHT * 3 // 2
    raw_frame = proc.stdout.read(yuv_size)
    if not raw_frame:
        print("❌ No frame received.")
        break

    yuv = np.frombuffer(raw_frame, dtype=np.uint8).reshape((HEIGHT * 3 // 2, WIDTH))
    color_frame = cv2.cvtColor(yuv, cv2.COLOR_YUV2BGR_I420)

    color_frame = detector.detect(color_frame)

    cv2.imshow("Pi Camera Vision", color_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
proc.terminate()