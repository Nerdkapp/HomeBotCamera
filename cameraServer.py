import json
from picamera import PiCamera
import cherrypy

camera = PiCamera()

class HomeBotCamera(object):
    @cherrypy.expose
    @cherrypy.tools.json_out()
    def takePicture(self):
    	response = {}
    	stream = io.BytesIO()
    	camera.capture(stream, 'jpeg')
        return {"image" : stream.readall()}

if __name__ == '__main__':
   cherrypy.quickstart(HomeBotCamera())