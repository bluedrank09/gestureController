import cv2
import numpy as np
import logging as log
import sys
import inspect
import mediapipe as mp
import math
import PySimpleGUI as psg

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
                log.debug(f"Finding the hands in the frame")
                results = hands.process(image)
                log.debug(f"Found hands in the frame")

                #Telling the computer it can change the image given.
                image.flags.writeable = True

                #creating two lists for the coordinates for the landmarks in each hand
                coordinates_landmark_hand_one = []
                coordinates_landmark_hand_two = []

                if results.multi_hand_landmarks:
                    #processing hands detected 
                    for index, hand_found in enumerate(results.multi_hand_landmarks):
                        image_height, image_width, image_channel = image.shape

                        #Getting normalized coordinates and getting real coordinates for each hand
                        for id, landmark in enumerate(hand_found.landmark):
                            x_position, y_postition = int(landmark.x * image_width), int(landmark.x * image_height)

                            #Appending to each hand
                            log.debug(f"The index is {index}")

                            if index == 0:
                                coordinates_landmark_hand_one.append([id, x_position, y_postition])
                                log.debug(f"Appended to list one")
                            else:
                                coordinates_landmark_hand_two.append([id, x_position, y_postition])
                                log.debug(f"Appeneded to list two")

                        #Drawing landmarks
                        mp_drawing.draw_landmarks(image, hand_found, mp_hands.HAND_CONNECTIONS)

                        log.debug(f"Length of coordinates list one is {len(coordinates_landmark_hand_one)}")
                        log.debug(f"Length of coordinates list two is {len(coordinates_landmark_hand_two)}")

                        if len(coordinates_landmark_hand_one) != 0 and len(coordinates_landmark_hand_two) != 0:
                            log.debug(f"Calculating coordinates distaces between the two hands")
                            log.debug(f"The distance between the coords is {math.dist(coordinates_landmark_hand_one[4], coordinates_landmark_hand_two[8])}")

                            if math.dist(coordinates_landmark_hand_one[8], coordinates_landmark_hand_two[4]) in range(0, 20):
                                log.info("A")

                            if math.dist(coordinates_landmark_hand_one[8], coordinates_landmark_hand_two[8]) in range(0, 10):
                                log.info(f"E")

                            if math.dist(coordinates_landmark_hand_one[8], coordinates_landmark_hand_two[12]) in range(0, 10):
                                log.info(f"I")

                            if math.dist(coordinates_landmark_hand_one[8], coordinates_landmark_hand_two[16]) in range(0, 10):
                                log.info(f"O")

                            if math.dist(coordinates_landmark_hand_one[8], coordinates_landmark_hand_two[20]) in range(0,10):
                                log.info(f"U")

                else:
                    log.debug(f"Hand not found")

                log.debug(f"Finished drawing hand landmarks and lines")


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

    except Exception as error:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        log.info(f"{inspect.stack()[0][3]} : {exc_tb.tb_lineno} : {error}")
        raise(error)
        

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