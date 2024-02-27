import cv2
import numpy as np
import mediapipe as mp

mpHands = mp.solutions.hands
hands = mpHands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mpDraw = mp.solutions.drawing_utils
cap = cv2.VideoCapture(0)
canvas = np.zeros((480, 640, 3), np.uint8)
last_point = None
gesture = ' '  
num_fingers = 0  

while True:
    ret, frame = cap.read()
    
    
    if ret and frame is not None and frame.shape[0] > 0 and frame.shape[1] > 0:
        x, y, c = frame.shape
        frame = cv2.flip(frame, 1)
        framergb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = hands.process(framergb)

        if result.multi_hand_landmarks:
            landmarks = []
            for handslms in result.multi_hand_landmarks:
                for lm in handslms.landmark:
                    lmx = int(lm.x * x)
                    lmy = int(lm.y * y)

                    landmarks.append([lmx, lmy])
                    
            mpDraw.draw_landmarks(frame, handslms, mpHands.HAND_CONNECTIONS)
            
            if len(landmarks) > 0:
                num_fingers = 0  # Reset num_fingers
                
                if landmarks[4][0] < landmarks[3][0]:
                    num_fingers += 1
                if landmarks[8][1] < landmarks[6][1]:
                    num_fingers += 1
                if landmarks[12][1] < landmarks[10][1]:
                    num_fingers += 1
                if landmarks[16][1] < landmarks[14][1]:
                    num_fingers += 1
                if landmarks[20][1] < landmarks[18][1]:
                    num_fingers += 1
                    
                if num_fingers == 1:
                    gesture = 'Draw Line'
                elif num_fingers == 2:
                    gesture = 'Draw Rectangle'
                elif num_fingers == 3:
                    gesture = 'Draw Circle'
                elif num_fingers == 4:
                    gesture = 'Eraser'
                elif num_fingers == 5:
                    gesture = 'Eraser'
                    
                if canvas is not None:
                    if gesture == 'Draw Line':
                        current_point = landmarks[0]
                        if last_point is not None:
                            cv2.line(canvas, last_point, current_point, (157, 252, 220), 2)
                        last_point = current_point
                    elif gesture == 'Draw Rectangle':
                        cv2.rectangle(canvas, landmarks[0], landmarks[1], (200, 180, 233), 2)
                        last_point = None
                    elif gesture == 'Draw Circle':
                        cv2.circle(canvas, landmarks[0], 50, (223, 178, 200), -1)
                        last_point = None
                    elif gesture == 'Eraser':
                        cv2.circle(canvas, landmarks[0], 50, (0, 0, 0), -1)
                        last_point = None
                        
        cv2.imshow("Board", canvas)

        cv2.putText(frame, gesture, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 
                       1, (0,0,255), 2, cv2.LINE_AA)
        cv2.putText(frame, f"Number of Fingers: {num_fingers}", (10, 100), cv2.FONT_HERSHEY_SIMPLEX, 
                       1, (0,0,255), 2, cv2.LINE_AA)
        cv2.imshow("TechVidvan", frame)
        
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
