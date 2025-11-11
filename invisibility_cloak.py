import cv2
import numpy as np
import sys
import platform
import time

CAM_INDEX = 0            
MIRROR = True            
WIN_NAME = "Enhanced Invisibility Cloak"
SHOW_HSV = False         
SHOW_OBJECT_DETECTION = True
CURRENT_COLORS = ["red"]  # Can now track multiple colors
MULTI_COLOR_MODE = False

BACKEND = cv2.CAP_DSHOW if platform.system() == "Windows" else 0

def nothing(_):
    pass

def init_hsv_window():
    win1 = "HSV Controls"
    win2 = "HSV Controls 2"

    cv2.namedWindow(win1, cv2.WINDOW_NORMAL)
    cv2.namedWindow(win2, cv2.WINDOW_NORMAL)
    try:
        cv2.resizeWindow(win1, 420, 560)
        cv2.moveWindow(win1, 100, 100)
        cv2.resizeWindow(win2, 420, 320)
        cv2.moveWindow(win2, 540, 100)
    except Exception:
        pass

    cv2.createTrackbar("H1 min", win1, 0, 180, nothing)
    cv2.createTrackbar("S1 min", win1, 120, 255, nothing)
    cv2.createTrackbar("V1 min", win1, 70, 255, nothing)
    cv2.createTrackbar("H1 max", win1, 10, 180, nothing)
    cv2.createTrackbar("S1 max", win1, 255, 255, nothing)
    cv2.createTrackbar("V1 max", win1, 255, 255, nothing)
    cv2.createTrackbar("H2 min", win2, 170, 180, nothing)
    cv2.createTrackbar("S2 min", win2, 120, 255, nothing)
    cv2.createTrackbar("V2 min", win2, 70, 255, nothing)
    cv2.createTrackbar("H2 max", win2, 180, 180, nothing)
    cv2.createTrackbar("S2 max", win2, 255, 255, nothing)
    cv2.createTrackbar("V2 max", win2, 255, 255, nothing)
    cv2.createTrackbar("Kernel", win2, 5, 15, nothing)
    cv2.createTrackbar("Dilate", win2, 2, 10, nothing)
    cv2.createTrackbar("Blur", win2, 5, 20, nothing)

COLOR_PRESETS = {
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
    },
    "yellow":{
        "r1": (20, 100, 100, 30, 255, 255),
        "r2": (0, 0, 0, 0, 0, 0),
        "kernel": 5, "dilate": 2, "blur": 5
    },
    "orange":{
        "r1": (10, 100, 100, 20, 255, 255),
        "r2": (0, 0, 0, 0, 0, 0),
        "kernel": 5, "dilate": 2, "blur": 5
    },
    "purple":{
        "r1": (130, 50, 50, 160, 255, 255),
        "r2": (0, 0, 0, 0, 0, 0),
        "kernel": 5, "dilate": 2, "blur": 5
    }
}
    
def set_preset(color):
    p = COLOR_PRESETS[color]
    H1min, S1min, V1min, H1max, S1max, V1max = p["r1"]
    H2min, S2min, V2min, H2max, S2max, V2max = p["r2"]
   
    cv2.setTrackbarPos("H1 min", "HSV Controls", H1min)
    cv2.setTrackbarPos("S1 min", "HSV Controls", S1min)
    cv2.setTrackbarPos("V1 min", "HSV Controls", V1min)
    cv2.setTrackbarPos("H1 max", "HSV Controls", H1max)
    cv2.setTrackbarPos("S1 max", "HSV Controls", S1max)
    cv2.setTrackbarPos("V1 max", "HSV Controls", V1max)
    
    cv2.setTrackbarPos("H2 min", "HSV Controls 2", H2min)
    cv2.setTrackbarPos("S2 min", "HSV Controls 2", S2min)
    cv2.setTrackbarPos("V2 min", "HSV Controls 2", V2min)
    cv2.setTrackbarPos("H2 max", "HSV Controls 2", H2max)
    cv2.setTrackbarPos("S2 max", "HSV Controls 2", S2max)
    cv2.setTrackbarPos("V2 max", "HSV Controls 2", V2max)

    cv2.setTrackbarPos("Kernel", "HSV Controls 2", p["kernel"])
    cv2.setTrackbarPos("Dilate", "HSV Controls 2", p["dilate"])
    cv2.setTrackbarPos("Blur", "HSV Controls 2", p["blur"])
    
