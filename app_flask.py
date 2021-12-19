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

@app.route('/api/v1/runpid', methods=['POST', 'PUT'])
def api_runpid():

    if not request.is_json():
        return "yo this ain't json"
    if request.methods == 'POST':
        setTemp = request.get_json()['setTemp']
        pid = controller.simple_pid.PID(Kp=1, Ki=1, Kd=1, setPoint=setTemp, sample_time=1)

        start = time.time()
        duration = 1 
        t_end = start + duration * 60

        currTemp = 1
        pid(currTemp)
    elif request.methods == 'PUT':
        setTemp = request.get_json()['setTemp']
        currTemp = 1
        pid(currTemp)

app.run()