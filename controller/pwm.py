import RPi.GPIO as IO


class PWM:

    def __init__(self, pin, freq):
        self._pin = pin
        self._freq = freq

        IO.setmode(IO.BCM)
        IO.setup(pin, IO.OUT)
        self.PWM = IO.PWM(self._pin, self._freq)
    
    def startPWM(self, dutycycle):
        self.PWM.start(dutycycle)
    
    def getInstance(self):
        return self.PWM
    
    def updatePWM(self, newDutycycle):
        self.PWM.ChangeDutyCycle(newDutycycle)

"""     def reset(self):
        IO.output(self._pin, IO.LOW)
        return "Pin " + str(self._pin) + " has been set to IO.LOW and PWM freq and dutycycle set to 0."

    def __del__(self):
        self.reset()
        IO.cleanup(self._pin)
        return "Pin " + str(self._pin) + " has been set to IO.LOW and PWM object has been cleared."
 """


