import os
from mlProject.constants import * 
from mlProject.utils.common import read_yaml, create_directories
from mlProject.entity.config_entity import (DataIngestionConfig, DataValidationConfig)

class ConfigurationManager:
    def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAMS_FILE_PATH,
        schema_filepath = SCHEMA_FILE_PATH):

        print(f"Config file path: {config_filepath}")
        print(f"Params file path: {params_filepath}")
        print(f"Schema file path: {schema_filepath}")

        # Check if config files exist and handle missing files gracefully
        if not os.path.exists(config_filepath):
            raise FileNotFoundError(f"Config file not found at path: {config_filepath}")
        if not os.path.exists(params_filepath):
            raise FileNotFoundError(f"Params file not found at path: {params_filepath}")
        if not os.path.exists(schema_filepath):
            raise FileNotFoundError(f"Schema file not found at path: {schema_filepath}")

        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        self.schema = read_yaml(schema_filepath)

        create_directories([self.config.artifacts_root])


    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir 
        )

        return data_ingestion_config
    

    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation
        schema = self.schema.COLUMNS

        create_directories([config.root_dir])

        data_validation_config = DataValidationConfig(
            root_dir=config.root_dir,
            STATUS_FILE=config.STATUS_FILE,
            unzip_data_dir = config.unzip_data_dir,
            all_schema=schema,
        )

        return data_validation_config