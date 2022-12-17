import os
from typing import Tuple
import MySQLdb

def get_db_conn():
    conn = MySQLdb.connect(
        host= os.environ["HOST"],
        user=os.environ["DB_USERNAME"],
        passwd= os.environ["DB_PASSWORD"],
        db= os.environ["DATABASE"])
    return conn


def init_db():
    conn = get_db_conn()
    cur = conn.cursor()

    cur.execute('''
        CREATE TABLE IF NOT EXISTS owner (
        id serial PRIMARY KEY,
        name varchar (150) NOT NULL,
        ip_address varchar (150),
        object_created datetime DEFAULT CURRENT_TIMESTAMP);
    ''')

    cur.execute('''
        CREATE TABLE IF NOT EXISTS ducky (
        id serial PRIMARY KEY,
        name varchar (150) NOT NULL,
        owner_id int NOT NULL REFERENCES owner(id),
        location_id int NOT NULL REFERENCES owner(id),
        object_created datetime DEFAULT CURRENT_TIMESTAMP);
    ''')

    # todo move to migrations dir!
    # cur.execute('''
    #     INSERT INTO owner (id, name) VALUES (1, 'Rad Brad');
    # ''')

    # cur.execute('''
    #     INSERT INTO owner (id, name) VALUES (2, 'Toot');
    # ''')

    # cur.execute('''
    #     INSERT INTO ducky (id, name, owner_id, location_id) VALUES (1, 'Lucky', 1, 1); 
    # ''')

    conn.commit()

    cur.close()
    conn.close()


def get_ducky(ducky_id: int) -> Tuple[int, int]:
    conn = get_db_conn()
    cur = conn.cursor()
    cur.execute(
        "SELECT id, location_id FROM ducky WHERE id = %s", str(ducky_id))
    result = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()
    return result


def get_all_duckies():
    conn = get_db_conn()
    cur = conn.cursor()
    query_sql = "SELECT * FROM ducky"
    cur.execute(query_sql)
    results = cur.fetchall()
    cur.close()
    conn.close()
    return results


def update_ducky_location(ducky_id: int, location_id: int):
    conn = get_db_conn()
    cur = conn.cursor()
    cur.execute("UPDATE ducky SET location_id = %s WHERE id = %s",
                (location_id, ducky_id))
    conn.commit()
    cur.close()
    conn.close()
