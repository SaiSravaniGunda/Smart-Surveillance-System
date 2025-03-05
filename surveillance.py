import cv2
import time
import RPi.GPIO as GPIO
import telepot
from twilio.rest import Client
from picamera import PiCamera
import imutils
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# PIR Sensor Setup
PIR_PIN = 4  # GPIO pin for PIR sensor
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR_PIN, GPIO.IN)

# Camera Setup
camera = PiCamera()
camera.resolution = (640, 480)

# Load AI Face Recognition Model
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Load credentials from .env
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
TWILIO_SID = os.getenv("TWILIO_SID")
TWILIO_AUTH = os.getenv("TWILIO_AUTH")
TWILIO_PHONE = os.getenv("TWILIO_PHONE")
USER_PHONE = os.getenv("USER_PHONE")

def send_telegram_message(message, image_path=None):
    bot = telepot.Bot(TELEGRAM_BOT_TOKEN)
    bot.sendMessage(TELEGRAM_CHAT_ID, message)
    if image_path:
        bot.sendPhoto(TELEGRAM_CHAT_ID, open(image_path, "rb"))

def send_sms_notification(message):
    client = Client(TWILIO_SID, TWILIO_AUTH)
    client.messages.create(body=message, from_=TWILIO_PHONE, to=USER_PHONE)

def capture_image():
    image_path = f"/home/pi/surveillance_{int(time.time())}.jpg"
    camera.capture(image_path)
    return image_path

def detect_faces(image_path):
    image = cv2.imread(image_path)
    image = imutils.resize(image, width=500)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    
    if len(faces) > 0:
        print("Face detected!")
        send_telegram_message("🚨 Motion & Face Detected! Sending image...", image_path)
        send_sms_notification("🚨 Motion & Face Detected at your surveillance system!")
    else:
        print("No face detected, only motion.")

try:
    print("Monitoring for motion...")
    while True:
        if GPIO.input(PIR_PIN):
            print("Motion detected!")
            image_path = capture_image()
            detect_faces(image_path)  # AI Face Detection
            time.sleep(5)  # Avoid multiple detections
        time.sleep(1)

except KeyboardInterrupt:
    print("Exiting...")
    GPIO.cleanup()
