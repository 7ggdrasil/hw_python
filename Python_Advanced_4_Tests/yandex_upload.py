import requests

URL = 'https://cloud-api.yandex.net/v1/disk/resources'
TOKEN = 'токен'
headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Authorization': f'OAuth {TOKEN}'}


def create_folder_Ya_API(path: str):
    new_folder = requests.put(f'{URL}?path={path}', headers=headers)
    new_folder.raise_for_status()
    if new_folder.status_code == 201:
        print(f'Папка {path} создана')
    return new_folder.status_code


if __name__ == '__main__':
    create_folder_Ya_API('unit-test')