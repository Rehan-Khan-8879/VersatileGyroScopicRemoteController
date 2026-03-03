import serial
import keyboard
import time

# CHANGE COM PORT HERE
ser = serial.Serial('COM4', 9600)
time.sleep(2)

print("Connected to ESP8266")

while True:
    if keyboard.is_pressed('q'):
        print("Exiting...")
        break
    try:
        if ser.in_waiting > 0:
            line = ser.readline().decode().strip()
            values = line.split(',')

            if len(values) == 6:
                joyX1 = int(values[0])
                joyY1 = int(values[1])
                joyX2 = int(values[2])
                joyY2 = int(values[3])
                gyroX = int(values[4])
                gyroY = int(values[5])

                print(joyX1, joyY1, joyX2, joyY2, gyroX, gyroY)

                # -------- KEYBOARD CONTROL --------

                # Forward
                if joyX2 > 7:
                    keyboard.press('s')
                else:
                    keyboard.release('s')

                # Backward
                if joyX2 < 3:
                    keyboard.press('w')
                else:
                    keyboard.release('w')

                # Left
                if joyY1 < 3 :
                    keyboard.press('d')
                else:
                    keyboard.release('d')

                # Right
                if joyY1 > 7 :
                    keyboard.press('a')
                else:
                    keyboard.release('a')


    except:
        pass