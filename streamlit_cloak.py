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
            

with col2:
    st.subheader("Step 2: Capture with Cloak")
    st.info("Hold colored cloth and take photo")
    cloak_file = st.camera_input("Take cloak photo", key="cloak_camera")
    
    if cloak_file is not None and st.session_state.background is None:
        st.warning("Please capture background first!")
        
st.markdown("---")
st.subheader("Step 3: Select Cloak Color")
color_col1, color_col2 = st.columns([2, 1])

with color_col1:
    st.session_state.cloak_color = st.selectbox(
        "Choose the color of your cloth:",
        ["white", "red", "blue", "green"],
        index=0
    )

with color_col2:
    st.markdown("")
    st.markdown("")
    if st.button("Clear & Restart"):
        st.session_state.background = None
        st.rerun()

if cloak_file is not None and st.session_state.background is not None:
    st.markdown("---")
    st.subheader("Result: Invisibility Effect")

    with st.spinner("Applying invisibility magic.."):
        cloak_img = Image.open(cloak_file).convert("RGB")
        frame = cv2.cvtColor(np.array(cloak_img), cv2.COLOR_RGB2BGR)
        
        bg = st.session_state.background
        if (bg.shape[1], bg.shape[0]) != (frame.shape[1], frame.shape[0]):
            bg = cv2.resize(bg, (frame.shape[1], frame.shape[0]))
        
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        
        color_ranges = {
            "white": {
                "lower1": np.array([0, 0, 200]),
                "upper1": np.array([180, 40, 255]),
                "lower2": None,
                "upper2": None
            },
            "red": {
                "lower1": np.array([0, 120, 70]),
                "upper1": np.array([10, 255, 255]),
                "lower2": np.array([170, 120, 70]),
                "upper2": np.array([180, 255, 255])
            },
            "blue": {
                "lower1": np.array([94, 80, 2]),
                "upper1": np.array([126, 255, 255]),
                "lower2": None,
                "upper2": None
            },
            "green": {
                "lower1": np.array([36, 50, 70]),
                "upper1": np.array([89, 255, 255]),
                "lower2": None,
                "upper2": None
            }
        }
    
        color_range = color_ranges[st.session_state.cloak_color]
        
        mask1 = cv2.inRange(hsv, color_range["lower1"], color_range["upper1"])
        if color_range["lower2"] is not None:
            mask2 = cv2.inRange(hsv, color_range["lower2"], color_range["upper2"])
            mask = cv2.bitwise_or(mask1, mask2)
        else:
            mask = mask1
        
        kernel = np.ones((5, 5), np.uint8)
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel, iterations=2)
        mask = cv2.morphologyEx(mask, cv2.MORPH_DILATE, kernel, iterations=1)
        mask = cv2.GaussianBlur(mask, (5, 5), 0)

        mask_inv = cv2.bitwise_not(mask)
        cloak_area = cv2.bitwise_and(bg, bg, mask=mask)
        rest = cv2.bitwise_and(frame, frame, mask=mask_inv)
        final = cv2.add(cloak_area, rest)
        
        result_col1, result_col2 = st.columns(2)
        
        with result_col1:
            st.markdown("**Original Photo**")
            st.image(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB), use_container_width=True)
        
        with result_col2:
            st.markdown("**Invisibility Effect**")
            st.image(cv2.cvtColor(final, cv2.COLOR_BGR2RGB), use_container_width=True)
        
        st.markdown("")
        result_rgb = cv2.cvtColor(final, cv2.COLOR_BGR2RGB)
        result_pil = Image.fromarray(result_rgb)
        buf = io.BytesIO()
        result_pil.save(buf, format="PNG")
        
        st.download_button(
            label="💾 Download Result",
            data=buf.getvalue(),
            file_name="invisibility_cloak_result.png",
            mime="image/png",
            type="primary"
        )
    
st.markdown("---")
status_col1, status_col2 = st.columns(2)
with status_col1:
    if st.session_state.background is not None:
        st.success("✅ Background: Captured")
    else:
        st.error("❌ Background: Not captured")

with status_col2:
    if cloak_file is not None:
        st.success("✅ Cloak Photo: Captured")
    else:
        st.error("❌ Cloak Photo: Not captured")

st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666; font-size: 0.9em;'>
    <p>🔬 Uses HSV color space detection and image masking for the invisibility effect</p>
</div>
""", unsafe_allow_html=True)
        
        
        
        