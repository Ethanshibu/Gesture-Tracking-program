import cv2
import mediapipe as mp
import subprocess

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

# Start webcam
cap = cv2.VideoCapture(0)

launched = False
process = None  # Will hold the subprocess process

with mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7) as hands:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Flip image for mirror effect & convert to RGB
        frame = cv2.flip(frame, 1)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Process the image to find hands
        results = hands.process(rgb_frame)

        # Initialize finger states outside the loop
        rfingers = None
        lfingers = None

        if results.multi_hand_landmarks:
            for hand_idx, landmarks in enumerate(results.multi_hand_landmarks):
                # Draw landmarks on the frame
                mp_drawing.draw_landmarks(frame, landmarks, mp_hands.HAND_CONNECTIONS)
                handedness = results.multi_handedness[hand_idx].classification[0].label

                # Finger tip and pip indices
                finger_tips = [4, 8, 12, 16, 20]
                finger_pips = [3, 6, 10, 14, 18]

                landmark_list = landmarks.landmark

                def get_finger_state(landmark, finger_tip, finger_pip):
                    flist = []
                    flist.append(int((landmark[4].x > landmark[3].x)))  # Thumb
                    for tip, pip in zip(finger_tips[1:], finger_pips[1:]):
                        flist.append(int(landmark[tip].y > landmark[pip].y))
                    return flist

                if handedness == "Right":
                    rfingers = get_finger_state(landmark_list, finger_tips, finger_pips)
                elif handedness == "Left":
                    lfingers = get_finger_state(landmark_list, finger_tips, finger_pips)


        if rfingers == [1, 0, 1, 1, 0] and not launched:
            process = subprocess.Popen(["notepad.exe"])
            launched = True
            print("Notepad launched.")

        if lfingers == [0, 0, 0, 1, 1] and launched:
            subprocess.run(["taskkill", "/f", "/im", "notepad.exe"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            process = None
            launched = False
            print("Notepad closed.")

        cv2.imshow("Hand Tracker", frame)

        # Exit on 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
