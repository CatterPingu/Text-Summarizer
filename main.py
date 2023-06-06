from TextSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from TextSummarizer.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from TextSummarizer.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from TextSummarizer.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline
from TextSummarizer.pipeline.stage_05_model_evaluation import ModelEvaluationTrainingPipeline
from TextSummarizer.logging import logger

STAGE_NAME="Data Ingestion Stage"

try:
    logger.info(f">>>>>stage{STAGE_NAME} started<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>stage{STAGE_NAME} completed<<<<<\n\nx================================x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME="Data Validation Stage"

try:
    logger.info(f">>>>>stage{STAGE_NAME} started<<<<<")
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f">>>>>stage{STAGE_NAME} completed<<<<<\n\nx================================x")

except Exception as e:
    logger.exception(e)
    raise e   


STAGE_NAME="Data Transformation Stage"

try:
    logger.info(f">>>>>stage{STAGE_NAME} started<<<<<")
    data_transformation = DataTransformationTrainingPipeline()
    data_transformation.main()
    logger.info(f">>>>>stage{STAGE_NAME} completed<<<<<\n\nx================================x")

except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME="Model Training Stage"

try:
    logger.info(f">>>>>stage{STAGE_NAME} started<<<<<")
    model_training = ModelTrainerTrainingPipeline()
    model_training.main()
    logger.info(f">>>>>stage{STAGE_NAME} completed<<<<<\n\nx================================x")

except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME="Model Evaluation Stage"

try:
    logger.info(f">>>>>stage{STAGE_NAME} started<<<<<")
    model_evaluation = ModelEvaluationTrainingPipeline()
    model_evaluation.main()
    logger.info(f">>>>>stage{STAGE_NAME} completed<<<<<\n\nx================================x")

except Exception as e:
    logger.exception(e)
    raise e