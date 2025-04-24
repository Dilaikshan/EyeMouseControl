import cv2
import numpy as np
import pyautogui
import mediapipe as mp
from scipy.special import expit as sigmoid
from collections import deque

# Constants
CALIBRATION_TIME = 5  # seconds
DWELL_TIME = 1.5  # seconds for click
SMOOTHING_WINDOW = 5  # frames


class EyeController:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        self.screen_w, self.screen_h = pyautogui.size()
        self.mp_face = mp.solutions.face_mesh
        self.face = self.mp_face.FaceMesh(
            max_num_faces=1,
            refine_landmarks=True,
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5)

        # Calibration variables
        self.calibration_data = {'x': [], 'y': []}
        self.is_calibrated = False

        # Cursor smoothing
        self.cursor_buffer = deque(maxlen=SMOOTHING_WINDOW)

        # Dwell click variables
        self.dwell_start_time = None
        self.last_click_time = 0
        self.click_radius = 30

        # Control toggles
        self.tracking_active = True
        self.clicking_active = True

    def calibrate(self):
        print("Look around the screen edges for calibration...")
        start_time = cv2.getTickCount()

        while (cv2.getTickCount() - start_time) / cv2.getTickFrequency() < CALIBRATION_TIME:
            success, frame = self.cap.read()
            if not success:
                continue

            frame = cv2.flip(frame, 1)
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = self.face.process(rgb_frame)

            if results.multi_face_landmarks:
                landmarks = results.multi_face_landmarks[0].landmark
                right_eye = landmarks[474]
                left_eye = landmarks[476]

                # Use average eye position
                eye_x = (right_eye.x + left_eye.x) / 2
                eye_y = (right_eye.y + left_eye.y) / 2

                self.calibration_data['x'].append(eye_x)
                self.calibration_data['y'].append(eye_y)

            cv2.imshow('Calibration', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # Calculate calibration ranges
        self.x_min, self.x_max = np.percentile(self.calibration_data['x'], [5, 95])
        self.y_min, self.y_max = np.percentile(self.calibration_data['y'], [5, 95])
        self.is_calibrated = True
        print("Calibration complete!")
        cv2.destroyWindow('Calibration')

    def map_to_screen(self, eye_x, eye_y):
        # Normalize with calibration data
        x_norm = (eye_x - self.x_min) / (self.x_max - self.x_min)
        y_norm = (eye_y - self.y_min) / (self.y_max - self.y_min)

        # Apply sigmoid for non-linear control
        x_screen = sigmoid(4 * (x_norm - 0.5)) * self.screen_w
        y_screen = sigmoid(4 * (y_norm - 0.5)) * self.screen_h

        # Keep cursor within screen bounds
        x_screen = np.clip(x_screen, 0, self.screen_w)
        y_screen = np.clip(y_screen, 0, self.screen_h)

        return int(x_screen), int(y_screen)

    def smooth_cursor(self, x, y):
        self.cursor_buffer.append((x, y))
        return np.mean(self.cursor_buffer, axis=0).astype(int)

    def handle_dwell_click(self, x, y):
        if not self.clicking_active:
            return

        current_time = cv2.getTickCount() / cv2.getTickFrequency()
        if self.dwell_start_time is None:
            self.dwell_start_time = current_time
            self.dwell_position = (x, y)
        else:
            distance = np.sqrt((x - self.dwell_position[0]) ** 2 +
                               (y - self.dwell_position[1]) ** 2)

            if distance < self.click_radius:
                if current_time - self.dwell_start_time > DWELL_TIME:
                    pyautogui.click()
                    self.dwell_start_time = None
                    print("Click performed!")
            else:
                self.dwell_start_time = None

    def run(self):
        if not self.is_calibrated:
            self.calibrate()

        while True:
            success, frame = self.cap.read()
            if not success:
                continue

            frame = cv2.flip(frame, 1)
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = self.face.process(rgb_frame)

            if results.multi_face_landmarks and self.tracking_active:
                landmarks = results.multi_face_landmarks[0].landmark
                right_eye = landmarks[474]
                left_eye = landmarks[476]

                # Calculate average eye position
                eye_x = (right_eye.x + left_eye.x) / 2
                eye_y = (right_eye.y + left_eye.y) / 2

                # Map to screen coordinates
                x, y = self.map_to_screen(eye_x, eye_y)
                x, y = self.smooth_cursor(x, y)

                # Move cursor
                pyautogui.moveTo(x, y)

                # Handle dwell clicking
                self.handle_dwell_click(x, y)

                # Visual feedback
                cv2.circle(frame, (int(eye_x * frame.shape[1]), int(eye_y * frame.shape[0])),
                           10, (0, 255, 0), -1)

                # Draw dwell timer
                if self.dwell_start_time is not None:
                    time_elapsed = cv2.getTickCount() / cv2.getTickFrequency() - self.dwell_start_time
                    cv2.putText(frame, f"Click in: {DWELL_TIME - time_elapsed:.1f}s",
                                (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

            # Display status
            status = f"Tracking: {'ON' if self.tracking_active else 'OFF'} | Clicking: {'ON' if self.clicking_active else 'OFF'}"
            cv2.putText(frame, status, (10, frame.shape[0] - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 1)

            cv2.imshow('Eye Controller', frame)

            # Handle keyboard controls
            key = cv2.waitKey(1) & 0xFF
            if key == ord('q'):
                break
            elif key == ord('t'):
                self.tracking_active = not self.tracking_active
            elif key == ord('c'):
                self.clicking_active = not self.clicking_active
            elif key == ord('r'):
                self.calibrate()

        self.cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    controller = EyeController()
    controller.run()