from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np
import pandas as pd

app = Flask(__name__)

# Load the model
data=pd.read_csv('E:\CODES\Scripts\Cleaned_data.csv')
model = pickle.load(open('E:\CODES\Scripts\RidgeModel.pkl', 'rb'))
locations=sorted(data['location'].unique())

@app.route('/')
def home():
    return render_template('index.html',locations=locations)

@app.route('/predict', methods=['POST'])
def predict():
    # Retrieve values from form
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])
    sqft = float(request.form['sqft'])

    if bhk<=0 or bath<=0 or sqft<=0:
        return jsonify({'error': 'Invalid input values. Please try again with valid inputs.'})

    # Convert data into DataFrame (ensure it matches the input expected by the model)
    input_data = pd.DataFrame([[location, bhk, bath, sqft]], columns=['location', 'bhk', 'bath', 'total_sqft'])


    prediction = model.predict(input_data)[0]

    return render_template('index.html', locations=locations, prediction_text='Predicted Price: {} Lakhs'.format(round(prediction, 2)))

if __name__ == "__main__":
    app.run(debug=True)