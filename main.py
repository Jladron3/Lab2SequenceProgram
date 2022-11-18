

class KivaMain:
    def __init__(self, systemsCommunication, systemsInformation, mainframePower, model) -> None:
        systemsCommunication = systemsCommunication
        systemsInformation = systemsInformation
        mainframePower = mainframePower
        model = model
    def receiveInput(self):
        return 'Receive action from Controller'
    def kivaOn(self):
        print('Turn Kiva on')
    def KivaOff(self):
        print('Turn Kiva Off')
    def startMotion(self):
        print('Engine On')
    def haltMotion(self):
        print('Idle Engine')
