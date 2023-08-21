from src.config.configuration import ConfigurationManager
from src.components.model_trainer import ModelTrainer
from src.logging import logger


class ModelTrainerPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer = ModelTrainer(config = model_trainer_config)
        model_trainer.initiate_model_training()