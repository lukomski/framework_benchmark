import json
import os

def get_last_result_dir(setup_data: dict):
    dirs = [x[0] for x in os.walk(f'{setup_data["test_result_base_dir"]}')]
    dirs.sort()
    return dirs[-1]
