import json
import os

def get_last_result_dir(test_result_base_dir: str):
    '''
    Returns last loaded directory.
    '''
    dirs = [x[0] for x in os.walk(test_result_base_dir)]
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

def durationToString(durationInSeconds) -> str:
    seconds = durationInSeconds
    _minute_in_seconds = 60
    _hour_in_seconds = _minute_in_seconds * 60
    _day_in_seconds = _hour_in_seconds * 24

    days = int(seconds / _day_in_seconds)
    seconds -= days * _day_in_seconds

    hours = int(seconds / _hour_in_seconds)
    seconds -= hours * _hour_in_seconds

    minutes = int(seconds / _minute_in_seconds)
    seconds -= minutes * _minute_in_seconds

    s = ''
    if days > 0:
        if len(s) > 0:
            s += ' '
        s += f'{days}d'
    if hours > 0:
        if len(s) > 0:
            s += ' '
        s += f'{hours}h'
    if minutes > 0:
        if len(s) > 0:
            s += ' '
        s += f'{minutes}m'
    if seconds > 0 or len(s) == 0:
        if len(s) > 0:
            s += ' '
        s += f'{seconds}s'
    return s


