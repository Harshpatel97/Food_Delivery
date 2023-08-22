from src.utils import create_directories, read_yaml
from src.constants import *
from src.entity import (DataIngestionConfig, DataTransformationConfig, ModelTrainerConfig)

class ConfigurationManager:
    def __init__(self,
                config_filepath = CONFIG_FILE_PATH,
                params_filepath = PARAMS_FILE_PATH):
        
     
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
     
        create_directories([self.config.artifacts_root])    
     
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        
         
         
        config = self.config.data_ingestion      ## select the data_ingestion class from config.yaml
        create_directories([config.root_dir])    ## from data_ingestion create the given directory
         
        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir 
        )
        
        return data_ingestion_config 
    
    def get_data_transformation_config(self) -> DataTransformationConfig:
        config = self.config.data_transformation

        create_directories([config.root_dir])

        data_transformation_config = DataTransformationConfig(
            root_dir=config.root_dir,
            train_path=config.train_path,
            test_path=config.test_path,
            preprocessor_model_path=config.preprocessor_model_path
        )

        return data_transformation_config
    
    def get_model_trainer_config(self) -> ModelTrainerConfig:
        config = self.config.model_trainer

        create_directories([config.root_dir])

        model_trainer_config = ModelTrainerConfig(
            root_dir=config.root_dir,
            train_path=config.train_path,
            test_path=config.test_path,
            preprocessor_model_path=config.preprocessor_model_path,
            model_path=config.model_path
        )

        return model_trainer_config