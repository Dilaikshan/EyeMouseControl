# Eye-Controlled Mouse

This project implements an eye-controlled mouse using computer vision techniques. By tracking eye movements and blinks through a webcam, the system moves the mouse cursor accordingly and performs click operations when a blink is detected.

## Features

- **Eye Tracking**: Moves the mouse cursor based on the position of the user's eye.
- **Blink Detection**: Performs a mouse click when the user blinks.
- **Real-Time Processing**: Uses webcam input for continuous tracking.

## Prerequisites

To run this project, you need to install the following Python libraries:

- `opencv-python` (for webcam capture and image processing)
- `mediapipe` (for face and eye landmark detection)
- `pyautogui` (for controlling the mouse cursor)

You can install these dependencies using pip:

```bash
pip install opencv-python mediapipe pyautogui
```

## Hardware Requirements

- A webcam (built-in or external) for capturing video input.
- A computer running Windows, macOS, or Linux.

## Usage

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/Dilaikshan/eye-controlled-mouse.git
   ```
2. Navigate to the project directory:

   ```bash
   cd eye-controlled-mouse
   ```
3. Run the Python script:

   ```bash
   python eye_controlled_mouse.py
   ```
4. The webcam will open, and the mouse cursor will start following your eye movements.
5. Blink to perform a mouse click.

## How It Works

- **Webcam Input**: The script uses OpenCV to capture video from the default webcam.
- **Face and Eye Detection**: MediaPipe's FaceMesh model detects facial landmarks, focusing on the eyes.
- **Mouse Control**:
  - The position of the right eye (landmarks 474-477) is mapped to the screen coordinates to move the mouse cursor using PyAutoGUI.
  - A blink is detected by measuring the vertical distance between specific eye landmarks (145 and 159). If the distance is below a threshold, a click is triggered.
- **Visualization**: Green circles are drawn on the eye landmarks for visual feedback, displayed in a window.

## Code Structure

- `eye_controlled_mouse.py`: The main script containing the eye-tracking and mouse control logic.
- Key components:
  - Webcam initialization with OpenCV.
  - FaceMesh setup with MediaPipe for landmark detection.
  - Mouse movement and click logic using PyAutoGUI.

## Limitations

- **Lighting Conditions**: Performance may vary under poor lighting or with reflective surfaces.
- **Calibration**: The system assumes a standard webcam resolution and may require tuning for different setups.
- **Blink Sensitivity**: The blink detection threshold (0.006) may need adjustment for different users or environments.
- **Single User**: The system tracks only one face at a time.

## Future Improvements

- Add calibration for different screen sizes and webcam resolutions.
- Improve blink detection robustness with machine learning models.
- Support multiple click types (e.g., double-click, right-click) using different eye gestures.
- Optimize performance for lower-end hardware.

## Troubleshooting

- **Webcam Not Detected**: Ensure your webcam is connected and accessible. Try changing the camera index in `cv2.VideoCapture(0)`.
- **Dependencies Issues**: Verify that all required libraries are installed correctly.
- **Mouse Not Moving**: Ensure the webcam captures your face clearly and that lighting conditions are adequate.

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests for bug fixes, optimizations, or new features.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments

- OpenCV for computer vision utilities.
- MediaPipe for face landmark detection.
- PyAutoGUI for mouse control.