import os
from src.logging import logger
import geopy.distance
import numpy as np
import pandas as pd

from src.entity import DataTransformationConfig

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config
        
    def feature_eng(self, data):
        data.replace('NaN', float(np.nan), regex=True, inplace=True)
        data['Weatherconditions']=data['Weatherconditions'].str.split(" ", expand=True)[1]
        data['Time_taken(min)']=data['Time_taken(min)'].str.split(" ", expand=True)[1]
        
        
        num_cols = ['Delivery_person_Age','Delivery_person_Ratings','Restaurant_latitude','Restaurant_longitude',
            'Delivery_location_latitude','Delivery_location_longitude','Vehicle_condition','multiple_deliveries',
            'Time_taken(min)']
        for col in num_cols:
            data[col]=data[col].astype('float64')
        
        return data
            
    def distance(self, data):
    
        data['Restaurant_latitude'] = data['Restaurant_latitude'].abs()
        data['Restaurant_longitude'] = data['Restaurant_longitude'].abs()
        
        restaurant_coordinates = data[['Restaurant_latitude', 'Restaurant_longitude']].to_numpy()
        delivery_location_coordinates = data[['Delivery_location_latitude', 'Delivery_location_longitude']].to_numpy()
        
        Distance = []
        for i in range(len(data)):
            dist = geopy.distance.geodesic(restaurant_coordinates[i], delivery_location_coordinates[i]).km
            Distance.append(dist)

        data['Distance(kms)'] = Distance
        
        return data

    def fill_na(self, data):
        
        data['Delivery_person_Age'].fillna(29, inplace=True) 
        data['Delivery_person_Ratings'].fillna(4.5, inplace=True)
        data['Weatherconditions'].fillna('Sunny', inplace=True)
        data['Road_traffic_density'].fillna('Low', inplace=True)
        data['multiple_deliveries'].fillna(1.0, inplace=True)
        data['Festival'].fillna('No', inplace=True)
        data['City'].fillna('Metropolitian', inplace=True)
        
        data.drop(['ID', 'Delivery_person_ID', 'Time_Orderd','Time_Order_picked', 'Restaurant_latitude',
            'Restaurant_longitude','Delivery_location_latitude', 'Delivery_location_longitude',
            'Order_Date'],axis=1,inplace=True)
        
        return data

    def cat_values(self, data):
        
        Road_encodes = {'Low ': 0, 'Medium ': 1, 'High ': 2, 'Jam ': 3, 'Low':0}
        Weather_encodes = {'Sunny': 0,'Cloudy': 1, 'Windy': 2, 'Fog': 3, 'Stormy': 4, 'Sandstorms': 5}
    
        data['Road_traffic_density'] = data['Road_traffic_density'].replace(Road_encodes)
        data['Weatherconditions'] = data['Weatherconditions'].replace(Weather_encodes)
        
        categorical_columns = [feature for feature in data.columns if data[feature].dtypes == "O"]
        data = pd.get_dummies(data, columns=categorical_columns, drop_first=True, dtype=int)
        
        return data
    
    
    def convert(self):
        df = pd.read_csv(self.config.data_path)
        feat = self.feature_eng(df)
        dist = self.distance(feat)
        nul = self.fill_na(dist)
        cat = self.cat_values(nul)
        cat.to_csv(r"E:\Food_Delivery\artifacts\data_ingestion\Final_train.csv", index=False)