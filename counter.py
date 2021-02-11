import json
import os

file_name = "counters.json"

counters = dict()
if os.path.exists(file_name):
    file = open(file_name, "r")
    counters = json.loads(file.read())
    file.close()


def create(name, title, default = 0):
    counters[name] = dict()
    counters[name]["title"] = title
    counters[name]["value"] = default
    save()


def delete(name):
    counters.pop(name)


def increment(name):
    counter = counters.get(name)
    if counter != None:
        counter["value"] += 1
        save()


def decrement(name):
    counter = counters.get(name)
    if counter != None:
        counter["value"] -= 1
        save()
    

def get_title(name):
    counter = counters.get(name)
    if counter != None:
        return counter["title"]
    

def get_value(name):
    counter = counters.get(name)
    if counter != None:
        return counter["value"]


def to_string():
    text = ""
    
    for id, counter in counters.items():
        text += "**{}** - {}\n".format(id, counter["title"])
    
    return text


def save():
    file = open(file_name, "w")
    file.write(json.dumps(counters))
    file.close()