from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route('/get_team_names', methods=['GET'])
def get_team_names():
    response = jsonify({
        'teams': util.get_team_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

@app.route('/predict_runs', methods=['POST'])
def predict_runs():
    balls_faced = float(request.form['balls_faced'])

    fours = float(request.form['fours'])
    sixes = float(request.form['sixes'])
    teams = request.form['teams']

    response = jsonify({
        'estimated_runs': util.get_estimated_runs(balls_faced,fours,sixes,teams)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    util.load_saved_artifacts()
    app.run()
