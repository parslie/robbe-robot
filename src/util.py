import os


def make_folder(path):
    try:
        os.mkdir(path)
    except:
        pass