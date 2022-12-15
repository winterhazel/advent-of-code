import requests

SESSION = 'FILL THIS'


def get_input(day=1, year=2022):
    url = f'https://adventofcode.com/{year}/day/{day}/input'
    response = requests.get(url, cookies={'session': SESSION})
    return response.text
