import seaborn as sns
import matplotlib.pyplot as plt
from unidecode import unidecode
import os
import pandas as pd

def load_data(apps: dict, dir: str):
    apps_dfs = []
    framework_names = []
    apps_durations_dfs = []
    for key in apps:
        name = apps[key]['name']
        path = os.path.join(dir, f'{name}.csv')
        df = pd.read_csv(path)
        
        df_1 = df.loc[(df['metric_name'] == 'http_req_duration')][:]
        df_1 = df_1.filter(['timestamp', 'metric_value'])
        apps_durations_df = df_1['metric_value']

        apps_dfs.append(df)
        framework_names.append(name)
        apps_durations_dfs.append(apps_durations_df)

    return apps_dfs, framework_names, apps_durations_dfs

def draw_timeline(framework_names: list[str], apps_dfs: list[str], title: str):
    for idx in range(len(framework_names)):
        df = apps_dfs[idx]
        framework_name = framework_names[idx]
        df_1 = df.loc[(df['metric_name'] == 'http_req_duration')][:]
        df_1 = df_1.reset_index(drop=True)
        duration = df_1['metric_value']
        sns.lineplot(
            data=duration, 
            label=f'{framework_name}'
            ).set(
                title=title, 
                xlabel="numer zapytania", 
                ylabel="czas [ms]"
                )
        plt.savefig(f'{unidecode(title.replace(" ", "_"))}.png')

def draw_avg_duration(framework_names: list[str], mean_durations: list[float], title: str):
    plt.figure(figsize = (10, 5))
    
    # creating the bar plot
    plt.bar(framework_names, mean_durations, color ='maroon', 
            width = 0.4)

    def addlabels(x,y):
        for i in range(len(x)):
            plt.text(i, y[i]//2, round(y[i], 2), ha = 'center', c="white")

    addlabels(framework_names, mean_durations)
    
    plt.ylabel("czas [ms]")
    plt.title(f'{title}')
    plt.savefig(f'{unidecode(title.replace(" ", "_"))}.png')
