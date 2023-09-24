import os
from typing import Tuple
import redis

pool = redis.ConnectionPool(host='red-ck7pfb08elhc73c3a5rg', port=6379, db=0)
r = redis.Redis(connection_pool=pool)

def get_db_conn():
    r = redis.Redis(host='red-ck7pfb08elhc73c3a5rg', port=6379, decode_responses=True)
    return r

def init_db():
    # r = get_db_conn()

    r.hset("owner:1", mapping={
        'id': 1,
        'name': 'Rad Brad'
    })
    r.hset("owner:2", mapping={
        'id': 2,
        'name': 'Toot'
    })
    r.hset("ducky:1", mapping={
        'id': 1,
        'name': 'Lucky',
        'owner_id': 1,
        'location_owner_id': 1
    })


def get_ducky(ducky_id: int) -> Tuple[int, int]:
    # r = get_db_conn()

    r.hgetall("ducky:%d" % ducky_id)
    return result

def get_all_duckies():
    # r = get_db_conn()

    values = []
    keys = r.keys("ducky:*")
    for key in keys:
        value = r.hgetall(key)
        values.append(value)
    return values

def update_ducky_location(ducky_id: int, location_id: int):
    # r = get_db_conn()

    r.hset("ducky:%d" % ducky_id, mapping={
        'location_id': location_id
    })
