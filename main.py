import cv2 #import the respect opencv package
import mediapipe as  mp # this is respect to detect face

cam = cv2.VideoCapture(0) # declare cam used to capture video
face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
while True:
    _,frame = cam.read()
    rgp_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = face_mesh.process(rgp_frame)

    landmark_points = output.multi_face_landmarks
    frame_h, frame_w,_= frame.shape

    if landmark_points:
        landmarks = landmark_points[0].landmark
        for landmark in landmarks[474:478]:
            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)
            cv2.circle(frame,(x,y),3,(0,255,0))
            print(x, y)
    cv2.imshow('Eye control mouse', frame)
    cv2.waitKey(1)
