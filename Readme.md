# 👁️ Eye Controlled Mouse - Version 2 (Improved)

This is an improved version of the eye-controlled mouse system built using Python, OpenCV, and MediaPipe. It adds calibration, cursor smoothing, and dwell-based clicking for a smoother and more reliable experience.

---

## 🚀 Improvements Over Version 1

- ✅ **Calibration Phase**: Guides the user to look around the screen edges before tracking begins
- ✅ **Smooth Cursor Movement**: Uses sigmoid-based non-linear scaling and a moving average buffer
- ✅ **Dwell-Based Clicking**: Triggers a click if the cursor remains at the same position for 1.5 seconds
- ✅ **Toggle Controls**: Easily enable or disable tracking and clicking with keyboard shortcuts

---

## ⚙️ How It Works

1. **Calibration**: The system records eye positions as the user looks around, defining the bounds for accurate mapping.
2. **Mapping**: Eye coordinates are normalized and mapped using a sigmoid function for more natural control.
3. **Cursor Smoothing**: Uses a buffer of recent cursor positions to reduce jitter.
4. **Dwell Click**: If the eye gaze stays near one point for more than 1.5 seconds, a click is automatically performed.

---

## 🖼️ Screenshot / Demo

> (Add a short demo video or GIF showing calibration and smooth control)

---

## 🧰 Requirements

```bash
pip install opencv-python mediapipe pyautogui numpy scipy
```

---

## ▶️ How to Run

```bash
python version2.py
```

---

## ⌨️ Keyboard Shortcuts

| Key | Function              |
|-----|-----------------------|
| `q` | Quit                  |
| `t` | Toggle Eye Tracking   |
| `c` | Toggle Dwell Clicking |
| `r` | Recalibrate           |

---

## 📂 File Structure

```
Version2/
│
├── version2.py      # Improved version with calibration and smoothing
├── README.md        # This file
```

---

## 📊 Performance

- Cursor movement is more accurate and less jittery
- Dwell-clicking reduces false clicks from normal blinks
- Calibrated control makes it easier to access all screen regions without exaggerated head movement

---

## 📊 Compare With Version 1

| Feature             | Version 1 | Version 2 |
|---------------------|-----------|-----------|
| Eye Tracking        | ✅         | ✅         |
| Blink to Click      | ✅         | ❌ (uses dwell) |
| Calibration         | ❌         | ✅         |
| Cursor Smoothing    | ❌         | ✅         |
| Toggle Control      | ❌         | ✅         |

---

## 📸 Credits

- [MediaPipe](https://github.com/google/mediapipe) by Google
- [OpenCV](https://opencv.org/)
- [PyAutoGUI](https://pyautogui.readthedocs.io/)
- [SciPy](https://scipy.org/) and [NumPy](https://numpy.org/) for math and signal smoothing

---

## 🙌 Author

**Dilaikshan**  
If you're interested in eye tracking, assistive tech, or computer vision, feel free to connect with me on [LinkedIn](https://linkedin.com)!

---

