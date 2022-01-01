import RPi.GPIO as IO


class PWM:

    def __init__(self, freq):
        IO.setmode(IO.BCM)
        IO.setup(19, IO.OUT)
        self.PWM = IO.PWM(13, freq)


    def startPWM(self, dutycycle):
        self.PWM.start(dutycycle)

    def updatePWM(self, dutycycle):
        self.PWM.ChangeDutyCycle(dutycycle)

    def reset(self):
        IO.output(13, IO.LOW)
        self.PWM = IO.PWM(13, 0)
        self.updatePWM(0)
        IO.cleanup(13)

    def __del__(self):
        self.reset()



