from flask import Flask, render_template, jsonify
# from flask.ext.socketio import SocketIO, emit
from flask.ext.restful import Api, Resource
from mare_db import MareService

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
api = Api(app)
# socketio = SocketIO(app)

mare_service = MareService()

@app.route("/")
def hello():
    return "Hello World!"


class ClientApi(Resource):
	"""Api restful for client domain class"""
	def get(self, id):
		client = mare_service.get_client_by_id(id)
		return jsonify(client.to_map() if client else {})



api.add_resource(ClientApi, '/client/<int:id>', endpoint = 'client')

if __name__ == '__main__':
    app.run()
    # socketio.run(app)

