# -*- coding: utf-8 -*-

import json
import datetime
import time

from gevent.pywsgi import WSGIServer
from geventwebsocket.handler import WebSocketHandler

from flask import Flask, render_template, request, redirect

app = Flask(__name__)
app.config.from_object(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0  # Disable the stupid cache mechanism


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/pipe')
def pipe():
    if request.environ.get('wsgi.websocket'):
        ws = request.environ['wsgi.websocket']
        while True:
            time.sleep(1)
            message = ws.receive()
            if message is None:
                break
            datetime_now = datetime.datetime.now()
            data = {
                'time': str(datetime_now),
                'message': message
            }
            ws.send(json.dumps(data))
            print(message)
            print(data)
    return


@app.route('/login')
def login():
    return render_template('form.html')


@app.route('/register', methods=["POST"])
def register():
    display_name = request.form['display-name']
    price = request.form['price']
    description = request.form['description']
    email = request.form['email']
    psw = request.form['psw']
    print(display_name, price, description, email, psw)
    return redirect('/')

if __name__ == '__main__':
    app.debug = True

    host = 'localhost'
    port = 8080
    host_port = (host, port)

    server = WSGIServer(
        host_port,
        app,
        handler_class=WebSocketHandler
    )
    server.serve_forever()