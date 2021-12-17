import flask
from flask import request, jsonify
import controller.simple_pid


app = flask.Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return ''' <h1> index </h1>
    <p> This is the main page for now </p>
    '''

@app.route('/api/v1/initpid', methods=['POST', 'PUT'])
def api_initpid():

    if !request.is_json():
        return "yo this ain't json"

    setTemp = request.get_json()['setTemp']
    pid = controller.simple_pid.PID(Kp=1, Ki=1, Kd=1, setPoint=setTemp, sample_time=1)

 
 app.run()