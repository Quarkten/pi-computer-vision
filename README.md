Real-time face and hand detection using OpenCV on Raspberry Pi.

## Requirements
- Raspberry Pi 4 or better
- Camera Module (enabled in raspi-config)
- Python 3.9+

## Install Dependencies
```bash
sudo apt update
sudo apt install -y python3-picamera2
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Run the Program
```bash
source venv/bin/activate
python main.py
```

Press `q` to quit the camera window.