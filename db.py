import os
import psycopg2

DATABASE_URL = 'postgres://snfzjbzottankj:863d78821e6ea8be9a60abe9fd829eed951cbcf100707bb3861ea0667c7df423@ec2-44-196-174-238.compute-1.amazonaws.com:5432/d8fitsasagpcfa'

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

def update_ducky_location(ducky_id, location_id):
  conn = get_db_conn()
  cur = conn.cursor()
  cur.execute("UPDATE ducky SET location_id = %s WHERE id = %s", (location_id, ducky_id))
  conn.commit()
  cur.close()
  conn.close()