import flask
from flask import request, jsonify, make_response
import controller.simple_pid
import time
import controller.pwm
import temperature.probe

app = flask.Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return ''' <h1> index </h1>
    <p> This is the main page for now </p>
    '''

@app.route('/api/v1/updatetargettemp', methods=['PUT'])
def api_updateTargetTemp():
    if not request.is_json:
        return "yo this ain't json"
    if not request.get_json()['setTemp']:
        return make_response(jsonify({"Incorrectly formatted call"}), 300)
    setTemp = request.get_json()['setTemp']
    return make_response(jsonify("Target temperature set to: " + setTemp), 200)

@app.route('/api/v1/piddutycycle', methods=['GET'])
def api_pidDutycycle():
    if not pidControl.dutycycle:
        return "Pid loop not engaged \n"    
    return make_response(jsonify(pidControl.dutycycle), 200)

@app.route('/api/v1/healtcheck', methods=['GET'])
def api_healthcheck():
    response = {
        "currentTemp": currentTemp
        ""
    }
    return make_response(jsonify("ok"), 200)


'''
@app.route('/api/v1/pidfrequency', methods=['GET'])
def api_pidFrequency():
    return make_response(jsonify(pidControl.frequency))
'''

if __name__ == "__main__":
    app.run()
    
    pidControl = controller.simple_pid.PID(Kp=1, Ki=1, Kd=1, setpoint=0, sample_time=0.05)

    start =  time.time()
    duration = 60
    end = start - duration * 60
    pulseOutput = controller.pwm(1/pidControl.sample_time, 13)

    currentTemp = temperature.probe()

    while (time.time() < end ):
        latest = pidControl(currentTemp.getTemp())
        pulseOutput.updatePWM(latest)
        print(time.time(), end)

    pulseOutput.reset()



""" Timing code placeholder 
        start = time.time()
        duration = 1 
        t_end = start + duration * 60
"""

