###
# Python opencv operating video example.
# 
# License - MIT.
###

import os
from time import sleep

# pip install opencv-python
import cv2 as cv


# show_video - Show video frame.
def show_video(videoPath):
# {
    cap = cv.VideoCapture(videoPath)

    for i in range(500):
        ret, frame = cap.read()
        cv.imshow('video', frame)

        keycode = cv.waitKey(10)
        # ESC keycode is 27.
        if 27 == keycode:
            break

        sleep(0.01)

    cap.release()
# }


# Main function.
def main():
# {
    print('Press ESC to quit.')

    show_video(video_path)
# }


# Program entry.
if '__main__' == __name__:
# {
    # video path: 0 -->camera; Path --> video file.
    video_path = 0
    # video_path = "D:/catwalk.flv"

    main()
# }
