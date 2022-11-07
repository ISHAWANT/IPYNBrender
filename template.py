import os
from pathlib import Path
import logging


logging.basicConfig(level=logging.INFO,format="[%(asctime)s: %(levelnames)s]: %(message)s")

while True:
    projct_name = input('Enter the project Name: ')
    if projct_name !='':
        break

logging.info(f"Creating project by name:{projct_name}")

# lists of files:

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{projct_name}/__init__.py",
    f"tests/__init__.py",
    f"test/unit/__init__.py",
    f"tests/integration/__init__.py",
    "init_setup_.sh",
    "requirements_dev.txt",
    "setup.py",
    "pyproject.toml",
    "setup.cfg",
    "tox.ini"
    ]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir,filename = os.path.split(filepath)
    if filedir !="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating a directory at: {filedir} for file:{filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,'w') as f:
            pass
            logging.info(f"Creating a new file:{filename} at path: {filepath} at path: {filepath}")

    else:
        logging.info(f"file is already present at: {filepath}")
