from flask import Flask
from systemdb import init_db

app = Flask(__name__)
init_db()


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
