from flask import Flask, Response, request
from flask_cors import CORS, cross_origin
from flask_socketio import SocketIO, send, emit
from db import init_db, get_ducky, update_ducky_location, get_all_duckies
import json

app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['SECRET_KEY'] = 'Woweweweoahwoah'
cors = CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*")


class BadRequestException(Exception):
    pass

@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
  return response

@app.route('/')
@cross_origin()
def get_duckies():
    duckies_list = get_all_duckies()

    return json.dumps(duckies_list, default=str)


@app.route('/location', methods=['POST'])
@cross_origin()
def update_location():
    try:
        ducky_id = request.json['ducky_id']
        location_id = request.json['location_id']
        if not isinstance(ducky_id, int) or not isinstance(location_id, int):
            raise BadRequestException
    except KeyError:
        return Response(status=400)
    except BadRequestException:
        return Response(status=400)

    update_ducky_location(ducky_id=ducky_id, location_id=location_id)

    return Response(status=204)


@ socketio.on('message')
def handle_json(json_data):
    # todo error handling
    # todo this shouldn't take 2 seconds - possibly optimize db connections
    ducky_id = json_data['ducky_id']
    location_id = json_data['location_id']
    update_ducky_location(ducky_id=ducky_id, location_id=location_id)
    duckies_list = get_all_duckies()
    response = json.dumps(duckies_list, default=str)
    print(response)
    emit('update', response, broadcast=True)


if __name__ == '__main__':
    init_db()
    socketio.run(app)
