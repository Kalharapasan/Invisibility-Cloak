import sys

print("=" * 60)
print("INVISIBILITY CLOAK - SYSTEM DIAGNOSTIC")
print("=" * 60)

# Check Python version
print(f"\n1. Python Version: {sys.version}")
if sys.version_info < (3, 7):
    print("   WARNING: Python 3.7+ recommended")
else:
    print("   Python version OK")

# Check OpenCV
print("\n2. Checking OpenCV...")
try:
    import cv2
    print(f"   OpenCV installed: {cv2.__version__}")
except ImportError as e:
    print(f"   OpenCV NOT installed: {e}")
    print("   Install with: pip install opencv-python")

# Check NumPy
print("\n3. Checking NumPy...")
try:
    import numpy as np
    print(f"   NumPy installed: {np.__version__}")
except ImportError as e:
    print(f"   NumPy NOT installed: {e}")
    print("   Install with: pip install numpy")

# Check Streamlit (optional)
print("\n4. Checking Streamlit (for web app)...")
try:
    import streamlit as st
    print(f" Streamlit installed: {st.__version__}")
except ImportError:
    print(" Streamlit NOT installed (only needed for web version)")
    print(" Install with: pip install streamlit")


print("\n5. Checking Pillow (for web app)...")
try:
    from PIL import Image
    import PIL
    print(f"  Pillow installed: {PIL.__version__}")
except ImportError:
    print("    Pillow NOT installed (only needed for web version)")
    print("   Install with: pip install pillow")

# Test camera access
print("\n6. Testing Camera Access...")
try:
    import cv2
    cap = cv2.VideoCapture(0)
    if cap.isOpened():
        ret, frame = cap.read()
        if ret:
            print(f"   Camera working! Resolution: {frame.shape[1]}x{frame.shape[0]}")
        else:
            print("   Camera opened but can't read frames")
        cap.release()
    else:
        print("   Cannot open camera (index 0)")
        print("   Try different camera index (1, 2, etc.)")
        print("   Close other apps using the camera")
        print("   Check camera permissions")
except Exception as e:
    print(f"   Camera test failed: {e}")

# Check platform
import platform
print(f"\n7. Operating System: {platform.system()} {platform.release()}")

print("\n" + "=" * 60)
print("DIAGNOSTIC COMPLETE")
print("=" * 60)

# Recommendations
print("\n RECOMMENDATIONS:")
all_good = True
try:
    import cv2
    import numpy as np
except:
    all_good = False
    print("Install required packages:")
    print("   pip install opencv-python numpy")

if all_good:
    print("All required packages installed!")
    print("\n You can run the OpenCV version with:")
    print("   python invisibility_cloak.py")
    
try:
    import streamlit
    import PIL
    print("\n Web version packages installed!")
    print(" You can run the Streamlit version with:")
    print("   streamlit run streamlit_app.py")
except:
    pass

print("\n" + "=" * 60)