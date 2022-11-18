""""This is my arms constructer"""

class Arms:
    def __init__(self, actuator, sensors, powersystem, receiver,armhydraulics) -> None:
        actuator = actuator
        sensors = sensors
        powersystem = powersystem
        receiver = receiver
        armhydraulics = armhydraulics
    def receiveMotionInput(self):
        print('Receive inputs from Motion Processor')
    def shiftArmUp(self):
        print('Moving Arm Upwards')
    def shiftArmDown(self):
        print('Moving Arm Down')
    def shiftArmLeft(self):
        print('Moving arm Left')
    def shiftArmRight(self):
        print('Moving Arm Right')