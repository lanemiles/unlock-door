from gpiozero import OutputDevice
from time import sleep

class DoorUnlocker:
    self.GPIO_PIN = 18
    def __init__():
        self.output_device = OutputDevice(self.GPIO_PIN)
        
    def unlock_door(self):
        try:
            self.output_device.on()
            sleep(3)
            self.output_device.off()
        except Exception e:
            self.output_device.off()
