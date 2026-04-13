import cv2

class VideoCapture:
    def __init__(self, source=0):
        self.cap = cv2.VideoCapture(source)

    def get_frame(self):
        ret, frame = self.cap.read()
        return frame if ret else None

    def show(self, frame):
        cv2.imshow("Taekwondo Analyzer", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            exit()