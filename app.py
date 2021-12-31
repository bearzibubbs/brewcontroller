#!/usr/bin/python3

import controller.simple_pid
import time
import sys
#import spidev
import controller.pwm 

def pid_loop(currentTemp):
    

    # Need following information from the cli
    # get Kp, Ki, Kd values - Default values available
    # get collection interval - Defaults values available
    # get PID mode {boil, mash}
    # get duration of loop in minutes
    # temp setpoint

    PID(currentTemp)        



if __name__ == "__main__":
    # should I def the main loop and then just put it here?
    
    # for CLI - to be removed
    # error out if too many args, need to add test for proper int type
    
    args = sys.argv[1:]    
    for arg in args:
        if arg == '-h':
            print('app.py <setTemp>')
            sys.exit()
    if len(args) > 1:
        print('Too many argumnents')
        sys.exit()


    # set up the env with vars

    setTemp = int(args[0])
    start = time.time()
    duration = 1 
    t_end = start + duration * 60

    # Connect to pt100 with spidev
    # pt100spi = spidev.SpiDev()
    # pt100spi.open(bus, device) -> needs bus and device name, needs a test with raspi
    # pt100spi.threewire = true
    pt100_temp = 100


    PID = controller.simple_pid.PID(Kp=1, Ki=1, Kd=1, setpoint=setTemp, sample_time=1)
    PWM = controller.pwm(1/PID.sample_time)
    PWM.startPWM(0)

    while (time.time() < t_end ):

        # get pt100 temp reading
        # pt100_temp = pt100spi.readbytes(n) spidev something someting

        latest = pid_loop(pt100_temp)
        PWM.updatePWM(latest)
        print(time.time(), t_end)

    PID.reset()
