import os
import random
import discord
import glob

emotion_folder = "emotions"
emotions = dict()  # Links to emotions via paths


def available_emotions():
    return [e for e in emotions.keys()]


async def add(emotion, file_name, file_bytes):
    if emotion not in emotions:
        make_folder("{}/{}".format(emotion_folder, emotion))
        emotions[emotion] = []

    file_path = "{}/{}/{}".format(emotion_folder, emotion, file_name)
    with open(file_path, "wb") as f:
        f.write(file_bytes)
    emotions[emotion].append(file_path)


def get(emotion):
    images = emotions.get(emotion)
    if images != None and len(images) != 0:
        image_file = None
        with open(random.choice(images), "rb") as f:
            image_file = discord.File(f)
        return image_file
    return None


def make_folder(path):
    try:
        os.mkdir(path)
    except:
        pass


def init():
    make_folder(emotion_folder)

    available_emotions = glob.glob("{}/*/".format(emotion_folder))
    for i in range(len(available_emotions)):
        available_emotions[i] = os.path.dirname(available_emotions[i])
        available_emotions[i] = os.path.basename(available_emotions[i])

    for emotion in available_emotions:
        emotions[emotion] = glob.glob("{}/{}/**".format(emotion_folder, emotion))