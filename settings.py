import logging
import os


class Config(object):
    """Base configuration."""

    ENVIRONMENT = os.getenv("Environment", "dev")
    _DATASCHEMA = os.getenv("DataSchemaTbl", "DataSchemas")
    DATASCHEMA_TABLE = "test-{}-{}".format(_DATASCHEMA, ENVIRONMENT)

    _DATASET = os.getenv("DatasetTbl", "Datasets")
    DATASET_TABLE = "test-{}-{}".format(_DATASET, ENVIRONMENT)


    AWS_DEFAULT_REGION = os.getenv("AWS_DEFAULT_REGION", "us-east-1")
    LOGGING_LEVEL = os.getenv("LOGGING_LEVEL", logging.getLevelName(logging.DEBUG))

    DEBUG = os.getenv("DEBUG", False) == "true"

    DATASET_MAX_LIMIT = 2
    MAX_LIMIT = 100
