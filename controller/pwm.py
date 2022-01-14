import RPi.GPIO as IO


class PWM:

    def __init__(self, freq, pin):
        self._pin = pin
        self._freq = freq
        self.PWM = IO.PWM(self.pin, self.freq)

        IO.setmode(IO.BCM)
        IO.setup(self.pin, IO.OUT)

    def getInstance(self):
        return self.PWM
    
    def updatePWM(self, newFreq):
        self.PWM = IO.PWM(self.pin, newFreq)

    def reset(self):
        IO.output(self.pin, IO.LOW)
        self.PWM = IO.PWM(self.pin, 0)
        self.updatePWM(0)
        return "Pin " + self.pin + " has been set to IO.LOW and PWM freq and dutycycle set to 0."

    def __del__(self):
        self.reset()
        IO.cleanup(self.pin)
        return "Pin " + self.pin + " has been set to IO.LOW and PWM object has been cleared."



