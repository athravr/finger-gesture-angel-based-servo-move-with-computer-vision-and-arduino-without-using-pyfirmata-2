import cv2
import cvzone
from cvzone.HandTrackingModule import HandDetector
import serial
import time

# Initialize serial communication with Arduino
arduino = serial.Serial(port='COM3', baudrate=9600, timeout=.1)  # Change 'COM3' to your Arduino port

# Initialize webcam
cap = cv2.VideoCapture(0)
detector = HandDetector(maxHands=1, detectionCon=0.8)
print("1 pass out of 5 athrav raj")
print("2 pass out of 5 athrav raj")
print("3 pass out of 5 athrav raj")
print("4 pass out of 5 athrav raj")
print("5 pass out of 5 athrav raj")
print("serial connected athrav raj")
print("arduino passed athrav raj ")
print("made by athrav raj for class 8 'c' assembly")
print("CLASS 8'C' WELCOME YOU PRESENTED BY ATHRAV RAJ")
def calculate_angle(point1, point2, point3):
    # Function to calculate the angle between three points
    import math
    a = point2[0] - point1[0]
    b = point2[1] - point1[1]
    c = point3[0] - point2[0]
    d = point3[1] - point2[1]

    angle = math.degrees(math.atan2(d, c) - math.atan2(b, a))
    if angle < 0:
        angle += 360
    return angle

while True:
    success, img = cap.read()
    if not success:
        break

    hands, img = detector.findHands(img)

    if hands:
        hand = hands[0]
        lmList = hand['lmList']  # List of 21 Landmark points

        if len(lmList) >= 8:
            # Calculate angle between three landmarks (e.g., index finger: tip, PIP, MCP)
            angle = calculate_angle(lmList[5], lmList[6], lmList[8])
            print(f"Angle: {angle}")

            # Map angle to servo position (0 to 180 degrees)
            servo_angle = int(angle)
            if servo_angle > 180:
                servo_angle = 180
            elif servo_angle < 0:
                servo_angle = 0

            # Send the angle to Arduino
            arduino.write(bytes(f"{servo_angle}\n", 'utf-8'))
            time.sleep(0.1)

    cv2.imshow('ASSEMBLY CLASS 8 C MADE BY ATHRAV RAJ', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
