#code for servo motors
import Rpi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
pwmPin1=18
pwmPin2=12
GPIO.setup(pwmPin1,GPIO.OUT)
GPIO.setup(pwmPin2,GPIO.OUT)
pwm1=GPIO.PWM(pwmPin1,50)
pwm2=GPIO.PWM(pwmPin2,50)
pwm1.start()
pwm2.start()

try:
    while True:
        for i in range(1,11):
            pwm1.changeDutyCycle(i)
            time.sleep(0.1)
            for j in range(1,7):
                pwm2.changeDutyCycle(j)
                time.sleep(0.1)
            pwm1.changeDutyCycle(i+0.5)
            time.sleep(0.1)
        for i in range(10,1,-1):
            pwm1.changeDutyCycle(i+0.5)
            time.sleep(0.1)
            for j in range(1,7):
                pwm2.changeDutyCycle(j)
                time.sleep(0.1)
            pwm1.changeDutyCycle(i)
            time.sleep(0.1)
except KeyboardInterrupt:
    GPIO.cleanup()


