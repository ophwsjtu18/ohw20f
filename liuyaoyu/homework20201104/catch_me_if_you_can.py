# This is the implementation of a game "Hit the mouse"

import cv2
import random
import numpy as np

background = np.zeros((750,625,3),np.uint8)
mice = cv2.imread("mouse.jpg")
mouse_head = mice.copy()

success = 0  # Number of success hits
total = 0

has_image = [[0,0,0],[0,0,0],[0,0,0]] # Records whether an image appears at some place

# Returns the position of the mouse click
def check_hit(event,x,y,flags,param):
    global has_image
    global success
    if event == cv2.EVENT_LBUTTONDOWN:
        if has_image[int(x/150)-1][int(y/125)-1] == 1:
            print("Successful hit at:",x," ",y)
            success = success+ 1
            has_image[int(x/150)-1][int(y/125)-1] = 0  # In case multiple clicks at one point

while(True):
    bg = background.copy()
    # draw a rectangle to mark the boundaries
    for x in [150, 300, 450]:
        for y in [125, 250, 375]:
            cv2.rectangle(bg,(x,y),(x+150,y+125),(0,0,255),3)
    # Reset the flag list
    for x in [0,1,2]:
        for y in [0,1,2]:
            has_image[x][y] = 0
    # Generate pictures at random
    for x in [1,2,3]:
        for y in [1,2,3]:
            if random.randint(0,8)>5:
                bg[(125*x):(125*x+125),(150*y):(150*y+150)] = mouse_head
                total = total + 1
                has_image[y-1][x-1] = 1
    # Print the results
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(bg, 'Hits= '+str(success), (10, 100), font, 1, (255,255,255),2)
    
    cv2.imshow("Hit the mouse", bg)
    cv2.setMouseCallback('Hit the mouse', check_hit)  # Bind the function with the window
    # Break if 'q' is pressed
    if cv2.waitKey(2000)&0xFF == ord('q'):
        break

cv2.destroyAllWindows()  
print("Number of hits: ", success)
print("Total Mice: ", total)
print("Accuracy: ", success/total)
