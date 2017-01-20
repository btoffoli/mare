from flask import Flask, render_template
# from flask.ext.socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
# socketio = SocketIO(app)


@app.route("/")
def hello():
    return "Hello World!"



if __name__ == '__main__':
    app.run()
    # socketio.run(app)

