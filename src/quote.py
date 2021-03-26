import random
import json
import os

file_name = "quotes.json"
quotes = dict()


def add(type_id, quote):
    if type_id not in quotes:
        quotes[type_id] = []
    quotes[type_id].append(quote)
    save()


def remove(type_id, quote_index):
    if type_id not in quotes:
        raise Exception(f'There is no quote of type "{type_id}"!')
    elif len(quotes[type_id]) < quote_index + 1:
        raise Exception(f'No quote of index {quote_index} exists!')

    if len(quotes[type_id]) == 1:
        quotes.pop(type_id)
    else:
        quotes[type_id].pop(quote_index)
    save()


def get(type_id):
    if type_id not in quotes:
        return None
    return random.choice(quotes[type_id])


def get_all(type_id):
    if type_id not in quotes:
        return []
    return quotes[type_id]


def get_types():
    return quotes.keys()


def save():
    with open(file_name, 'w', encoding='utf-8') as f:
        f.write(json.dumps(quotes))


def init():
    global quotes
    if os.path.exists(file_name):
        with open(file_name, 'r', encoding='utf-8') as f:
            quotes = json.loads(f.read())