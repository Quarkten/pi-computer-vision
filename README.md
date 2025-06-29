# Pi Computer Vision (with MediaPipe Hands + Face Detection)

Real-time face and hand detection using OpenCV and MediaPipe Hands on Raspberry Pi with OV7251 grayscale camera.

## Requirements
- Raspberry Pi 4 or 5
- OV7251 camera with `dtoverlay=ov7251` in `/boot/config.txt`
- Python 3.9+
- `libcamera` installed (Raspberry Pi OS Bookworm+)

## Setup
```bash
sudo apt update
sudo apt install -y libcamera-apps python3-opencv python3-numpy
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Run
```bash
source venv/bin/activate
python main.py
```

Press `q` to quit the video window.

## Features
- LBP face detection (fast on grayscale input)
- MediaPipe hand landmark tracking (21 points)
- Vertical camera flip for inverted cameras
- FPS display overlay