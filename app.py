from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np

app = Flask(__name__)

# Load the model
model = joblib.load('linear_regression_model.pkl')

# Define a route for the index page
@app.route('/')
def index():
    return render_template('index.html')

# Define a route for the prediction
@app.route('/predict', methods=['POST'])
def predict():
    # Get the JSON data from the request
    data = request.get_json(force=True)
    # Convert JSON data to numpy array
    features = np.array(data['features']).reshape(1, -1)
    # Make prediction
    prediction = model.predict(features)
    # Return prediction as JSON response
    return jsonify(prediction=prediction.tolist())

if __name__ == '__main__':
    app.run(debug=True)
