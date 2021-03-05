import os
import random
import discord
from glob import glob
from util import make_folder

folder_name = "memes"
memes = dict()  # Links to memes via paths


def get_types():
    return [t for t in memes.keys()]


def get(meme_type):
    images = memes.get(meme_type)
    if images != None and len(images) != 0:
        image_file = None
        with open(random.choice(images), "rb") as f:
            image_file = discord.File(f)
        return image_file  # TODO: check if needs to close
    return None


def add(meme_type, file_name, file_bytes):
    if meme_type not in memes:
        make_folder(f"{folder_name}/{meme_type}")
        memes[meme_type] = []

    file_path = f"{folder_name}/{meme_type}/{file_name}"
    if file_bytes not in memes[meme_type]:
        with open(file_path, "wb") as f:
            f.write(file_bytes)
        memes[meme_type].append(file_path)


def init():
    make_folder(folder_name)

    meme_types = glob(f"{folder_name}/*/")
    for i in range(len(meme_types)):
        meme_types[i] = os.path.dirname(meme_types[i])
        meme_types[i] = os.path.basename(meme_types[i])

    for meme_type in meme_types:
        memes[meme_type] = glob(f"{folder_name}/{meme_type}/**")