import cv2
import numpy as np
import sys
import platform
import time

CAM_INDEX = 0            
MIRROR = True            
WIN_NAME = "Invisibility Cloak"
SHOW_HSV = False         
CURRENT_COLOR = "red"    

BACKEND = cv2.CAP_DSHOW if platform.system() == "Windows" else 0