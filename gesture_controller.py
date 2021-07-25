import cv2
import numpy as np
import logging as log
import sys
import inspect

def get_gesture():
    log.info(f"Getting video image")

    #Capture video from the first camera on computer.
    log.info(f"Getting video input from computer camera")
    video_capture = cv2.VideoCapture(0)

    '''
    Numbers and definitions for video_capture.set()

    0. CV_CAP_PROP_POS_MSEC Current position of the video file in milliseconds.
    1. CV_CAP_PROP_POS_FRAMES 0-based index of the frame to be decoded/captured next.
    2. CV_CAP_PROP_POS_AVI_RATIO Relative position of the video file
    3. CV_CAP_PROP_FRAME_WIDTH Width of the frames in the video stream.
    4. CV_CAP_PROP_FRAME_HEIGHT Height of the frames in the video stream.
    5. CV_CAP_PROP_FPS Frame rate.
    6. CV_CAP_PROP_FOURCC 4-character code of codec.
    7. CV_CAP_PROP_FRAME_COUNT Number of frames in the video file.
    8. CV_CAP_PROP_FORMAT Format of the Mat objects returned by retrieve() .
    9. CV_CAP_PROP_MODE Backend-specific value indicating the current capture mode.
    10. CV_CAP_PROP_BRIGHTNESS Brightness of the image (only for cameras).
    11. CV_CAP_PROP_CONTRAST Contrast of the image (only for cameras).
    12. CV_CAP_PROP_SATURATION Saturation of the image (only for cameras).
    13. CV_CAP_PROP_HUE Hue of the image (only for cameras).
    14. CV_CAP_PROP_GAIN Gain of the image (only for cameras).
    15. CV_CAP_PROP_EXPOSURE Exposure (only for cameras).
    16. CV_CAP_PROP_CONVERT_RGB Boolean flags indicating whether images should be converted to RGB.
    17. CV_CAP_PROP_WHITE_BALANCE Currently unsupported
    18. CV_CAP_PROP_RECTIFICATION Rectification flag for stereo cameras (note: only supported by DC1394 v 2.x backend currently)
    '''
    #Setting height and width for window that will display.
    log.info(f"Setting dimensions of the window to be diplayed. It is a rectangle")
    video_capture.set(3, 640)
    video_capture.set(4, 480)

    #Checking that the video has been initialized.
    log.info(f"making sure video is being captured and is working")
    while video_capture.isOpened():

        #Checking if the image capture has worked and the frame/image.
        success, image = video_capture.read()

        #If the video isnt wotking, it will return an error message
        if not success:
            log.info(f"Video isn't working")
            break

        log.debug(f"Showing video now")

        #Showing the video window 
        cv2.imshow('Video', image)

        #Destroying the window when q is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            video_capture.release()
            cv2.destroyAllWindows()
            log.info(f'Destroyed all windows')


if __name__ == "__main__":
    try:
        log.basicConfig(format='%(asctime)s, %(lineno)d, %(message)s', level=log.INFO)
        log.info(f"Starting gesture_controller program")
        get_gesture()

    except Exception as error:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        log.info(f"{inspect.stack()[0][3]} : {exc_tb.tb_lineno} : {error}")

    finally:
        print(f":D")