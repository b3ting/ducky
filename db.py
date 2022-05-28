import os
import psycopg2

DATABASE_URL = os.environ['DATABASE_URL']

def get_db_conn():
  conn = psycopg2.connect(DATABASE_URL, sslmode='require')
  # conn = psycopg2.connect(
  #   host="localhost",
  #   database="shippo",
  #   user="appuser",
  #   password="123123123")

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




init_db()