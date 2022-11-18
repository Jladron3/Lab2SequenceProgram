"""This is my MotionProcessor constructer"""

class MotionProcessor:
    def __init__(self, armJoints, axles, motionHydraulics, manipulator) -> None:
        armJoints=armJoints
        axles=axles
        motionHydraulics=motionHydraulics
        manipulator=manipulator
    def sendMotionInput(self):
        print('Send Motion signals to motion units')
    def setForwardMovementLight(g):
        print('Set Forward Motion Light to Green')
    def setBackwardMovementLight(r):
        print('Set Backword Movement Light to Red')
    def setIdleLight(y):
        print('Set Idle Light to Yellow')
    def motionGo(self):
        print('Ready to move')
    def motionStop(self):
        print('Kill motion commands')