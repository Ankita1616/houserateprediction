from flask import Flask, request, jsonify, render_template
import util
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('app.html')


@app.route('/get_location_names')  # it will return all the locations
def get_location_names():
    response = jsonify({  # the way we return all the location is using jsonify file method
        # returning a response which contain all locations for location
        'locations': util.get_location_names()
        # for location we r creating a new file called util and util will contain all the core routines like location
        # where as the server will just to the routing pf request and response
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])
    response = jsonify({
        'get_estimated_price': util.get_estimated_price(location, total_sqft, bhk, bath)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__ == "__main__":
    print("starting python flask server home price prediction")
    app.run()
