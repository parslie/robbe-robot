import os
import json

def save(data: dict, path):
    dir = os.path.dirname(path)
    os.makedirs(dir, exist_ok=True)

    with open(path, 'w') as file:
        json.dump(data, file)


def load(path) -> dict:
    dir = os.path.dirname(path)
    os.makedirs(dir, exist_ok=True)

    data = dict()
    if os.path.exists(path):
        with open(path, 'r') as file:
            data = json.load(file)
    else:
        with open(path, 'w') as file:
            file.write('{}')
    return data