def read_hsv_ranges():
    H1min = cv2.getTrackbarPos("H1 min", "HSV Controls")
    S1min = cv2.getTrackbarPos("S1 min", "HSV Controls")
    V1min = cv2.getTrackbarPos("V1 min", "HSV Controls")
    H1max = cv2.getTrackbarPos("H1 max", "HSV Controls")
    S1max = cv2.getTrackbarPos("S1 max", "HSV Controls")
    V1max = cv2.getTrackbarPos("V1 max", "HSV Controls")
    
    H2min = cv2.getTrackbarPos("H2 min", "HSV Controls 2")
    S2min = cv2.getTrackbarPos("S2 min", "HSV Controls 2")
    V2min = cv2.getTrackbarPos("V2 min", "HSV Controls 2")
    H2max = cv2.getTrackbarPos("H2 max", "HSV Controls 2")
    S2max = cv2.getTrackbarPos("S2 max", "HSV Controls 2")
    V2max = cv2.getTrackbarPos("V2 max", "HSV Controls 2")

    kernel = cv2.getTrackbarPos("Kernel", "HSV Controls 2")
    kernel = max(1, kernel)
    if kernel % 2 == 0:
        kernel += 1
    dilate_iter = max(0, cv2.getTrackbarPos("Dilate", "HSV Controls 2"))
    blur_val = max(0, cv2.getTrackbarPos("Blur", "HSV Controls 2"))

    lower1 = np.array([H1min, S1min, V1min])
    upper1 = np.array([H1max, S1max, V1max])
    lower2 = np.array([H2min, S2min, V2min])
    upper2 = np.array([H2max, S2max, V2max])

    return (lower1, upper1, lower2, upper2, kernel, dilate_iter, blur_val)

def create_color_mask(hsv, color):
    """Create mask for a specific color using presets"""
    p = COLOR_PRESETS[color]
    H1min, S1min, V1min, H1max, S1max, V1max = p["r1"]
    H2min, S2min, V2min, H2max, S2max, V2max = p["r2"]
    
    lower1 = np.array([H1min, S1min, V1min])
    upper1 = np.array([H1max, S1max, V1max])
    lower2 = np.array([H2min, S2min, V2min])
    upper2 = np.array([H2max, S2max, V2max])
    
    mask1 = cv2.inRange(hsv, lower1, upper1)
    mask2 = cv2.inRange(hsv, lower2, upper2)
    mask = cv2.bitwise_or(mask1, mask2)
    
    ksz = p["kernel"]
    if ksz % 2 == 0:
        ksz += 1
    kernel = np.ones((ksz, ksz), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel, iterations=1)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel, iterations=1)
    
    if p["dilate"] > 0:
        mask = cv2.dilate(mask, kernel, iterations=p["dilate"])
    
    if p["blur"] > 0:
        blur_size = p["blur"] * 2 + 1
        mask = cv2.GaussianBlur(mask, (blur_size, blur_size), 0)
    
    return mask

