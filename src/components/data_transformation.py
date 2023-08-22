import os
from src.logging import logger
import pandas as pd
import numpy as np
import geopy.distance
import pickle

from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler,OneHotEncoder
from sklearn.pipeline import Pipeline

from src.entity import DataTransformationConfig

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config
        
    
class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config
        
    def feature_eng(self):
        train = pd.read_csv(self.config.train_path)
        test = pd.read_csv(self.config.test_path)
        
        
        train.replace('NaN', float(np.nan), regex=True, inplace=True)
        test.replace('NaN', float(np.nan), regex=True, inplace=True)
        
        train['Weatherconditions']=train['Weatherconditions'].str.split(" ", expand=True)[1]
        train['Time_taken(min)']=train['Time_taken(min)'].str.split(" ", expand=True)[1]
        
        test['Weatherconditions']=test['Weatherconditions'].str.split(" ", expand=True)[1]
        
        num_cols = ['Delivery_person_Age','Delivery_person_Ratings','Restaurant_latitude','Restaurant_longitude',
            'Delivery_location_latitude','Delivery_location_longitude','Vehicle_condition','multiple_deliveries',
            'Time_taken(min)']
        for col in num_cols:
            train[col]=train[col].astype('float64')
            
        for col in num_cols[:-1]:
            test[col]=test[col].astype('float64')
        
        
        return train, test
            
    def distance(self, train, test):
    
        train['Restaurant_latitude'] = train['Restaurant_latitude'].abs()
        train['Restaurant_longitude'] = train['Restaurant_longitude'].abs()
        
        restaurant_coordinates = train[['Restaurant_latitude', 'Restaurant_longitude']].to_numpy()
        delivery_location_coordinates = train[['Delivery_location_latitude', 'Delivery_location_longitude']].to_numpy()
        
        Distance = []
        for i in range(len(train)):
            dist = geopy.distance.geodesic(restaurant_coordinates[i], delivery_location_coordinates[i]).km
            Distance.append(dist)

        train['Distance'] = Distance
        
        test['Restaurant_latitude'] = test['Restaurant_latitude'].abs()
        test['Restaurant_longitude'] = test['Restaurant_longitude'].abs()
        
        restaurant_coordinates = test[['Restaurant_latitude', 'Restaurant_longitude']].to_numpy()
        delivery_location_coordinates = test[['Delivery_location_latitude', 'Delivery_location_longitude']].to_numpy()
        
        Distance = []
        for i in range(len(test)):
            dist = geopy.distance.geodesic(restaurant_coordinates[i], delivery_location_coordinates[i]).km
            Distance.append(dist)

        test['Distance'] = Distance
        
        drop_cols = ['ID', 'Delivery_person_ID', 'Time_Orderd','Time_Order_picked', 'Restaurant_latitude',
            'Restaurant_longitude','Delivery_location_latitude', 'Delivery_location_longitude',
            'Order_Date']
        
        train.drop(drop_cols, axis=1, inplace=True)
        test.drop(drop_cols, axis=1, inplace=True)
        
        train.to_csv(r"E:\Food_Delivery\artifacts\data_ingestion\Final_train.csv", index=False)
        test.to_csv(r"E:\Food_Delivery\artifacts\data_ingestion\Final_test.csv", index=False)
        return train, test

    def data_transformer(self):
        categorical_columns = ['Type_of_order','Type_of_vehicle','Festival','City',
                               'Road_traffic_density', 'Weatherconditions']
        
        numerical_columns=['Delivery_person_Age','Delivery_person_Ratings','Vehicle_condition',
                              'multiple_deliveries','Distance']

        # Numerical pipeline
        numerical_pipeline = Pipeline(steps = [
            ('impute', SimpleImputer(strategy = 'constant', fill_value=0)),
            ('scaler', StandardScaler(with_mean=False))
        ])

        # Categorical Pipeline
        categorical_pipeline = Pipeline(steps = [
            ('impute', SimpleImputer(strategy = 'most_frequent')),
            ('onehot', OneHotEncoder(handle_unknown = 'ignore')),
            ('scaler', StandardScaler(with_mean=False))
        ])

        preprocessor = ColumnTransformer([
            ('numerical_pipeline', numerical_pipeline,numerical_columns),
            ('categorical_pipeline', categorical_pipeline,categorical_columns)
        ])
        
        return preprocessor
        
    
    def initiate_data_transformation(self):
        train, test = self.feature_eng()
        self.distance(train, test)
        preprocessor = self.data_transformer()
        
        
    
        X_train = train.drop('Time_taken(min)', axis = 1)
        X_test = test
        y_train = train['Time_taken(min)']
        
        
        X_train = preprocessor.fit_transform(X_train)
        X_test = preprocessor.transform(X_test)
        
        preprocessor_path = self.config.preprocessor_model_path
        
        logger.info(f"Saving preprocessor pickle file at {preprocessor_path}")
        
        with open(preprocessor_path, 'wb') as file:
            pickle.dump(preprocessor, file)
    
        
            
        