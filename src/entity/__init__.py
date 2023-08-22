from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path
    
    
@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir: Path
    train_path: Path
    test_path: Path
    preprocessor_model_path: Path
    
    
@dataclass(frozen=True)
class ModelTrainerConfig:
    root_dir: Path
    train_path: Path
    test_path: Path
    preprocessor_model_path: Path
    model_path:Path