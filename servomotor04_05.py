#from gpiozero import Servo
from time import sleep

servo = Servo(12)
val = 0

try:
    while True:
        i = 0
        j = 0
        teste = input()
        if teste == '6':
            if val <= 0.8:
                for i in range(1):
                    val = val+0.1
                    servo.value = val
                    sleep(0.5)
                    print(val)
            else:
                servo.value = val
        if teste == '4':
            if val >= -0.8:
                for i in range(1):
                    val = val-0.1
                    servo.value = val
                    sleep(0.5)
                    print(val)
            else:
                servo.value = val
except KeyboardInterrupt:
    print("Programa parou")
