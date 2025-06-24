# pi-computer-vision
OpenCV + computer vision

Real-time face, hand, and fingertip detection using OpenCV and MediaPipe. Optimized for Raspberry Pi but developed on desktop for faster testing.

## Features
- ✅ Face detection
- ✅ Hand detection
- ✅ Fingertip tracking

## Setup
```bash
git clone https://github.com/yourname/pi-computer-vision.git
cd pi-computer-vision
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python main.py
```

Press `q` to quit the preview window.

## Hardware
- Works on both macOS and Raspberry Pi
- On Pi, reduce resolution in `main.py` if performance lags:
```python
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)
