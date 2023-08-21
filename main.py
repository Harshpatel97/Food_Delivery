from src.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.pipeline.stage_02_data_transformation import DataTransformationTrainingPipeline
from src.pipeline.stage_03_model_trainer import ModelTrainerPipeline
from src.logging import logger


STAGE_NAME = 'Data Ingestion'

try:
    logger.info(f">>>>>>>{STAGE_NAME} started <<<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e
    
STAGE_NAME1 = 'Data Transformation'

try:
    logger.info(f">>>>>>>{STAGE_NAME1} started <<<<<<<")
    data_ingestion = DataTransformationTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> stage {STAGE_NAME1} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e
    
    
STAGE_NAME2 = 'Model Trainer'

try:
    logger.info(f">>>>>>>{STAGE_NAME2} started <<<<<<<")
    data_ingestion = ModelTrainerPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> stage {STAGE_NAME2} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e