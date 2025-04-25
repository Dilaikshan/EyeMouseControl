# 👁️ Eye Controlled Mouse - Version 1

This is the first version of an eye-tracking mouse controller using Python, OpenCV, and MediaPipe. It allows users to control the mouse cursor using their eye movements and perform click actions by blinking.

---

## 🚀 Features

- 👟 Move the mouse cursor using your right eye
- 👁️ Left eye blink detection triggers a click
- 🔧 Lightweight and easy to run
- 🎓 Good starting point to learn computer vision with facial landmarks

---

## ⚙️ How It Works

1. Uses **MediaPipe FaceMesh** to detect facial landmarks on the face.
2. Tracks specific landmarks near the right eye (IDs 474–478) to move the mouse cursor.
3. Detects left eye blink by measuring vertical distance between landmarks 145 and 159.
4. If a blink is detected (based on distance threshold), it triggers a mouse click.

---

## 🖼️ Screenshot / Demo

> (You can add a GIF or screenshot here after recording)

---

## 🧰 Requirements

Make sure you have Python 3 installed. Then, install the required packages using pip:

```bash
pip install opencv-python mediapipe pyautogui
```

---

## ▶️ How to Run

Clone the repository and run the script:

```bash
python version1.py
```

---

## 📝 Notes

- The program uses your webcam for real-time eye tracking.
- Mouse movement works, but reaching the screen corners can be difficult — you might need to move your face/head more than usual.
- Clicking is based on **left eye blink detection** — sometimes it might click by mistake if you blink naturally.

---

## 📂 File Structure

```
Version1/
│
├── version1.py      # Main script for eye tracking and control
├── README.md        # This file
```

---

## 📈 Limitations

- No calibration phase, so cursor control can feel "stretched" or too sensitive.
- Blink detection might misfire depending on lighting and your blinking pattern.
- No smoothing — cursor may jitter if your eye position fluctuates slightly.

---

## 💡 What's Next?

Check out [Version 2](../Version2/README.md) — it includes:

- ✅ Calibration for smoother control
- ✅ Dwell-based click (no blinking)
- ✅ Cursor smoothing and better experience

---

## 📸 Credits

- [MediaPipe](https://github.com/google/mediapipe) by Google for facial landmark detection
- [OpenCV](https://opencv.org/) for image processing
- [PyAutoGUI](https://pyautogui.readthedocs.io/) for mouse control

---

## 🙌 Author

**Dilaikshan**  
Feel free to connect with me on [LinkedIn](https://linkedin.com) and check out the improved version in this repo!

---

