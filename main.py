# Importing all required packages
import cv2
import numpy as np
import matplotlib.pyplot as plt 


# Read in the cascade classifiers for face and eyes
face_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_eye.xml')


# create a function to detect face
def adjusted_detect_face(img):
	
	face_img = img.copy()
	
	face_rect = face_cascade.detectMultiScale(face_img, 
											scaleFactor = 1.2, 
											minNeighbors = 5)
	
	for (x, y, w, h) in face_rect:
		cv2.rectangle(face_img, (x, y), 
					(x + w, y + h), (255, 255, 255), 10)\
		
	return face_img

# create a function to detect eyes
def detect_eyes(img):
	
	eye_img = img.copy() 
	eye_rect = eye_cascade.detectMultiScale(eye_img, 
											scaleFactor = 1.2, 
											minNeighbors = 5) 
	for (x, y, w, h) in eye_rect:
		cv2.rectangle(eye_img, (x, y), 
					(x + w, y + h), (255, 255, 255), 10)	 
	return eye_img


# define a video capture object 
vid = cv2.VideoCapture(0)

while(True): 
	
	# Capture the video frame 
	# by frame 
    ret, frame = vid.read()
	
    # Detecting the face 
    face = adjusted_detect_face(frame)

	# Display the resulting frame 
    cv2.imshow('face frame', adjusted_detect_face(frame)) 
	
	# the 'q' button is set as the 
	# quitting button you may use any 
	# desired button of your choice 
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break

# After the loop release the cap object 
vid.release() 
# Destroy all the windows 
cv2.destroyAllWindows() 
