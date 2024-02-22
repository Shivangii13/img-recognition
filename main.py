import cv2
from cv2 import VideoCapture
from cv2 import waitKey
video_cap = cv2.videocapture(0)
while True: 
    ret , vedio = video_cap.read()
    cv2.imshow("video_live" , video_data)
    if cv2.waitkey(10)==ord("a"):
        break
video_cap.release()

    