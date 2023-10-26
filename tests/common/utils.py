import json
import os

def get_last_result_dir(setup_data: dict):
    '''
    Returns last loaded directory.
    '''
    dirs = [x[0] for x in os.walk(f'{setup_data["test_result_base_dir"]}')]
    dirs.sort()
    return dirs[-1]

def get_incorrect_part(df) -> float:
    '''
    Returns incorrect part of requests.

    E.g.
    - Returned value 0.0 means that every requested has finished successfully
    - Returned value 1.0 means that every requests has failed
    '''
    df = df.loc[(df['metric_name'] == 'http_req_failed')]
    correct_status = df.loc[(df['status'] == 200 )]['status']
    incorrect_status = df.loc[(df['status'] != 200)]['status']
    incorrect_part = incorrect_status.count() / (correct_status.count() + incorrect_status.count())
    return incorrect_part


