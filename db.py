import os
import psycopg2
from psycopg2.extras import RealDictCursor

DATABASE_URL = os.environ['DATABASE_URL']


def get_db_conn():
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    return conn


def init_db():
    conn = get_db_conn()
    cur = conn.cursor()

    cur.execute('CREATE TABLE IF NOT EXISTS owner (id serial PRIMARY KEY,'
                'name varchar (150) NOT NULL,'
                'ip_address varchar (150),'
                'object_created date DEFAULT CURRENT_TIMESTAMP);'
                )

    cur.execute('CREATE TABLE IF NOT EXISTS ducky (id serial PRIMARY KEY,'
                'name varchar (150) NOT NULL,'
                'owner_id int REFERENCES owner(id) NOT NULL,'
                'location_id int REFERENCES owner(id) NOT NULL,'
                'object_created date DEFAULT CURRENT_TIMESTAMP);'
                )

    conn.commit()

    cur.close()
    conn.close()


def get_all_duckies():
    conn = get_db_conn()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    query_sql = "SELECT * FROM ducky"
    cur.execute(query_sql)
    results = cur.fetchall()
    cur.close()
    conn.close()
    return results


def update_ducky_location(ducky_id, location_id):
    conn = get_db_conn()
    cur = conn.cursor()
    cur.execute("UPDATE ducky SET location_id = %s WHERE id = %s",
                (location_id, ducky_id))
    conn.commit()
    cur.close()
    conn.close()
