import json
from picamera import PiCamera
import cherrypy
import io
import base64

camera = PiCamera()

class HomeBotCamera(object):
    @cherrypy.expose
    @cherrypy.tools.json_out()
    def takePicture(self):
    	camera.capture('/home/pi/images/camera.jpg')    	
        return {"image" : "/home/pi/images/camera.jpg"}

if __name__ == '__main__':
   cherrypy.quickstart(HomeBotCamera(), '/', "app.conf")	
