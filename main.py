import cv2
import mediapipe as mp
import pyautogui

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mp_drawing = mp.solutions.drawing_utils

# Initialize webcam
cap = cv2.VideoCapture(0)

# Get screen dimensions
screen_width, screen_height = pyautogui.size()

# Mouse movement smoothing
smoothening = 5
prev_x, prev_y = screen_width // 2, screen_height // 2  # Start from the center of the screen
curr_x, curr_y = prev_x, prev_y

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Flip the frame horizontally for a later selfie-view display
    frame = cv2.flip(frame, 1)

    # Convert the BGR image to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the frame with MediaPipe Hands
    results = hands.process(rgb_frame)

    # If hands are detected
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Draw hand landmarks on the frame
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Get the coordinates of the index finger tip (landmark 8)
            index_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
            index_finger_x = int(index_finger_tip.x * screen_width)
            index_finger_y = int(index_finger_tip.y * screen_height)

            # Smooth the mouse movement
            curr_x = prev_x + (index_finger_x - prev_x) / smoothening
            curr_y = prev_y + (index_finger_y - prev_y) / smoothening

            # Ensure coordinates are within screen bounds
            if curr_x is not None and curr_y is not None:  # Check for valid values
                curr_x = max(0, min(curr_x, screen_width - 1))  # Clamp to screen width
                curr_y = max(0, min(curr_y, screen_height - 1))  # Clamp to screen height

                # Move the mouse
                pyautogui.moveTo(curr_x, curr_y)
                prev_x, prev_y = curr_x, curr_y

            # Get the coordinates of the thumb tip (landmark 4)
            thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
            thumb_x = int(thumb_tip.x * screen_width)
            thumb_y = int(thumb_tip.y * screen_height)

            # Calculate the distance between index finger tip and thumb tip
            distance = ((index_finger_x - thumb_x) ** 2 + (index_finger_y - thumb_y) ** 2) ** 0.5

            # If the distance is small, perform a mouse click
            if distance < 30:
                pyautogui.click()

    # Display the frame
    cv2.imshow('Hand Gesture Mouse Control', frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()