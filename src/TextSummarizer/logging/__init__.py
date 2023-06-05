import os
import sys
import logging

logging_str="[%(asctime)s]: %(levelname)s:%(module)s:%(message)s"
log_dir="logs"
log_filepath=os.path.join(log_dir, "running_logs.log")
os.makedirs(log_dir,exist_ok=True)


#Format of a custom log

logging.basicConfig(
    level=logging.INFO,
    format=logging_str,

handlers=[
    logging.FileHandler(log_filepath), #Will create a file
    logging.StreamHandler(sys.stdout) #Will show log in terminal
]
)

logger = logging.getLogger("TextSummarizerLogger")