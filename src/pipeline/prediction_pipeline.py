import pandas as pd
import pickle


class PredictionPipeline:
    def __init__(self):
        pass
    
    def predict(self, features):
        try:
            model_path = r"artifacts\models\DeliveryModel.pkl"
            with open(model_path, 'rb') as file:
                model = pickle.load(file)
                
            preprocessor_path = r"artifacts\models\Preprocessor.pkl"
            with open(preprocessor_path, 'rb') as file:
                preprocessor = pickle.load(file)
            
            data_scaled = preprocessor.transform(features)
            pred = model.predict(data_scaled)
            return pred
        except Exception as e:
            raise e
        
class CustomData:
    def __init__(self,
                 Delivery_person_Age: int,
                 Delivery_person_Ratings:int,
                 Weatherconditions: str,
                 Road_traffic_density:str,
                 Vehicle_condition: int,
                 Type_of_order: str,
                 Type_of_vehicle: str,
                 multiple_deliveries: int,
                 Festival: str,
                 City: str,
                 Distance: int):
        
        self.Delivery_person_Age = Delivery_person_Age
        self.Delivery_person_Ratings = Delivery_person_Ratings
        self.Weatherconditions = Weatherconditions
        self.Road_traffic_density = Road_traffic_density
        self.Vehicle_condition = Vehicle_condition
        self.Type_of_order = Type_of_order
        self.Type_of_vehicle = Type_of_vehicle
        self.multiple_deliveries = multiple_deliveries
        self.Festival = Festival
        self.City = City
        self.Distance = Distance
        
    def get_data_as_dataframe(self):
        try:
            custom_data_input_dict = {
                "Delivery_person_Age": [self.Delivery_person_Age],
                "Delivery_person_Ratings": [self.Delivery_person_Ratings],
                "Weatherconditions": [self.Weatherconditions],
                "Road_traffic_density": [self.Road_traffic_density],
                "Vehicle_condition": [self.Vehicle_condition],
                "Type_of_order": [self.Type_of_order],
                "Type_of_vehicle": [self.Type_of_vehicle],
                "multiple_deliveries": [self.multiple_deliveries],
                "Festival": [self.Festival],
                "City": [self.City],
                "Distance": [self.Distance]
            }
            return pd.DataFrame(custom_data_input_dict)
        
        except Exception as e:
            raise e    
        
    


