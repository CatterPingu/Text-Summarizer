import os
from pathlib import Path
import logging #Logging during runtime


logging.basicConfig(level=logging.INFO,format='[%(asctime)s]: %(message)s:')
#Level and message types for logging

project_name= "TextSummarizer"

list_of_files=[
    ".github/workflows/.gitkeep" ,#CI/CD deployment(.yaml) files
    f"src/{project_name}/__init__.py", #Constructor package requirement for local installation
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb"
]

for filepath in list_of_files:
    filepath = Path(filepath) #Convert the path to the path type of the OS we are running
    filedir,filename = os.path.split(filepath) #Split function returning the fiel directory and filename
    if filedir!="": #Check that the directory is not empty
        os.makedirs(filedir,exist_ok=True) #Create the folder if it doesn't exist
        logging.info(f"Creating directory: {filedir} for the file {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
         with open(filepath,"w") as f:
             pass
             logging.info(f"Creating empty file: {filename}")

    else:
            logging.info(f"File already exists: {filename}")