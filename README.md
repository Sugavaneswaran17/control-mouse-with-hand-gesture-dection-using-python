Hand Gesture Mouse Control
Control your computer's mouse using hand gestures detected via a webcam. This project uses Python, OpenCV, MediaPipe, and PyAutoGUI to track hand movements and translate them into mouse movements and clicks.

Features
Real-time Hand Tracking: Detects hand landmarks using MediaPipe.

Mouse Movement: Moves the mouse cursor based on the position of your index finger.

Mouse Click: Simulates a mouse click when the thumb and index finger are brought close together.

Smooth Cursor Movement: Applies smoothing to reduce jittery mouse movements.

Prerequisites
Before running the project, ensure you have the following installed:

Python 3.x: Download and install Python from python.org.

Required Libraries: Install the required Python libraries using pip:

bash
Copy
pip install opencv-python mediapipe pyautogui
Webcam: A working webcam is required for hand gesture detection.

How to Run
Clone the repository or download the source code:

bash
Copy
git clone https://github.com/your-username/hand-gesture-mouse-control.git
cd hand-gesture-mouse-control
Run the Python script:

bash
Copy
python hand_gesture_mouse_control.py
Show your hand to the webcam:

Move your index finger to control the mouse cursor.

Bring your thumb close to your index finger to simulate a mouse click.

Press q to quit the application.

Code Overview
Key Components
Hand Landmark Detection:

Uses MediaPipe's Hands module to detect and track hand landmarks.

Maps the index finger and thumb positions to screen coordinates.

Mouse Control:

Uses PyAutoGUI to move the mouse cursor and perform clicks.

Applies smoothing to ensure smooth cursor movement.

Webcam Feed:

Displays the webcam feed with hand landmarks overlaid.

Customization
Smoothing Factor: Adjust the smoothening variable in the code to control the smoothness of the mouse movement.

Click Threshold: Modify the distance threshold (if distance < 30) to change the sensitivity of the mouse click.

Screen Resolution: The script automatically detects your screen resolution using pyautogui.size(). If needed, you can manually set screen_width and screen_height.

Troubleshooting
No Hand Detected:

Ensure your hand is visible to the webcam and well-lit.

Adjust the min_detection_confidence parameter in the Hands initialization.

Mouse Moves Erratically:

Increase the smoothening factor in the code.

Ensure proper lighting and a clear view of your hand.

High CPU Usage:

Reduce the webcam resolution or frame rate.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgments
MediaPipe for hand landmark detection.

OpenCV for computer vision.

PyAutoGUI for mouse control.

Contributing
Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

Author
[SUGAVANESWARAN.R]
[]
[sugavanesraja6598@gmail.com]
