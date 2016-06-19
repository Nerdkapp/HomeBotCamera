import json
from picamera import PiCamera
import cherrypy

camera = PiCamera()

class HelloWorld(object):
    @cherrypy.expose
    def index(self):
    	camera.capture('image.jpg')
        return "Hello world!"

if __name__ == '__main__':
   cherrypy.quickstart(HelloWorld())