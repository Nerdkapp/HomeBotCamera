import json
from picamera import PiCamera
import cherrypy
import uuid

camera = PiCamera()

class HomeBotCamera(object):
    @cherrypy.expose
    @cherrypy.tools.json_out()
    def takePicture(self):
        fileName = str(uuid.uuid1()) + '.jpg';
        camera.capture('/home/pi/images/' + fileName)
        return {"image" : "/static/" + fileName}

if __name__ == '__main__':
    cherrypy.quickstart(HomeBotCamera(), '/', "app.conf")