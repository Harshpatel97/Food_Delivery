import os
from src.logging import logger
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
import pickle

from src.entity import ModelTrainerConfig

scaler=StandardScaler()


class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config
        
    def initiate_model_training(self):
        data = pd.read_csv(self.config.data_path)
        X = data.drop('Time_taken(min)', axis = 1)
        y = data['Time_taken(min)'] 
        
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)
        
        X_train = scaler.fit_transform(X_train)
        X_test = scaler.transform(X_test)
        
        
        rf = RandomForestRegressor()
        
        rf.fit(X_train, y_train)
        
        rf_model = self.config.model_path
        
        with open(rf_model, 'wb') as file:
            pickle.dump(rf, file)