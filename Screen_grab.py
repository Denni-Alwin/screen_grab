import numpy as np
from PIL import ImageGrab
import cv2


while(True):
   # 1280x720 windowed mode
   printscreen =  np.array(ImageGrab.grab(bbox=(5,5,1280,720)))
   cv2.imshow('window',cv2.cvtColor(printscreen, cv2.COLOR_BGR2RGB))
   if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break


