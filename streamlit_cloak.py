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

def set_preset(color):
    presets = {
        "red":  {
            "r1": (0, 120, 70, 10, 255, 255),
            "r2": (170, 120, 70, 180, 255, 255),
            "kernel": 5, "dilate": 2, "blur": 5
        },
        "blue": {
            "r1": (94, 80, 2, 126, 255, 255),
            "r2": (0, 0, 0, 0, 0, 0),
            "kernel": 5, "dilate": 2, "blur": 5
        },
        "green":{
            "r1": (36, 50, 70, 89, 255, 255),
            "r2": (0, 0, 0, 0, 0, 0),
            "kernel": 5, "dilate": 2, "blur": 5
        },
        "white":{
            "r1": (0, 0, 200, 180, 40, 255),
            "r2": (0, 0, 0, 0, 0, 0),
            "kernel": 5, "dilate": 2, "blur": 5
        }
    }
    p = presets[color]
    H1min, S1min, V1min, H1max, S1max, V1max = p["r1"]
    H2min, S2min, V2min, H2max, S2max, V2max = p["r2"]
    cv2.setTrackbarPos("H1 min", "HSV Controls", H1min)
    cv2.setTrackbarPos("S1 min", "HSV Controls", S1min)
    cv2.setTrackbarPos("V1 min", "HSV Controls", V1min)
    cv2.setTrackbarPos("H1 max", "HSV Controls", H1max)
    cv2.setTrackbarPos("S1 max", "HSV Controls", S1max)
    cv2.setTrackbarPos("V1 max", "HSV Controls", V1max)

    cv2.setTrackbarPos("H2 min", "HSV Controls", H2min)
    cv2.setTrackbarPos("S2 min", "HSV Controls", S2min)
    cv2.setTrackbarPos("V2 min", "HSV Controls", V2min)
    cv2.setTrackbarPos("H2 max", "HSV Controls", H2max)
    cv2.setTrackbarPos("S2 max", "HSV Controls", S2max)
    cv2.setTrackbarPos("V2 max", "HSV Controls", V2max)

    cv2.setTrackbarPos("Kernel", "HSV Controls", p["kernel"])
    cv2.setTrackbarPos("Dilate", "HSV Controls", p["dilate"])
    cv2.setTrackbarPos("Blur", "HSV Controls", p["blur"])
