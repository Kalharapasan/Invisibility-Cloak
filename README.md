"# Invisibility Cloak 🧙‍♂️✨

[![Python Version](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.0+-green.svg)](https://opencv.org/)
[![License](https://img.shields.io/badge/license-MIT-orange.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey.svg)]()

A real-time computer vision application that creates a magical invisibility cloak effect using OpenCV and Python. Hide behind any colored cloth and watch yourself disappear like magic! Inspired by Harry Potter's invisibility cloak, this project demonstrates advanced image processing techniques including color detection, masking, and background subtraction.

![Invisibility Cloak Demo](https://img.shields.io/badge/Status-Working-success)

## 🌟 Features

- ✨ **Real-time Invisibility Effect**: Uses advanced color detection and background subtraction to create a convincing invisibility effect at 30 FPS
- 🎨 **Multiple Color Presets**: Support for Red, Blue, Green, and White colored cloaks with optimized HSV ranges
- 🎛️ **Live HSV Controls**: Adjust color detection parameters in real-time with interactive trackbars for perfect tuning
- 📊 **FPS Counter**: Monitor application performance in real-time
- 📷 **Background Capture**: Easy background capture with 3-second countdown timer
- 💾 **Frame Saving**: Save your invisible moments as high-quality JPG images with timestamps
- 🪞 **Mirror Mode**: Flip the camera view for easier interaction and more natural experience
- 🔧 **Advanced Morphological Operations**: Kernel adjustments, dilation, and Gaussian blur for smooth edges
- 🖥️ **Cross-Platform**: Works on Windows, Linux, and macOS
- ⚡ **Optimized Performance**: Efficient processing for smooth real-time operation
- 🎭 **Dual HSV Range**: Supports two HSV ranges for better color detection (especially useful for red colors)
- 🛠️ **Diagnostic Tools**: Built-in system check and troubleshooting utilities

## 🎯 How It Works

The invisibility cloak effect is achieved through:

1. **Background Capture**: Captures the scene without the subject
2. **Color Detection**: Uses HSV color space to detect the colored cloth
3. **Mask Creation**: Creates a binary mask of the detected color region
4. **Background Replacement**: Replaces the masked region with the captured background
5. **Morphological Operations**: Smooths and refines the mask using kernel operations, dilation, and blur

## 📋 Prerequisites

- Python 3.7 or higher
- Webcam or external camera
- Colored cloth (red, blue, green, or white)
- Good lighting conditions
- 4GB RAM (minimum)
- Windows 10/11, Ubuntu 18.04+, or macOS 10.14+

### Required Python Packages
- OpenCV (cv2) >= 4.0
- NumPy >= 1.19
- Platform (built-in)
- Time (built-in)
- Sys (built-in)

## 🔧 Installation

1. Clone the repository:
```bash
git clone https://github.com/Kalharapasan/Invisibility-Cloak.git
cd Invisibility-Cloak
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

## 🚀 Usage

### Basic Usage

Run the main application:
```bash
python invisibility_cloak.py
```

### Streamlit Version (Optional)

For a web-based interface:
```bash
streamlit run streamlit_cloak.py
```

### Step-by-Step Guide

1. **Clear the Frame**: Remove yourself from the camera view
2. **Capture Background**: Press `[b]` to capture the background (3-second countdown)
3. **Wear Your Cloak**: Put on a colored cloth (red, blue, green, or white)
4. **Select Color Preset**: 
   - Press `[1]` for Red
   - Press `[2]` for Blue
   - Press `[3]` for Green
   - Press `[4]` for White
5. **Fine-tune (Optional)**: Press `[h]` to toggle HSV control windows for precise color detection
6. **Enjoy**: Watch yourself disappear!

## ⌨️ Keyboard Controls

| Key | Action |
|-----|--------|
| `b` | Capture/Recapture background |
| `1` | Switch to Red color preset |
| `2` | Switch to Blue color preset |
| `3` | Switch to Green color preset |
| `4` | Switch to White color preset |
| `h` | Toggle HSV control windows |
| `s` | Save current frame as image |
| `q` | Quit application |

## 🎨 HSV Control Parameters

When you press `[h]`, two control windows appear:

### HSV Controls Window
- **H1/H2 min/max**: Hue range (0-180)
- **S1/S2 min/max**: Saturation range (0-255)
- **V1/V2 min/max**: Value/Brightness range (0-255)

### Additional Controls
- **Kernel**: Size of morphological operation kernel (odd numbers)
- **Dilate**: Number of dilation iterations for mask expansion
- **Blur**: Gaussian blur strength for smoother edges

## 🎭 Color Presets

### Red (Default) 🔴
- **Range 1**: H(0-10), S(120-255), V(70-255)
- **Range 2**: H(170-180), S(120-255), V(70-255)
- **Kernel**: 5, **Dilate**: 2, **Blur**: 5
- **Best for**: Red cloth, fabric, blankets, or scarves
- **Note**: Red requires two HSV ranges because it wraps around the hue spectrum

### Blue 🔵
- **Range**: H(94-126), S(80-255), V(2-255)
- **Kernel**: 5, **Dilate**: 2, **Blur**: 5
- **Best for**: Blue cloth, denim, or colored fabric
- **Tip**: Works well in various lighting conditions

### Green 🟢
- **Range**: H(36-89), S(50-255), V(70-255)
- **Kernel**: 5, **Dilate**: 2, **Blur**: 5
- **Best for**: Green screen fabric, green cloth, chroma key backgrounds
- **Advantage**: Professional-grade green screens give best results

### White ⚪
- **Range**: H(0-180), S(0-40), V(200-255)
- **Kernel**: 5, **Dilate**: 2, **Blur**: 5
- **Best for**: White sheets, paper, or light-colored fabric
- **Challenge**: Requires very bright, uniform lighting

### Custom Colors 🌈
You can create your own color presets by:
1. Pressing `[h]` to open HSV controls
2. Adjusting the trackbars to detect your desired color
3. Fine-tuning kernel, dilate, and blur values
4. Adding the preset to the code for future use

## 📁 Project Structure

```
Invisibility-Cloak/
│
├── invisibility_cloak.py      # Main application with OpenCV
├── streamlit_cloak.py          # Web-based Streamlit version
├── diagnostic_check.py         # System diagnostics tool
├── requirements.txt            # Python dependencies
└── README.md                   # Project documentation
```

## 🛠️ Troubleshooting

### Camera Issues
- **Camera not opening**: Try changing `CAM_INDEX` in the code (0, 1, or 2)
- **Permission denied**: Close other applications using the camera
- **Poor quality**: Ensure good lighting conditions

### Detection Issues
- **Color not detected**: Use HSV controls (`[h]`) to adjust color ranges
- **Flickering effect**: Increase blur value or adjust kernel size
- **Incomplete invisibility**: Ensure uniform colored cloth and adjust dilation

### Performance Issues
- **Low FPS**: Reduce camera resolution or close other applications
- **Lag**: Update graphics drivers or use a more powerful machine

## 🧪 Diagnostic Tool

Run the diagnostic check to verify your setup:
```bash
python diagnostic_check.py
```

This will check:
- Python version
- Installed packages
- Camera availability
- System information

## 📸 Tips for Best Results

### Lighting 💡
- Use **consistent, bright lighting** without harsh shadows
- Avoid direct sunlight or strong backlighting
- Diffused light (like cloudy day or softbox) works best
- Keep lighting consistent during background capture and actual use

### Background 🖼️
- Choose a **static, non-moving** background
- Avoid complex patterns or moving elements (fans, curtains, people)
- Simple, solid-colored backgrounds work better
- Ensure nothing changes between background capture and use

### Cloth Selection 👕
- Use **solid-colored, non-reflective** fabric
- Avoid shiny, metallic, or patterned fabrics
- Larger cloth = better coverage
- Smooth fabric without wrinkles gives cleaner edges

### Camera Position 📹
- **Stay still** during background capture (3-second countdown)
- Mount camera on a tripod if possible
- Avoid camera movement during use
- Position camera at eye level for best perspective

### Performance Optimization ⚡
- Close unnecessary applications
- Use good lighting to reduce noise
- Adjust camera resolution if needed (default: 1280x720)
- Update graphics drivers for better performance

### Advanced Tuning 🎛️
- **Kernel Size**: Larger values = smoother but less precise edges (recommended: 5-9)
- **Dilate Iterations**: More = larger masked area (recommended: 1-3)
- **Blur Value**: Higher = smoother transitions but less sharp (recommended: 3-7)
- **HSV Ranges**: Narrow ranges = precise but may miss some colors; Wide ranges = catches more but may include unwanted colors

## 🔬 Technical Details

### Computer Vision Techniques
- **Color Space**: HSV (Hue, Saturation, Value) for robust color detection
  - More intuitive than RGB for color-based segmentation
  - Separates color information from brightness
  - Better performance under varying lighting conditions

### Image Processing Pipeline
1. **Frame Capture**: Read frame from camera using OpenCV VideoCapture
2. **Color Space Conversion**: Convert BGR to HSV using `cv2.cvtColor()`
3. **Color Thresholding**: Create binary masks using `cv2.inRange()`
4. **Mask Combination**: Combine two HSV ranges using `cv2.bitwise_or()`
5. **Morphological Operations**:
   - **Opening**: Removes noise (`cv2.MORPH_OPEN`)
   - **Closing**: Fills gaps (`cv2.MORPH_CLOSE`)
   - **Dilation**: Expands masked regions (`cv2.dilate()`)
6. **Blur Application**: Gaussian blur for smooth edges (`cv2.GaussianBlur()`)
7. **Mask Inversion**: Create inverse mask using `cv2.bitwise_not()`
8. **Image Composition**:
   - Extract cloak area from background: `cv2.bitwise_and(background, mask)`
   - Extract rest from current frame: `cv2.bitwise_and(frame, mask_inv)`
   - Combine results: `cv2.add(cloak_area, rest)`

### Performance Features
- **Backend Optimization**: Uses DirectShow (Windows) for better camera performance
- **FPS Monitoring**: Real-time frame rate calculation
- **Resolution**: Default 1280x720 for balance between quality and performance
- **Mirror Mode**: Horizontal flip for intuitive interaction

### System Architecture
```
Camera Input → Frame Processing → Color Detection → Mask Creation 
→ Morphological Operations → Background Replacement → Display Output
```

### Configuration Options
```python
CAM_INDEX = 0           # Camera device index
MIRROR = True           # Enable mirror mode
WIN_NAME = "..."        # Window title
SHOW_HSV = False        # Show HSV controls on startup
CURRENT_COLOR = "red"   # Default color preset
```

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

### Reporting Issues 🐛
- Check if the issue already exists
- Provide detailed description with steps to reproduce
- Include system information (OS, Python version, OpenCV version)
- Attach screenshots or error messages if applicable

### Suggesting Features 💡
- Describe the feature and its use case
- Explain how it improves the project
- Consider implementation complexity

### Submitting Pull Requests 🔧
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Development Ideas 🚀
- [ ] Add object detection to identify and track the cloak automatically
- [ ] Implement multiple color detection simultaneously
- [ ] Add video recording functionality
- [ ] Create GUI with Tkinter or PyQt
- [ ] Add support for custom color presets saving/loading
- [ ] Implement edge refinement using machine learning
- [ ] Add augmented reality effects
- [ ] Support for multiple cameras
- [ ] Mobile app version (iOS/Android)
- [ ] Real-time performance profiling dashboard

### Code Style
- Follow PEP 8 guidelines
- Add comments for complex logic
- Update documentation for new features
- Test on multiple platforms if possible

## 📝 [License](./LICENSE.md): Proprietary – Permission Required

## 👨‍💻 Author

**Kalharapasan**
- GitHub: [@Kalharapasan](https://github.com/Kalharapasan)

## 🙏 Acknowledgments

- **OpenCV Community** for excellent documentation and tutorials
- **Computer Vision Enthusiasts** worldwide for sharing knowledge
- **Harry Potter Series** by J.K. Rowling for the magical inspiration! ⚡
- **NumPy Developers** for efficient array operations
- **Python Community** for creating an amazing ecosystem
- **Stack Overflow Contributors** for invaluable problem-solving help

### Inspired By
- Harry Potter's Invisibility Cloak
- Chroma Key Technology used in film production
- Advanced computer vision research

### Educational Resources
- [OpenCV Documentation](https://docs.opencv.org/)
- [HSV Color Space Explanation](https://en.wikipedia.org/wiki/HSL_and_HSV)
- [Morphological Operations Tutorial](https://docs.opencv.org/master/d9/d61/tutorial_py_morphological_ops.html)

## 📚 Further Reading

### Concepts Used
- **Color Detection**: HSV-based segmentation for robust color identification
- **Background Subtraction**: Static background replacement technique
- **Morphological Operations**: Mathematical morphology for image processing
- **Masking**: Binary image operations for selective processing
- **Real-time Processing**: Efficient algorithms for live video feed

### Related Projects
- Green Screen Effects
- Chroma Key Applications
- Augmented Reality Filters
- Object Detection and Tracking
- Real-time Video Effects

## 🎓 Learning Outcomes

By working with this project, you'll learn:
- ✅ OpenCV fundamentals and camera handling
- ✅ Color space conversions (BGR → HSV)
- ✅ Image masking and binary operations
- ✅ Morphological transformations
- ✅ Real-time video processing
- ✅ GUI creation with OpenCV trackbars
- ✅ Performance optimization techniques
- ✅ Computer vision algorithm implementation

## 📧 Contact

For questions, suggestions, or collaboration:

- **GitHub Issues**: [Report bugs or request features](https://github.com/Kalharapasan/Invisibility-Cloak/issues)
- **Pull Requests**: [Contribute to the project](https://github.com/Kalharapasan/Invisibility-Cloak/pulls)
- **Discussions**: Share your results and ideas on GitHub Discussions

## ⭐ Star This Project

If you find this project helpful or interesting, please consider giving it a star! ⭐

It helps others discover the project and motivates continued development.

## 📜 Version History

### v1.0.0 (Current)
- ✅ Initial release
- ✅ Multiple color presets (Red, Blue, Green, White)
- ✅ Real-time HSV controls
- ✅ Background capture with countdown
- ✅ FPS monitoring
- ✅ Frame saving functionality
- ✅ Cross-platform support

### Future Updates
- 🔜 Object detection integration
- 🔜 Additional color presets (Yellow, Orange, Pink, Purple)
- 🔜 Video recording with audio
- 🔜 Advanced edge refinement
- 🔜 Machine learning-based color detection

## 🔐 Privacy & Safety

- 🔒 **No Data Collection**: This application runs entirely locally
- 📹 **Camera Usage**: Only used for real-time processing, no recording without explicit save command
- 💾 **Saved Files**: Only saved when you press `[s]` key
- 🛡️ **No Internet Required**: Works completely offline

## 🌐 Platform-Specific Notes

### Windows 🪟
- Uses DirectShow backend for optimal camera performance
- Tested on Windows 10 and Windows 11
- PowerShell or CMD for running scripts

### Linux 🐧
- Requires V4L2 compatible camera
- May need camera permissions: `sudo usermod -a -G video $USER`
- Tested on Ubuntu 20.04, 22.04

### macOS 🍎
- Uses default camera backend
- May require camera permissions in System Preferences
- Tested on macOS Monterey and Ventura

## 🎯 Use Cases

- 🎓 **Education**: Learn computer vision and image processing
- 🎨 **Art Projects**: Create magical photos and videos
- 🎬 **Content Creation**: YouTube videos, TikTok content
- 🔬 **Research**: Study color detection and background subtraction
- 🎪 **Entertainment**: Amaze friends and family
- 💼 **Portfolio**: Showcase programming skills

## ❓ FAQ

**Q: Why doesn't the invisibility effect work perfectly?**  
A: The quality depends on lighting, cloth uniformity, and background complexity. Adjust HSV values and ensure good lighting for best results.

**Q: Can I use other colors besides Red, Blue, Green, and White?**  
A: Yes! Press `[h]` to access HSV controls and tune for any color. You can also add custom presets to the code.

**Q: Why does my camera show error on startup?**  
A: Try changing `CAM_INDEX` from 0 to 1 or 2. Also ensure no other application is using the camera.

**Q: Can I record videos of the invisibility effect?**  
A: Currently, you can save individual frames with `[s]`. Video recording feature is planned for future updates.

**Q: What's the minimum system requirements?**  
A: Python 3.7+, 4GB RAM, webcam, and any modern OS (Windows/Linux/macOS).

**Q: How can I improve performance/FPS?**  
A: Close other applications, reduce camera resolution, ensure good lighting, and update drivers.

**Q: Does this work with multiple people?**  
A: Yes, as long as they're wearing the same color cloth within the detected range.

**Q: Can I use this professionally for video production?**  
A: For professional use, consider dedicated chroma key software. This is primarily an educational/demonstration project.

---

**Note**: This is a fun computer vision project for educational purposes. The quality of the invisibility effect depends on lighting conditions, background complexity, and cloth color consistency.

**Disclaimer**: This project is not affiliated with Harry Potter, Warner Bros, or J.K. Rowling. It's an independent educational project inspired by the fictional invisibility cloak.

---

<div align="center">

### Enjoy your invisibility powers! 🎩✨🪄

**Made with ❤️ and Python**

[![GitHub](https://img.shields.io/badge/GitHub-Kalharapasan-181717?style=for-the-badge&logo=github)](https://github.com/Kalharapasan)
[![Python](https://img.shields.io/badge/Python-3.7+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.0+-5C3EE8?style=for-the-badge&logo=opencv)](https://opencv.org/)

**[⬆ Back to Top](#invisibility-cloak-️)**

</div>
" 
