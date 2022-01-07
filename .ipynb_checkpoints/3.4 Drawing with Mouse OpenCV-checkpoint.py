### Check Python .py file and run it from there

import cv2
import numpy as np


############
# Function #
############

def draw_circle(event,x,y,flags,params):
    
    
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x,y),100, (0,255,0), -1)
    elif event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(img, (x,y),100, (0,0,255), -1)
        
cv2.namedWindow(winname='my_drawing')

cv2.setMouseCallback('my_drawing',draw_circle)

#############################
# Showing Image with OPENCV #
#############################

img = np.zeros((512,512,3),np.int8)

while True:
    
    cv2.imshow('my_drawing',img)
    
    if cv2.waitKey(1) & 0xFF == 27:
        break
        
cv2.destroyAllWindows()