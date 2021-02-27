import os
import random
import discord
import glob

emotion_folder = "emotions"
emotions = dict()  # Links to emotions via paths
available_emotions = ["serenity", "joy", "ecstasy",
                    "acceptance", "trust", "admiration",
                    "apprehension", "fear", "terror",
                    "distraction", "surprise", "amazement",
                    "pensiveness", "sadness", "grief",
                    "boredom", "disgust", "loathing",
                    "annoyance", "anger", "rage",
                    "interest", "anticipation", "vigilance"]


async def add(emotion, file_name, file_bytes):
    if emotion in emotions:
        file_path = "{}/{}/{}".format(emotion_folder, emotion, file_name)
        with open(file_path, "wb") as f:
            f.write(file_bytes)
        emotions[emotion].append(file_path)
        return True
    return False


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
    for emotion in available_emotions:
        emotion_path = "{}/{}".format(emotion_folder, emotion)
        make_folder(emotion_path)

        emotions[emotion] = glob.glob(emotion_path + "/**")
        print(emotions[emotion])

