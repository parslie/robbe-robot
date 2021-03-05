import json
import os

file_name = "counters.json"

counters = dict()


def create(name, title, default = 0):
    if name in counters:
        return False

    counters[name] = dict()
    counters[name]["title"] = title
    counters[name]["value"] = default
    save()
    return True


def delete(name):
    if name not in counters:
        return False

    counters.pop(name)
    save()
    return True


def increment(name):
    counter = counters.get(name)
    if counter == None:
        return False
    
    counter["value"] += 1
    save()
    return True


def decrement(name):
    counter = counters.get(name)
    if counter == None:
        return False

    counter["value"] -= 1
    save()
    return True
    

def get_title(name):
    counter = counters.get(name)
    if counter == None:
        return None
    return counter["title"]
    

def get_value(name):
    counter = counters.get(name)
    if counter == None:
        return None
    return counter["value"]


def to_string():
    text = ""
    
    for id, counter in counters.items():
        text += "**{}** - {}\n".format(id, counter["title"])
    if text == "":
        text = "There are no counters..."

    return text


def save():
    file = open(file_name, "w")
    file.write(json.dumps(counters))
    file.close()


def init():
    if os.path.exists(file_name):
        file = open(file_name, "r")
        counters = json.loads(file.read())
        file.close()