"""This is my sequence constructor"""
"""The idea of this code is in relation to my sequence diagram. Move a small object within the AutoDrive path of the robot to continue to desintation"""

def receiveInput():
    print('Receive command from Controller')
def sendMotionInput():
    print('Moving Forward towards goal line')
def wheelHalt():
    print('Wheels stopped due to object')
def motionHalt():
    print('Kill all x-axis motion inputs')
def shiftArmDown():
    print('Shift arm down to object')
def handClose():
    print('Close hand to grab object')
def shiftArmRight():
    print('Shift object to the right')
def handOpen():
    print('Open hand to release lego obstacle')
def wheelForwardMotion():
    print('Continue forward to goal')

receiveInput()
sendMotionInput()
wheelHalt()
motionHalt()
shiftArmDown()
handClose()
shiftArmRight()
handOpen()
wheelForwardMotion()