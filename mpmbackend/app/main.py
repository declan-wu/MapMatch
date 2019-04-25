from flask import Flask, request, jsonify
from service import Service

app = Flask(__name__, static_url_path='/static')
service = Service()


@app.route("/")
def hello():
    return '', 200

@app.route("fullinsert")
def fullinsert():
    service.init()
    return '', 200

#To access parameters submitted in the URL (?key=value)
@app.route('/insert', methods=['POST'])
def insert():
    data = request.get_json()
    user = data['user']
    interest = data['interest']
    longitude = data['longitude']
    latitude = data['latitude']
    imgurl = data['imgurl']

    service.insert(user, interest, longitude, latitude, imgurl)
    return '', 200  

@app.route('/query')
def query():
    user = request.args.get('user')
    interest = request.args.get('interest')
    longitude = request.args.get('longitude')
    latitude = request.args.get('latitude')
    return jsonify(service.query(user, interest, longitude, latitude))

@app.route('/fullquery')
def fullquery():
    return jsonify(service.fullquery())

#prompt the user to enter their interest
@app.route('/interest/')
def interest():
	person = [
			{'user': 'Declan',
			'interest': ['reading, yikes','gaming','writing']
			}
			]
	return jsonify(person)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=False, port=5000)