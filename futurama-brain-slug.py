import sys
import cv2
import numpy as np

window_name = "Brain Slug"
cv2.namedWindow(window_name,cv2.WINDOW_AUTOSIZE)

brain_slug = cv2.imread("brain_slug.png")

cap = cv2.VideoCapture(0)

if(cap.isOpened() != True):
  print >> sys.stderr, "Failed to open webcam!"
  sys.exit(1)

print type(brain_slug).__name__ + "  " + type(cap).__name__

while(1):
  #read curr frame and grayscale it
  ret,frame = cap.read()
  fgray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

  brain_slug = cv2.resize(brain_slug,tuple(reversed(frame.shape[:2])))

  print str(brain_slug.shape)+" : "+str(frame.shape)
  display = cv2.add(brain_slug,frame)

  #show on window
  cv2.imshow(window_name,display)

  #to exit window
  if cv2.waitKey(10) == 27:
    break

#clean up
cv2.destroyAllWindows()
cap.release()
