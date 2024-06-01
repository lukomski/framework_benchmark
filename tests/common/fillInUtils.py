# Initialize database
import requests
import datetime
import utils

def fill_framework(
        app: dict, 
        N: int,
    ):
    clear_url = app['clearUrl']
    print(clear_url)
    response = requests.post(clear_url)
    print(response.content)
    print(response.status_code)

    fill_in_url = app['fillInUrl']
    print(fill_in_url)
    print(N)
    patch = app['patch']
    iterations = int(N / patch)
    print(f'iterations: {iterations}')
    for i in range(1, iterations + 1):
        first_time = datetime.datetime.now()
        response = requests.post(fill_in_url, params={'N': patch})
        later_time = datetime.datetime.now()
        difference = later_time - first_time
        print(f'{i}/{iterations}: {response.content}')
        print(f'{i}/{iterations}: {response.status_code}')
        print(f'{i}/{iterations}: duration: {utils.durationToString(difference.seconds)}')
        remaining_iterations = iterations - i
        print(f'{i}/{iterations}: expected end in: {utils.durationToString(difference.seconds * remaining_iterations)}')

    remaining = N % patch
    if remaining > 0:
        print(f'remaining: {remaining}')
        response = requests.post(fill_in_url, params={'N': remaining})
        print(response.content)
        print(response.status_code)