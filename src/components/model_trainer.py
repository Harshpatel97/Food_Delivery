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
        train = pd.read_csv(self.config.train_path)
        test = pd.read_csv(self.config.test_path)
        
        X_train = train.drop('Time_taken(min)', axis = 1)
        X_test = test
        y_train = train['Time_taken(min)']
        
        preprocessor_path = self.config.preprocessor_model_path
        
        with open(preprocessor_path, 'rb') as file:
            preprocessor = pickle.load(file)
            
        
        X_train = preprocessor.fit_transform(X_train)
        X_test = preprocessor.transform(X_test)
        
        
        rf = RandomForestRegressor()
        
        rf.fit(X_train, y_train)
        
        rf_model = self.config.model_path
        
        logger.info(f"Saving model.pkl file at {rf_model}")
        
        with open(rf_model, 'wb') as file:
            pickle.dump(rf, file)
        