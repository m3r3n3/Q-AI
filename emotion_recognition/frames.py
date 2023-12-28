# Importing all necessary libraries 
import cv2 
import os 
import math

# Read the video from specified path 
cam = cv2.VideoCapture("resume.mov") 

try: 
	
	# creating a folder named data 
	if not os.path.exists('data'): 
		os.makedirs('data') 

# if not created then raise error 
except OSError: 
	print ('Error: Creating directory of data') 
frameRate = cam.get(5)
# frame 
currentframe = 0

while(True): 
    frameId = cam.get(1)
    ret,frame = cam.read() 
    if(frameId % math.floor(frameRate) == 0):
	        # reading from frame 
            if ret: 
                # if video is still left continue creating images 
                name = './data/frame' + str(currentframe) + '.jpg'
                print ('Creating...' + name) 

                # writing the extracted images 
                cv2.imwrite(name, frame) 

                # increasing counter so that it will 
                # show how many frames are created 
                
            else: 
                break
    currentframe += 1

# Release all space and windows once done 
cam.release() 
cv2.destroyAllWindows() 
