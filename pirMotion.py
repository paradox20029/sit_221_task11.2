from gpiozero import MotionSensor
from gpiozero import LED
led=LED(17)
pir = MotionSensor(26)

while True:
	pir.wait_for_motion()
	print("patient detected")
    led.on()
    pir.wait_for_no_motion()
    print("patient not detected")
    led.off()