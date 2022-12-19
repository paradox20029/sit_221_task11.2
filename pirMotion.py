from gpiozero import MotionSensor #importing the motion sensor libraries and led
from gpiozero import LED
led=LED(17) #defining the GPIO pin for the led and motion sensor
pir = MotionSensor(26)

while True:
    pir.wait_for_motion() #using the inbuilt method to intiate the sensor when the person comes in the range
    print("patient detected") #printing message in accordance to the detection
    led.on()
    pir.wait_for_no_motion()
    print("patient not detected")
    led.off()
