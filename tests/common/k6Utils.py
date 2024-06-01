import os

def run_k6(app: dict, script_path: str, vus: int, dir_name: str):
  bashCommand = f'k6 run {script_path} \
    --env vus={vus} \
    --env url={app["url"]} \
    --out json={dir_name}/{app["name"]}.json \
    --out csv={dir_name}/{app["name"]}.csv'
  os.system(bashCommand)