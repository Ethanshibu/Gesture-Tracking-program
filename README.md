# ✋ Hand Gesture App Launcher using OpenCV & MediaPipe

This project uses your **webcam** to detect hand gestures in real-time and launch or close applications (e.g., Notepad) using specific finger poses. It combines **computer vision**, **hand landmark detection**, and **gesture recognition** into a lightweight interface.

---

## 🎯 Features

- 👋 Detects hand gestures using **MediaPipe Hands**
- 🧠 Custom logic to recognize specific finger poses
- 🚀 Launches Notepad using a **right-hand gesture**
- 🛑 Closes Notepad using a **left-hand gesture**
- 🪟 Built for Windows with `taskkill` integration
- 🔄 Real-time feedback via webcam feed

---

## 🤖 Gestures Used

<table>
  <tr>
    <th>Hand</th>
    <th>Finger Pose</th>
    <th>Action</th>
  </tr>
  <tr>
    <td>Right Hand</td>
    <td>🤘 (Index + Pinky fingers up)</td>
    <td>Launch Notepad</td>
  </tr>
  <tr>
    <td>Left Hand</td>
    <td>✌️ (Index + Middle fingers up)</td>
    <td>Close Notepad</td>
  </tr>
</table>


*(You can modify the finger pattern in code to change behavior.)*

---

## 🛠️ Libraries used

- Python 3.x  
- OpenCV  
- MediaPipe  
- Subprocess (for app control)

---

