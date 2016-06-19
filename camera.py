# USAGE
# python motion_detector.py
# python motion_detector.py --video videos/example_01.mp4

# import the necessary packages
import argparse
import datetime
import imutils
import time
import cv2
import json
import urllib2
import requests

ACCESS_TOKEN = '226896590:AAEXOVKAHmR6zwxqdWMupOv_CLf7BjHMSRo'

def calcLastUpdateId(data):
	length = len(data['result'])
	if(length > 0):
		lastUpdateId = data['result'][length-1]['update_id']
		return lastUpdateId + 1;
	else:
		return 0;	

def retrieveMessages():
	return json.load(urllib2.urlopen("https://api.telegram.org/bot" + ACCESS_TOKEN + "/getUpdates"))		

camera = cv2.VideoCapture(0)
time.sleep(0.25)

# initialize the first frame in the video stream
firstFrame = None

data = retrieveMessages()
lastUpdateId = calcLastUpdateId(data)

# loop over the frames of the video
while True:
	#Wait for 5 seconds
	time.sleep(5)
	#Check if someone asked for the image
	data = json.load(urllib2.urlopen("https://api.telegram.org/bot226896590:AAEXOVKAHmR6zwxqdWMupOv_CLf7BjHMSRo/getUpdates?offset=" + str(lastUpdateId + 1)))
	# Calculate the next lastUpdateId

	if(data['result']):
		textMessage = data['result'][0]['message']['text']
	
		print(textMessage)
		if textMessage == "Come va?":
			# grab the current frame and initialize the occupied/unoccupied
			# text
			(grabbed, frame) = camera.read()

			cv2.imwrite('/Users/lcoccia/git/personal/motion-detector/image.jpg',frame)	
			#Send the image
			files = {'photo': open('/Users/lcoccia/git/personal/motion-detector/image.jpg', 'rb')}
			r = requests.post("https://api.telegram.org/bot226896590:AAEXOVKAHmR6zwxqdWMupOv_CLf7BjHMSRo/sendPhoto", files=files, data={'chat_id': 184011338})


	else:
		print('No new messages!')
			
# cleanup the camera and close any open windows
camera.release()
cv2.destroyAllWindows()

