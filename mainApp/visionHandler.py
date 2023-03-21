import cv2, os
from cvzone import FPS, overlayPNG
from cvzone.FaceMeshModule import FaceMeshDetector
from .imagePreprocessing import readTransfromImages

class Vision:
    """
    This is a Advanced Computer Vision class to add png images to a Face
    """
    def __init__(self, detectionCon = 0.85,camNo = 0,
                 wCam = 1280, hCam = 720, fps= 80, brightness = 150, focus = 20, showFPS = True, FPScolor = (255, 0, 255), ImageName = "Image"):
        """
        This initializes the object of Visions class and sets all the utility and main Parameters
        :param detectionCon: this sets the minDetectionCon for the input camera
        :param camNo: this sets the index for the input camera
        :param wCam: this sets the width of the output image
        :param hCam: this sets the height of the output image
        :param fps: this sets the FPS of the output video image 
        :param brightness: this sets the brightness of the output image 
        :param focus: this sets the focus threshold of the output image 
        :param showFPS: will show fps if true.
        :param FPScolor: will set the color of the fps shown
        :param ImageName: sets the name of the output Image Window
        """
        self.camNo = camNo
        self.wCam = wCam
        self.hCam = hCam
        self.fps = fps
        self.brightness = brightness
        self.focus = focus
        self.showFPS = showFPS 
        self.FPScolor = FPScolor
        self.ImageName = ImageName
        self.detectionCon = detectionCon

        self.cap = cv2.VideoCapture(self.camNo)
        self.cap.set(3, self.wCam)
        self.cap.set(4, self.hCam)
        self.cap.set(cv2.CAP_PROP_FPS, self.fps)
        self.cap.set(10, self.brightness)
        self.cap.set(28, self.focus)

        readTransfromImages()

        self.CameraFPS = FPS()

        self.detector = FaceMeshDetector(minDetectionCon = self.detectionCon)

    def displayPNG(self,img, imgPath = f"{os.path.abspath(os.path.dirname(__file__))}\\imgs\\toungue.png", size = [140, 128], pos = [0, 0], posMinus = [40, 30]):
                    """
                    This function makes an png overlay on an img with adjusting the size and position
                    :return img along with overlayed PNG
                    """
                    png = cv2.imread(imgPath, cv2.IMREAD_UNCHANGED)
                    if size != [-1, -1]:
                        png = cv2.resize(png, size)
                    img = overlayPNG(img, png, [pos[0] - posMinus[0], pos[1] - posMinus[1]])
                    return img
    
    @staticmethod
    def getImagePath(imgName):
        """
        :return a Path to the Image
        """
        return f"{os.path.abspath(os.path.dirname(__file__))}\\imgs\\{imgName}"

    def VisonApplier(self, index = 0):
        """
        This function applies all the changes to the image
        """
        while True:
            try:
                success, img = self.cap.read()
                if success:
                    
                    img = cv2.flip(img, 1)

                    img, faces = self.detector.findFaceMesh(img, draw = False)
                    if faces:
                        try:
                            match index:
                                 case 0:
                                      i=14
                                      img = self.displayPNG(img,pos = [faces[0][i][0], faces[0][i][1]])
                                 case 1:
                                    i=54
                                    img = self.displayPNG(img, imgPath = self.getImagePath("beard.png"), pos = [faces[0][i][0], faces[0][i][1]], size = [380, 350], posMinus = [90, 50])
                                 case 2:
                                    i=162
                                    img = self.displayPNG(img, imgPath = self.getImagePath("cartoon-specs.png"), pos = [faces[0][i][0], faces[0][i][1]], size = [250, 200], posMinus = [10, 50])

                                 case _:
                                      pass
                        except Exception as e:
                            continue

                    if self.showFPS:
                        self.CameraFPS.update(img, color = self.FPScolor)

                    self.img = img
                    print("running")
                else:
                    print("Some Error Occured")
                    break
            except Exception as e:
                print(e)
                break

    def __del__(self):
        self.cap.release()

    def get_frame(self):
        _,jpg =cv2.imencode('.jpg', self.img)
        return jpg.tobytes()

def main():
    vision = Vision(ImageName = "VipulSnapper")
    vision.VisonApplier()

if __name__ == "__main__":
    main()