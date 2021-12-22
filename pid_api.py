import flask
from flask import request, jsonify
import controller.simple_pid
import time


app = flask.Flask(__name__)
pid = controller.simple_pid.PID()

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

@app.route('/api/v1/getpid', methods=['GET'])
def api_getpid():
    if not pid.dutycycle:
        return "Pid loop not engaged \n"    
    return jsonify(pid.dutycycle)


if __name__ == "__main__":
    app.run()


""" Timing code placeholder 
        start = time.time()
        duration = 1 
        t_end = start + duration * 60
"""


