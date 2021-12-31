import RPi.GPIO as IO


class PWM:

    def __init__(self, freq):
        IO.setmode(IO.BCM)
        IO.setup(19, IO.OUT)
        self.PWM = IO.PWM(19, freq)


    def startPWM(self, dutycycle):
        self.PWM.start(dutycycle)

    def updatePWM(self, dutycycle):
        self.PWM.ChangeDutyCycle(dutycycle)



