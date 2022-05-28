from flask import Flask
from db import init_db, update_ducky_location

app = Flask(__name__)

@app.route('/')
def hello_world():
    update_ducky_location(1, 1)
    return 'Updated ducky location!'

if __name__ == '__main__':
    app.run()
    init_db()