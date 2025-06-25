from picamera2 import Picamera2
import cv2
import time

from vision.hand_detection import HandDetector
from vision.face_detection import FaceDetector

# Initialize Pi camera
picam2 = Picamera2()
config = picam2.preview_configuration(main={"format": "RGB888", "size": (640, 480)})
picam2.configure(config)
picam2.start()
time.sleep(2)  # let camera warm up

# Initialize detectors
hand_detector = HandDetector()
face_detector = FaceDetector()

# Initialize FPS calculation
prev_time = time.time()
fps = 0

# Optional: initialize video writer
record = False
video_writer = None
if record:
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    video_writer = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

frame_count = 0
skip_rate = 2  # Process detections every N frames

while True:
    frame = picam2.capture_array()
    frame_count += 1

    # FPS calculation
    curr_time = time.time()
    fps = 1 / (curr_time - prev_time)
    prev_time = curr_time

    # Run detection every N frames to save CPU
    if frame_count % skip_rate == 0:
        frame = face_detector.detect(frame)
        frame = hand_detector.detect(frame)

    # Overlay FPS
    cv2.putText(frame, f"FPS: {fps:.2f}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

    # Display output
    cv2.imshow("Pi Vision", frame)

    # Optional: save to video
    if record and video_writer:
        video_writer.write(frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
if video_writer:
    video_writer.release()
