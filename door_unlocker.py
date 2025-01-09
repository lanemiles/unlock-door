from gpiozero import OutputDevice
from time import sleep

class DoorUnlocker:
    GPIO_PIN = 18
    def __init__(self):
        self.output_device = OutputDevice(pin=self.GPIO_PIN, active_high=False)
        self.output_device.off()
        
    def unlock_door(self):
        try:
            self.output_device.on()
            sleep(3)
            self.output_device.off()
        except Exception as e:
            self.output_device.off()
            
    def get_status(self):
        return "UNLOCKED" if self.output_device.value == 1 else "LOCKED" 
