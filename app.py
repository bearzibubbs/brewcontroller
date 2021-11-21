import controller.simple_pid
import datetime

def pid_loop(self):
    

    # Need following information from the front end 
    # get Kp, Ki, Kd values - Default values available
    # get collection interval - Defaults values available
    # get PID mode {boil, mash}
    # get duration of loop in minutes
    # temp setpoint
    start = datetime.now()

    PID = controller.simple_pid.PID()
    PID.tunings(Kp, Ki, Kd)


    while ( flag && datetime.now()-start < duration ):
        #get temp from MAX
        settemp =  None # need to get this from front end
        PID(settemp)        
    PID.reset()

if __name__ == "__main__":
    # should I def the main loop and then just put it here?