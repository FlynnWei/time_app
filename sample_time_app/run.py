from flask import Flask
from datetime import datetime
app = Flask(__name__)


@app.route('/time')
def current_time():
    return str(datetime.today())

@app.route('/')
def hello_world():
    return 'Hello world!'


app.run(host='0.0.0.0',
        port=8081,
        debug=True)
