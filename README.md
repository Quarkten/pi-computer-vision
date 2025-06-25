
Real-time face, hand, and fingertip detection using OpenCV only. Fully compatible with Raspberry Pi 4 (64-bit).

## Features
- Face detection via Haar Cascades
- Hand bounding via skin color threshold
- Fingertip tracking via convexity defects

## How to Run
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python main.py
```

## Controls
- Press `q` to quit

## Notes
- No MediaPipe or TensorFlow required
- Optimized for Raspberry Pi performance