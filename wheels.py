"""This is my wheels constructer"""

class wheels:
    def __init__(self, resistance,rims,wheelHydraulics) -> None:
        resistance=resistance
        rims=rims
        wheelHydraulics=wheelHydraulics
    def wheelForwardMotion(self):
        print('Wheels Spin Forward')
    def wheelBackwardMotion(self):
        print('Wheels Spin Backward')
    def wheelIdle(self):
        print('Wheels remain still')
    def wheelHalt(self):
        print('Wheels come to a stop')