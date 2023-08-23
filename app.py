import pickle
from flask import Flask, request, render_template
import numpy as np
import pandas as pd

from src.pipeline.prediction_pipeline import CustomData, PredictionPipeline


application = Flask(__name__)
app = application

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/prediction', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        data = CustomData(
            Delivery_person_Age = request.form.get('Delivery_person_Age'),
            Delivery_person_Ratings = request.form.get('Delivery_person_Ratings'),
            Weatherconditions = request.form.get('Weatherconditions'),
            Road_traffic_density = request.form.get('Road_traffic_density'),
            Vehicle_condition = request.form.get('Vehicle_condition'),
            Type_of_order = request.form.get('Type_of_order'),
            Type_of_vehicle = request.form.get('Type_of_vehicle'),
            multiple_deliveries = request.form.get('multiple_deliveries'),
            Festival = request.form.get('Festival'),
            City = request.form.get('City'),
            Distance = request.form.get('Distance')
            )
        
        pred_df = data.get_data_as_dataframe()
        print(pred_df)
        
        predict_pipeline = PredictionPipeline()
        results = predict_pipeline.predict(pred_df)
        return render_template('home.html', results=results[0])
    
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
        