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

def nothing(_):
    pass

def init_hsv_window():
    cv2.namedWindow("HSV Controls", cv2.WINDOW_AUTOSIZE)
    cv2.createTrackbar("H1 min", "HSV Controls", 0, 180, nothing)
    cv2.createTrackbar("S1 min", "HSV Controls", 120, 255, nothing)
    cv2.createTrackbar("V1 min", "HSV Controls", 70, 255, nothing)
    cv2.createTrackbar("H1 max", "HSV Controls", 10, 180, nothing)
    cv2.createTrackbar("S1 max", "HSV Controls", 255, 255, nothing)
    cv2.createTrackbar("V1 max", "HSV Controls", 255, 255, nothing)
    cv2.createTrackbar("H2 min", "HSV Controls", 170, 180, nothing)
    cv2.createTrackbar("S2 min", "HSV Controls", 120, 255, nothing)
    cv2.createTrackbar("V2 min", "HSV Controls", 70, 255, nothing)
    cv2.createTrackbar("H2 max", "HSV Controls", 180, 180, nothing)
    cv2.createTrackbar("S2 max", "HSV Controls", 255, 255, nothing)
    cv2.createTrackbar("V2 max", "HSV Controls", 255, 255, nothing)
    cv2.createTrackbar("Kernel", "HSV Controls", 3, 15, nothing)
    cv2.createTrackbar("Dilate", "HSV Controls", 1, 10, nothing)
    cv2.createTrackbar("Blur", "HSV Controls", 0, 20, nothing)