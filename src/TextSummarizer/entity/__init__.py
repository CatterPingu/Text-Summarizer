#Entity(ReturnType of functions)

from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig: #This is a dataclass not a python class
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path