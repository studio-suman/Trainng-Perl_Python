import os
import json
from fastapi import HTTPException

# Get the absolute path of the directory where the current script is located
script_dir = os.path.dirname(os.path.abspath(__file__))
# Construct the path to config.json relative to the script's directory
config_file_path = os.path.join(script_dir, 'config.json')
CONFIG_DATA = {}
# print(config_file_path)
try:
    with open(config_file_path, 'r') as f:
        CONFIG_DATA = json.load(f)
except FileNotFoundError:
    raise HTTPException(
        detail=f"Error: The file {config_file_path} was not found.",
        status_code=500
    )
except json.JSONDecodeError:
    print(f"Error: Could not decode JSON from the file {config_file_path}.")
    raise HTTPException(
        detail=f"Error: Could not decode JSON from the file {config_file_path}.",
        status_code=500
    )