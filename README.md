This repository contains two Python projects: a computer vision-based hand gesture drawing app, and a simple employee information handler using object-oriented programming.
# Python Projects

This repository contains two Python projects: a computer vision-based hand gesture drawing app, and a simple employee information handler using object-oriented programming.

## 📌 Projects

### 1. ✋ Draw with Finger (Hand Gesture Drawing App)

This project uses a webcam to detect hand gestures and lets you draw on a virtual canvas using different gestures.

**Features:**
- Uses MediaPipe to detect hands and landmarks
- Draw lines, rectangles, circles, or erase based on the number of fingers shown
- Real-time video feed with gesture detection overlay

**Finger Mapping:**
- 1 Finger: Draw Line  
- 2 Fingers: Draw Rectangle  
- 3 Fingers: Draw Circle  
- 4 or 5 Fingers: Eraser  

**Dependencies:**
```bash
pip install opencv-python mediapipe numpy
Run the project:

bash
Copy
Edit
python "draw with fingure.py"
```

# 1.👨‍💼 Employer ID Handler

A basic Python script using classes to manage and display employee data.##  Functionality
Stores ID, name, gender, city, and salary

Displays all stored information

## Code Structure

Employee class with private attributes

setData() method to initialize data

showData() method to display the data

## Run the project

bash
Copy
Edit
python Employer_Id.py
## ✅ Requirements
Python 3.8+

Webcam (for the hand gesture app)

