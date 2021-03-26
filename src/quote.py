import json
import os

custom_fn = "custom_quotes.json"
default_fn = "default_quotes.json"
custom_quotes = dict()
default_quotes = dict()


def save():
    with open(custom_fn, 'w') as f:
        f.write(json.dumps(custom_quotes))


def init():
    global default_quotes
    global custom_quotes

    if os.path.exists(default_fn):
        with open(default_fn, 'r') as f:
            default_quotes = json.loads(f.read())
    if os.path.exists(custom_fn):
        with open(custom_fn, 'r') as f:
            custom_quotes = json.loads(f.read())