def detect_objects(frame, mask):
    """Detect objects in the mask and return their properties"""
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    objects = []
    
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 500:  # Minimum area threshold
            x, y, w, h = cv2.boundingRect(contour)
            center = (x + w//2, y + h//2)
            objects.append({
                'contour': contour,
                'area': area,
                'bbox': (x, y, w, h),
                'center': center
            })
    
    return objects

def draw_object_info(frame, objects, color_name):
    """Draw bounding boxes and information about detected objects"""
    color_map = {
        'red': (0, 0, 255),
        'blue': (255, 0, 0),
        'green': (0, 255, 0),
        'yellow': (0, 255, 255),
        'orange': (0, 165, 255),
        'purple': (255, 0, 255),
        'white': (255, 255, 255)
    }
    
    box_color = color_map.get(color_name, (0, 255, 0))
    
    for i, obj in enumerate(objects):
        x, y, w, h = obj['bbox']
        cv2.rectangle(frame, (x, y), (x+w, y+h), box_color, 2)
        
        label = f"{color_name.upper()} #{i+1}"
        area_text = f"Area: {int(obj['area'])}"
        
        cv2.putText(frame, label, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 
                   0.5, box_color, 2, cv2.LINE_AA)
        cv2.putText(frame, area_text, (x, y+h+20), cv2.FONT_HERSHEY_SIMPLEX, 
                   0.4, box_color, 1, cv2.LINE_AA)
        
        cv2.circle(frame, obj['center'], 5, box_color, -1)

print("Initializing camera...")

cap = cv2.VideoCapture(CAM_INDEX, BACKEND)
if not cap.isOpened():
    cap = cv2.VideoCapture(CAM_INDEX)
if not cap.isOpened():
    print("ERROR: Could not open webcam.")
    print("Try changing CAM_INDEX (0/1/2) or close other apps using the camera.")
    sys.exit(1)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
print("Camera initialized successfully!")

init_hsv_window()
set_preset(CURRENT_COLORS[0])
if not SHOW_HSV:
    try:
        cv2.destroyWindow("HSV Controls")
        cv2.destroyWindow("HSV Controls 2")
    except Exception:
        pass

background = None
font = cv2.FONT_HERSHEY_SIMPLEX
fps_start_time = time.time()
fps_counter = 0
fps_display = 0

print("\n=== ENHANCED INVISIBILITY CLOAK APPLICATION ===")
print("Controls:")
print("  [b] - Capture background")
print("  [1-7] - Color presets: 1=Red 2=Blue 3=Green 4=White 5=Yellow 6=Orange 7=Purple")
print("  [m] - Toggle Multi-Color Mode")
print("  [o] - Toggle Object Detection Overlay")
print("  [h] - Toggle HSV controls")
print("  [s] - Save current frame")
print("  [c] - Clear selected colors (in multi-color mode)")
print("  [q] - Quit")
print("\nStarting live feed...\n")

while True:
    ok, frame = cap.read()
    if not ok:
        print("Failed to read frame from camera.")
        break

    if MIRROR:
        frame = cv2.flip(frame, 1)

    display = frame.copy()
    
    fps_counter += 1
    if time.time() - fps_start_time >= 1.0:
        fps_display = fps_counter
        fps_counter = 0
        fps_start_time = time.time()
    
    mode_text = "MULTI" if MULTI_COLOR_MODE else "SINGLE"
    obj_text = "ON" if SHOW_OBJECT_DETECTION else "OFF"
    cv2.putText(display, f"Mode:{mode_text} ObjDet:{obj_text} | FPS:{fps_display}",
                (10, 25), font, 0.5, (255, 255, 255), 1, cv2.LINE_AA)

    if background is None:
        cv2.putText(display, "STEP 1: Clear the frame, then press [b] to capture background",
                    (10, 55), font, 0.6, (0, 255, 255), 2, cv2.LINE_AA)
        cv2.putText(display, "STEP 2: Wear colored cloth & press [1-7] | [m] for multi-color",
                    (10, 85), font, 0.6, (0, 255, 255), 2, cv2.LINE_AA)
        cv2.imshow(WIN_NAME, display)
        key = cv2.waitKey(1) & 0xFF
        
        if key == ord('q'):
            break
        elif key == ord('m'):
            MULTI_COLOR_MODE = not MULTI_COLOR_MODE
            print(f"Multi-color mode: {'ON' if MULTI_COLOR_MODE else 'OFF'}")
        elif key == ord('o'):
            SHOW_OBJECT_DETECTION = not SHOW_OBJECT_DETECTION
            print(f"Object detection: {'ON' if SHOW_OBJECT_DETECTION else 'OFF'}")
        elif key == ord('h'):
            SHOW_HSV = not SHOW_HSV
            if SHOW_HSV:
                init_hsv_window()
                set_preset(CURRENT_COLORS[0])
            else:
                try:
                    cv2.destroyWindow("HSV Controls")
                    cv2.destroyWindow("HSV Controls 2")
                except Exception:
                    pass
        elif key in (ord('1'), ord('2'), ord('3'), ord('4'), ord('5'), ord('6'), ord('7')):
            color_map = {'1':'red','2':'blue','3':'green','4':'white','5':'yellow','6':'orange','7':'purple'}
            selected_color = color_map[chr(key)]
            
            if MULTI_COLOR_MODE:
                if selected_color in CURRENT_COLORS:
                    CURRENT_COLORS.remove(selected_color)
                    print(f"Removed {selected_color}")
                else:
                    CURRENT_COLORS.append(selected_color)
                    print(f"Added {selected_color}")
                print(f"Active colors: {', '.join(CURRENT_COLORS)}")
            else:
                CURRENT_COLORS = [selected_color]
                SHOW_HSV = True
                init_hsv_window()
                set_preset(selected_color)
                print(f"Switched to {selected_color} preset")
        elif key == ord('c'):
            CURRENT_COLORS = []
            print("Cleared all colors")
        elif key == ord('b'):
            print("Capturing background in 3 seconds... Clear the frame!")
            for i in range(3, 0, -1):
                ok, temp = cap.read()
                if MIRROR:
                    temp = cv2.flip(temp, 1)
                temp_display = temp.copy()
                cv2.putText(temp_display, f"Capturing in {i}...", 
                           (frame.shape[1]//2 - 100, frame.shape[0]//2), 
                           font, 2, (0, 255, 255), 3, cv2.LINE_AA)
                cv2.imshow(WIN_NAME, temp_display)
                cv2.waitKey(1000)
            
            bg = None
            for _ in range(30):
                ok, temp_bg = cap.read()
                if not ok:
                    continue
                if MIRROR:
                    temp_bg = cv2.flip(temp_bg, 1)
                bg = temp_bg
            if bg is None:
                print("ERROR: Failed to capture background from camera.")
            else:
                background = bg.copy()
                print("Background captured successfully!")
        continue
    
    # Main processing with background
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    if not CURRENT_COLORS:
        cv2.putText(display, "No colors selected! Press [1-7] to select colors",
                    (10, 55), font, 0.7, (0, 0, 255), 2, cv2.LINE_AA)
        cv2.imshow(WIN_NAME, display)
    else:
        # Create combined mask for all selected colors
        combined_mask = np.zeros(frame.shape[:2], dtype=np.uint8)
        all_objects = []
        
        for color in CURRENT_COLORS:
            color_mask = create_color_mask(hsv, color)
            combined_mask = cv2.bitwise_or(combined_mask, color_mask)
            
            if SHOW_OBJECT_DETECTION:
                objects = detect_objects(frame, color_mask)
                for obj in objects:
                    obj['color'] = color
                all_objects.extend(objects)
        
        mask_inv = cv2.bitwise_not(combined_mask)
        
        cloak_area = cv2.bitwise_and(background, background, mask=combined_mask)
        rest = cv2.bitwise_and(frame, frame, mask=mask_inv)
        output = cv2.add(cloak_area, rest)
        
        if SHOW_OBJECT_DETECTION and all_objects:
            for obj in all_objects:
                draw_object_info(output, [obj], obj['color'])
            
            cv2.putText(output, f"Objects detected: {len(all_objects)}", 
                       (10, frame.shape[0] - 20), font, 0.6, (0, 255, 0), 2, cv2.LINE_AA)
        
        colors_text = ', '.join([c.upper() for c in CURRENT_COLORS])
        cv2.putText(output, f"Active: {colors_text}",
                    (10, 55), font, 0.6, (0, 255, 0), 2, cv2.LINE_AA)
        
        cv2.imshow(WIN_NAME, output)
        key = cv2.waitKey(1) & 0xFF
    
    if key == ord('q'):
        print("Exiting...")
        break
    elif key == ord('m'):
        MULTI_COLOR_MODE = not MULTI_COLOR_MODE
        print(f"Multi-color mode: {'ON' if MULTI_COLOR_MODE else 'OFF'}")
    elif key == ord('o'):
        SHOW_OBJECT_DETECTION = not SHOW_OBJECT_DETECTION
        print(f"Object detection: {'ON' if SHOW_OBJECT_DETECTION else 'OFF'}")
    elif key == ord('h'):
        SHOW_HSV = not SHOW_HSV
        if SHOW_HSV:
            init_hsv_window()
            set_preset(CURRENT_COLORS[0] if CURRENT_COLORS else 'red')
        else:
            try:
                cv2.destroyWindow("HSV Controls")
                cv2.destroyWindow("HSV Controls 2")
            except Exception:
                pass
    elif key in (ord('1'), ord('2'), ord('3'), ord('4'), ord('5'), ord('6'), ord('7')):
        color_map = {'1':'red','2':'blue','3':'green','4':'white','5':'yellow','6':'orange','7':'purple'}
        selected_color = color_map[chr(key)]
        
        if MULTI_COLOR_MODE:
            if selected_color in CURRENT_COLORS:
                CURRENT_COLORS.remove(selected_color)
                print(f"Removed {selected_color}")
            else:
                CURRENT_COLORS.append(selected_color)
                print(f"Added {selected_color}")
            print(f"Active colors: {', '.join(CURRENT_COLORS)}")
        else:
            CURRENT_COLORS = [selected_color]
            SHOW_HSV = True
            init_hsv_window()
            set_preset(selected_color)
            print(f"Switched to {selected_color} preset")
    elif key == ord('c'):
        CURRENT_COLORS = []
        print("Cleared all colors")
    elif key == ord('b'):
        print("Recapturing background in 3 seconds...")
        for i in range(3, 0, -1):
            ok, temp = cap.read()
            if MIRROR:
                temp = cv2.flip(temp, 1)
            temp_display = temp.copy()
            cv2.putText(temp_display, f"Capturing in {i}...", 
                       (frame.shape[1]//2 - 100, frame.shape[0]//2), 
                       font, 2, (0, 255, 255), 3, cv2.LINE_AA)
            cv2.imshow(WIN_NAME, temp_display)
            cv2.waitKey(1000)
        
        bg = None
        for _ in range(30):
            ok, temp_bg = cap.read()
            if not ok:
                continue
            if MIRROR:
                temp_bg = cv2.flip(temp_bg, 1)
            bg = temp_bg
        if bg is None:
            print("ERROR: Failed to recapture background from camera.")
        else:
            background = bg.copy()
            print("Background recaptured!")
    elif key == ord('s'):
        filename = f"invisibility_cloak_{int(time.time())}.jpg"
        cv2.imwrite(filename, output if background else display)
        print(f"Saved frame as {filename}")

cap.release()
cv2.destroyAllWindows()
print("Application closed successfully!")