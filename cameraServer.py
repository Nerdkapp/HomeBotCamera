import cv2
import json
from picamera.array import PiRGBArray
from picamera import PiCamera
from flask import Flask

camera = PiCamera()
app = Flask(__name__)


@app.route('/')
def hello_world():
	camera.capture('image.jpg')
    return 'Hello, World!'