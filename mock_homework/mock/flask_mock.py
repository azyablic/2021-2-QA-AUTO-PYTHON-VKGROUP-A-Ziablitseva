import json
import threading

from flask import Flask, request

import mock_homework.settings as settings

app = Flask(__name__)

SURNAME_DATA = {}


@app.route('/get_surname/<name>', methods=['GET'])
def get_user_surname(name):
    if surname := SURNAME_DATA.get(name):
        return json.dumps({'surname': surname}), 200
    else:
        return json.dumps(f'User {name} not found'), 404


@app.route('/add_user', methods=['POST'])
def post_user_surname():
    data = request.json()
    name = list(data.keys())[0]
    surname = data[name]
    if name in SURNAME_DATA.keys():
        return json.dumps(f'User {name} already exists'), 400
    else:
        SURNAME_DATA[name] = surname
        return json.dumps({name: surname}), 201


@app.route('/put_surname/<name>', methods=['PUT'])
def put_user_surname(name):
    new_surname = request.get_json()['surname']
    if name in SURNAME_DATA.keys():
        SURNAME_DATA[name] = new_surname
        return json.dumps({name: SURNAME_DATA[name]}), 201
    else:
        return json.dumps(f'User {name} not fount'), 400


@app.route('/delete_surname/<name>', methods=['DELETE'])
def delete_user_surname(name):
    if SURNAME_DATA.get(name):
        del SURNAME_DATA[name]
        return json.dumps({'status': 'Ok'}), 200
    else:
        return json.dumps(f'User {name} not found'), 404

def run_mock():
    server = threading.Thread(target=app.run, kwargs={
        'host': settings.MOCK_HOST,
        'port': settings.MOCK_PORT
    })
    server.start()
    return server

def shutdown_mock():
    terminate_func = request.environ.get('werkzeug.server.shutdown')
    if terminate_func:
        terminate_func()


@app.route('/shutdown')
def shutdown():
    shutdown_mock()
    return json.dumps(f'Ok, exiting'), 200
