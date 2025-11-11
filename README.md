"# Invisibility Cloak 🧙‍♂️

A real-time computer vision application that creates an invisibility cloak effect using OpenCV and Python. Hide behind any colored cloth and watch yourself disappear like magic!

## 🌟 Features

- **Real-time Invisibility Effect**: Uses color detection and background subtraction to create a convincing invisibility effect
- **Multiple Color Presets**: Support for Red, Blue, Green, and White colored cloaks
- **Live HSV Controls**: Adjust color detection parameters in real-time with interactive trackbars
- **FPS Counter**: Monitor application performance
- **Background Capture**: Easy background capture with countdown timer
- **Frame Saving**: Save your invisible moments as images
- **Mirror Mode**: Flip the camera view for easier interaction

## 🎯 How It Works

The invisibility cloak effect is achieved through:

1. **Background Capture**: Captures the scene without the subject
2. **Color Detection**: Uses HSV color space to detect the colored cloth
3. **Mask Creation**: Creates a binary mask of the detected color region
4. **Background Replacement**: Replaces the masked region with the captured background
5. **Morphological Operations**: Smooths and refines the mask using kernel operations, dilation, and blur

## 📋 Prerequisites

- Python 3.7+
- Webcam or camera

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

### Red (Default)
- Range 1: H(0-10), S(120-255), V(70-255)
- Range 2: H(170-180), S(120-255), V(70-255)
- Best for: Red cloth, fabric, or blankets

### Blue
- Range: H(94-126), S(80-255), V(2-255)
- Best for: Blue cloth, denim, or colored fabric

### Green
- Range: H(36-89), S(50-255), V(70-255)
- Best for: Green screen fabric, green cloth

### White
- Range: H(0-180), S(0-40), V(200-255)
- Best for: White sheets, paper, or light-colored fabric

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

1. **Lighting**: Use consistent, bright lighting without harsh shadows
2. **Background**: Choose a static, non-moving background
3. **Cloth**: Use solid-colored, non-reflective fabric
4. **Position**: Stay still during background capture
5. **Size**: Use cloth large enough to cover the area you want to hide

## 🔬 Technical Details

- **Color Space**: HSV (Hue, Saturation, Value) for robust color detection
- **Morphological Operations**: Opening and Closing to remove noise
- **Mask Processing**: Dilation and Gaussian Blur for smooth edges
- **Backend**: DirectShow (Windows) or default (Linux/Mac)

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests
- Improve documentation

## 📝 License

This project is open source and available under the MIT License.

## 👨‍💻 Author

**Kalharapasan**
- GitHub: [@Kalharapasan](https://github.com/Kalharapasan)

## 🙏 Acknowledgments

- OpenCV community for excellent documentation
- Computer vision tutorials and resources
- Harry Potter for the inspiration! ⚡

## 📧 Contact

For questions or suggestions, please open an issue on GitHub.

---

**Note**: This is a fun computer vision project for educational purposes. The quality of the invisibility effect depends on lighting conditions, background complexity, and cloth color consistency.

Enjoy your invisibility powers! 🎩✨
" 
