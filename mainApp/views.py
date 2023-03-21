from django.shortcuts import render
from datetime import datetime
import cv2,threading
from django.views.decorators import gzip
from django.http import StreamingHttpResponse
from .visionHandler import Vision
# Create your views here.

cam = None

def index(req):
    global cam
    if cam!=None:
        del cam
    return render(req,"index.html")

@gzip.gzip_page
def use(req):
    try:
        global cam
        cam = VideoCamera()
        # cam = Vision()
        # cam.VisonApplier()
        return StreamingHttpResponse(gen(cam), content_type="multipart/x-mixed-replace;boundary=frame")
    except Exception as e:
        print(e)
    return render(req,"useCase.html")

class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)
        (self.grabbed,self.frame) = self.video.read()
        threading.Thread(target=self.update,args=()).start()

    def __del__(self):
        self.video.release()
        print("yes")

    def get_frame(self):
        img = self.frame
        _,jpg =cv2.imencode('.jpg', img)
        return jpg.tobytes()

    def update(self):
        while True:
            (self.grabbed,self.frame) = self.video.read()
            self.frame = cv2.flip(self.frame,1)

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')