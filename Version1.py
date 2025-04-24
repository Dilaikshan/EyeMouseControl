import cv2
import mediapipe as mp
import pyautogui

cam = cv2.VideoCapture(0)
face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
screen_w, screen_h = pyautogui.size()

# For cursor smoothing
history = []
history_length = 5

# For dynamic range adjustment
min_x = max_x = min_y = max_y = None

while True:
    _, frame = cam.read()
    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = face_mesh.process(rgb_frame)
    landmark_points = output.multi_face_landmarks
    frame_h, frame_w, _ = frame.shape

    if landmark_points:
        landmarks = landmark_points[0].landmark

        # Get iris landmarks (average of four points)
        iris_landmarks = landmarks[474:478]
        iris_x = sum([lm.x for lm in iris_landmarks]) / 4
        iris_y = sum([lm.y for lm in iris_landmarks]) / 4

        # Add to smoothing history
        history.append((iris_x, iris_y))
        if len(history) > history_length:
            history.pop(0)

        avg_iris_x = sum([h[0] for h in history]) / len(history)
        avg_iris_y = sum([h[1] for h in history]) / len(history)

        # Update dynamic range
        min_x = min(avg_iris_x, min_x) if min_x is not None else avg_iris_x
        max_x = max(avg_iris_x, max_x) if max_x is not None else avg_iris_x
        min_y = min(avg_iris_y, min_y) if min_y is not None else avg_iris_y
        max_y = max(avg_iris_y, max_y) if max_y is not None else avg_iris_y

        # Calculate screen coordinates with dynamic range
        try:
            screen_x = ((avg_iris_x - min_x) / (max_x - min_x)) * screen_w
            screen_y = ((avg_iris_y - min_y) / (max_y - min_y)) * screen_h
        except ZeroDivisionError:
            screen_x, screen_y = pyautogui.position()

        # Keep cursor within screen bounds
        screen_x = max(0, min(screen_w, screen_x))
        screen_y = max(0, min(screen_h, screen_y))

        pyautogui.moveTo(screen_x, screen_y)

        # Draw iris visualization
        viz_x = int(avg_iris_x * frame_w)
        viz_y = int(avg_iris_y * frame_h)
        cv2.circle(frame, (viz_x, viz_y), 5, (0, 255, 0), -1)

        # Click functionality (original with enhanced stability)
        left = [landmarks[145], landmarks[159]]
        for landmark in left:
            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)
            cv2.circle(frame, (x, y), 3, (0, 255, 255))

        if (left[0].y - left[1].y) < 0.006:
            pyautogui.click()
            pyautogui.sleep(0.5)

    cv2.imshow('Enhanced Eye Control Mouse', frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cam.release()
cv2.destroyAllWindows()