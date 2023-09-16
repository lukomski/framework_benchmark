import json
import os

SETUP_PATH = 'setup.json'
f = open(SETUP_PATH)
data = json.load(f)


def get_last_result_dir():
    dirs = [x[0] for x in os.walk(f'{data["test_result_base_dir"]}')]
    dirs.sort()
    return dirs[-1]
