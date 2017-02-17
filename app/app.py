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
		client = mare_service.get_by_id('Client', id)
		return jsonify(client.to_map() if client else {})

	def list(self, limit=10, offset=0):		
		clients = mare_service.list('Client', limit, offset)
		clients_json = map(lambda i: i.to_map(), clients) if clients else []
		return jsonify(clients_json)



api.add_resource(ClientApi, '/client/<int:id>', endpoint = 'client')
api.add_resource(ClientApi, '/client/list', endpoint = 'list')

if __name__ == '__main__':
    app.run(debug=True)
    # socketio.run(app)

