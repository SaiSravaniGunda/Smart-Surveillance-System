# AI-Powered Smart Surveillance System

## Overview
This project is an AI-powered smart surveillance system using a Raspberry Pi, PIR motion sensor, and OpenCV for face detection. When motion is detected, the system captures an image and checks for human faces. If a face is detected, alerts are sent via Telegram and SMS (using Twilio).

## Features
- **Motion Detection**: Uses a PIR sensor to detect movement.
- **Face Recognition**: Uses OpenCV to detect faces in captured images.
- **Image Capture**: Captures images with the Raspberry Pi Camera when motion is detected.
- **Alerts**:
  - Sends Telegram messages with captured images.
  - Sends SMS alerts via Twilio.
- **Secure Credentials**: Uses a `.env` file to store sensitive credentials.

## Requirements
### Hardware:
- Raspberry Pi (any model with GPIO support)
- PIR Motion Sensor
- PiCamera Module

### Software & Libraries:
Install all dependencies using the following command:
```bash
pip install -r requirements.txt
```
Or manually install:
```bash
pip install opencv-python numpy telepot twilio RPi.GPIO picamera imutils python-dotenv
```

## Setup Instructions
### 1. Clone the Repository
```bash
git clone https://github.com/your-repo/smart-surveillance.git
cd smart-surveillance
```

### 2. Create a `.env` File
Create a `.env` file in the project directory and add the following:
```
TELEGRAM_BOT_TOKEN=your_telegram_bot_token
TELEGRAM_CHAT_ID=your_chat_id
TWILIO_SID=your_twilio_sid
TWILIO_AUTH=your_twilio_auth
TWILIO_PHONE=your_twilio_phone
USER_PHONE=your_phone_number
```

### 3. Run the Surveillance System
```bash
python surveillance.py
```

## File Structure
```
smart-surveillance/
│── surveillance.py        # Main script
│── requirements.txt       # Required dependencies
│── .env                   # Environment variables (excluded from Git)
│── .gitignore             # Ignore .env and other unnecessary files
│── README.md              # Project documentation
```

## Excluding `.env` from Git
Ensure your `.env` file is not uploaded by adding it to `.gitignore`:
```
.env
```
If you already committed `.env`, remove it from tracking:
```bash
git rm --cached .env
git commit -m "Removed .env from tracking"
git push origin main
```

## Future Enhancements
- **Live Video Streaming**: Add a feature to stream real-time video.
- **Email Alerts**: Send email notifications along with SMS and Telegram.
- **AI-Based Intruder Recognition**: Train a custom model to recognize known and unknown individuals.

