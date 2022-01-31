import RPi.GPIO as IO


class PWM:

    def __init__(self, pin):
        self._pin = pin
        self._freq = 0

        IO.setmode(IO.BCM)
        IO.setup(pin, IO.OUT)
    
    def startPWM(self, freq):
        self.PWM = IO.PWM(self._pin, freq)
    
    def getInstance(self):
        return self.PWM
    
    def updatePWM(self, newFreq):
        self.PWM = IO.PWM(self._pin, newFreq)

    def reset(self):
        IO.output(self._pin, IO.LOW)
        return "Pin " + str(self._pin) + " has been set to IO.LOW and PWM freq and dutycycle set to 0."

    def __del__(self):
        self.reset()
        IO.cleanup(self._pin)
        return "Pin " + str(self._pin) + " has been set to IO.LOW and PWM object has been cleared."



