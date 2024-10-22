import os
import shutil
from datetime import datetime
import math
import utils
import k6Utils
import pandas as pd

def test_vus_limit(
        result_base_dir: str,
        test_result_dir_prefix: str,
        script_path: str,
        setup_path: str,
        app: dict,
        inital_vus: int,
        out_file_name: str,
        end: int | None = None
        ):
    # prepare directory structure
    if not os.path.exists(result_base_dir):
        os.makedirs(result_base_dir)

    dt_string = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    print("date and time =", dt_string)

    dir_name = f'./{result_base_dir}/{test_result_dir_prefix}{dt_string}'
    print(dir_name)
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
        
    # copy script
    shutil.copy(script_path, dir_name)
    shutil.copy(setup_path, dir_name)

    out_file = open(out_file_name, "a")
    out_file.write(f'\n-------------------------')
    out_file.close()

    vus = inital_vus
    beg = 1
    end = end
    threshold = 0
    while (True):
        # run test
        k6Utils.run_k6(
            app=app,
            script_path=script_path,
            vus=vus,
            dir_name=dir_name
            )

        # load dataframe
        dir = utils.get_last_result_dir(test_result_base_dir=result_base_dir)
        path = f'./{dir}/{app["name"]}.csv'
        df = pd.read_csv(path)

        # calculate metric
        incorrect_part = utils.get_incorrect_part(df)
            
        print(f'Incorrect part for vus = {vus}: {incorrect_part}\n')

        out_file = open(out_file_name, "a")
        out_file.write(f'\nvus = {vus}, beg = {beg}, end = {end}, incorrect_part = {incorrect_part}')
        out_file.close()

        if (math.isnan(incorrect_part) or incorrect_part > threshold):
            end = vus
            vus = math.floor((end + beg) / 2)
        else:
            beg = vus
            vus = vus * 2 if end == None else math.floor((end + beg) / 2)
        
        if end and end - beg < 2:
            break