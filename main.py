from mlProject import logger
from mlProject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from mlProject.pipeline.stage_02_data_validation import DataValdationTrainingPipeline
from mlProject.pipeline.sage_03_data_transformation import DataTransformationTrainingPipelie
from mlProject.pipeline.stage_04_model_trainer import ModelTrainerTrainigPipeline
from mlProject.pipeline.stage_05_model_evaluation import ModelEvaluationTrainingPipeline

STAGE_NAME = "Data Ingestion Stage"


try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<\n\nx===============x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Data Validation Stage"

try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    obj = DataValdationTrainingPipeline()
    obj.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx===============x")
except Exception as e:
    raise e

STAGE_NAME = "Data Transformation Stage"
try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    obj = DataTransformationTrainingPipelie()
    obj.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx===============x")
except Exception as e:
    raise 

STAGE_NAME = "Model Training Stage"
try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    obj = ModelTrainerTrainigPipeline()
    obj.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx===============x")
except Exception as e:
    raise e    

STAGE_NAME = "Model Training Stage"
try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    obj = ModelEvaluationTrainingPipeline()
    obj.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx===============x")
except Exception as e:
    raise e    