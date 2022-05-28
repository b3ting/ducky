from flask import Flask, Response, request
from db import get_ducky, init_db, update_ducky_location, get_all_duckies
import json

app = Flask(__name__)


class BadRequestException(Exception):
    pass


@app.route('/')
def get_duckies():
    duckies_list = get_all_duckies()
    return json.dumps(duckies_list, default=str)


@app.route('/location', methods=['POST'])
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


@app.route('/travel')
def move_ducky_1():
    ducky = get_ducky(1)
    location_id = ducky[1]
    new_location = 1 if location_id == 2 else 2
    update_ducky_location(ducky_id=1, location_id=new_location)
    return Response(status=203)


if __name__ == '__main__':
    app.run()
    init_db()
