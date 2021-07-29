import cv2
import numpy as np
import logging as log
import sys
import inspect
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

def get_gesture():
    try :
        with mp_hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.8) as hands :

            log.info(f"Getting video image")

            #Capture video from the first camera on computer.
            log.info(f"Getting video input from computer camera")
            video_capture = cv2.VideoCapture(0)

            '''
            Numbers and definitions for video_capture.set()
            3. CV_CAP_PROP_FRAME_WIDTH Width of the frames in the video stream.
            4. CV_CAP_PROP_FRAME_HEIGHT Height of the frames in the video stream.
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
                    log.info(f"Detecting nothing")
                    break
                
                #Flipping the image and changing the colours.
                image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
                log.debug(f"Flipped image and changed the colours")

                #Telling the computer that it can just use the reference image given.
                image.flags.writeable = False
                log.debug(f"Told the computer that it just has to use the original reference image")

                #Finding the hands in the frame.
                log.info(f"Finding the hands in the frame")
                results = hands.process(image)
                log.info(f"Found hands in the frame")

                #Telling the computer it can change the image given.
                image.flags.writeable = True

                if results.multi_hand_landmarks:
                    for hand_found in results.multi_hand_landmarks:
                        # log.debug(results.multi_hand_landmarks)
                        # log.debug(f"Got first hand")
                        # hand = results.multi_hand_landmarks[]
                        # log.debug(f"Drawing hand landmarks and lines")
                        # mp_drawing.draw_landmarks(image, hand, mp_hands.HAND_CONNECTIONS)
                        # hand_two = results.multi_hand_landmarks[1]
                        # mp_drawing.draw_landmarks(image, hand_two, mp_hands.HAND_CONNECTIONS)
                        mp_drawing.draw_landmarks(image, hand_found, mp_hands.HAND_CONNECTIONS)
                else:
                    log.info(f"Hand not found")

                log.info(f"Finished drawing hand landmarks and lines")


                log.debug(f"Showing video now")

                #Showing the video window 
                cv2.imshow('Video', image)

                #Destroying the window when q is pressed
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    video_capture.release()
                    cv2.destroyAllWindows()
                    log.info(f'Destroyed all windows')
                    
    except Exception as error:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        log.info(f"{inspect.stack()[0][3]} : {exc_tb.tb_lineno} : {error}")
        raise(error)
        

if __name__ == "__main__":
    try:
        log.basicConfig(format='%(asctime)s, %(lineno)d, %(message)s', level=log.DEBUG)
        log.info(f"Starting gesture_controller program")
        get_gesture()

    except Exception as error:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        log.info(f"{inspect.stack()[0][3]} : {exc_tb.tb_lineno} : {error}")

    finally:
        print(f":D")