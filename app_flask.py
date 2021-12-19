import flask
from flask import request, jsonify
import controller.simple_pid
import time

app = flask.Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return ''' <h1> index </h1>
    <p> This is the main page for now </p>
    '''

@app.route('/api/v1/updatepid', methods=['POST', 'PUT'])
def api_updatepid():

    if not request.is_json:
        return "yo this ain't json"
    if request.method == 'POST':
        setTemp = int(request.get_json()['setTemp'])
    elif request.method == 'PUT':
        setTemp = request.get_json()['setTemp']
        currTemp = 1
        pid(currTemp)

@app.route('/api/v1/getPID', methods=['GET'])
def api_getPID():
    try: 
        pid
    except NameError:
        var_exists = False
    else: 
        var_exists = True
        
    if not var_exists:
        return "PID is not initialized"    
    
    return pid.dutycycle(), 200

pid = controller.simple_pid.PID(Kp=1, Ki=1, Kd=1, setpoint=0, sample_time=1)

""" Timing code placeholder 
        start = time.time()
        duration = 1 
        t_end = start + duration * 60
"""

print( "PID initialized" )

app.run()