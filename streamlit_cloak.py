import streamlit as st
import cv2
import numpy as np
from PIL import Image
import io

st.set_page_config(page_title="Invisibility Cloak", layout="centered", page_icon="🧙")

st.title("🧙‍♂️ Invisibility Cloak Demo")
st.markdown("### Make yourself invisible with computer vision!")

with st.expander("ℹ️ How to Use", expanded=True):
    st.markdown("""
    **Step-by-step instructions:**
    
    1. **Capture Background**: Stand *completely out* of the camera frame and take a photo of the empty background
    2. **Capture Cloak Photo**: Hold a colored cloth (white, red, blue, or green) in front of you and take a photo
    3. **Select Color**: Choose the color of your cloth from the dropdown
    4. The app will make the cloth "invisible" by replacing it with the background!
    
    **Tips for best results:**
    - Use solid-colored cloth (white works best)
    - Ensure good lighting
    - Keep the background static between both photos
    - Make sure the cloth covers the area you want to make invisible
    """)

if "background" not in st.session_state:
    st.session_state.background = None
if "cloak_color" not in st.session_state:
    st.session_state.cloak_color = "white"

st.markdown("---")


with col1:
    st.subheader("📷 Step 1: Capture Background")
    st.info("Stand out of frame before capturing!")
    bg_file = st.camera_input("Take background photo", key="bg_camera")
    
    if bg_file is not None:
        if st.button("Set as Background", type="primary"):
            bg_img = Image.open(bg_file).convert("RGB")
            bg = cv2.cvtColor(np.array(bg_img), cv2.COLOR_RGB2BGR)
            st.session_state.background = bg
            st.success("Background captured!")
            st.balloons()
            
            