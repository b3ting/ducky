from flask import Flask, Response, request
from db import init_db, update_ducky_location, get_all_duckies
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

    return Response(status=201)


if __name__ == '__main__':
    app.run()
    init_db()
