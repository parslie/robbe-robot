import random
import datetime

donken_menus = ["Big Mac & Co", "Trippel Cheese & Co", "McFeast & Co", "El Maco & Co",
        "Chicken McNuggets & Co", "Chicken McFeast & Co", "Chicken El Maco & Co",
        "McVegan & Co", "Veggie El Maco & Co", "Tasty & Co", "QP Cheese & Co",
        "Chicken Tasty & Co"]

donken_desserts = ["McFlurry Salted Caramel", "McFlurry Oreo", "McFlurry Daim",
        "Unicorn Freakshake", "Frappé Mocha", "Frappé Caramel",
        "Apple Pie", "Sundae Deluxe Daim", "Ice Cream with Strawberry Topping",
        "Ice Cream with Chocolate Topping", "Ice Cream with Caramel Topping"]

def donken(seed):
        curr_date = datetime.datetime.now()
        oldstate = random.getstate()
        random.seed(curr_date.strftime("%H") + seed + curr_date.strftime("%j%Y"))

        # TODO: add more options
        menu = random.choice(donken_menus)
        dessert = random.choice(donken_desserts)

        random.setstate(oldstate)

        return "You want a {} with a {}!".format(menu, dessert)


def dice(sides=6):
        return random.randint(1, sides)


tts_dict = {"att": "aht",
        "balle": "ball eh",
        "bissenisse": "bissuh nissuh",
        "coolt": "cooled",
        "dig": "day",
        "god": "gooed",
        "där": "dare",
        "dära": "daira",
        "er": "eer",
        "fika": "feeka",
        "finns": "fins",
        "få": "foe",
        "fått": "fought",
        "ganska": "gaanska",
        "gitarr": "jituhr",
        "gå": "gall",
        "göra": "yöra",
        "göras": "yöras",
        "hade": "haddeh",
        "hjälp": "yelp",
        "hjärtan": "yertaenn",
        "hon": "holn",
        "här": "hair",
        "hära": "haira",
        "i": "e",
        "idag": "e daag",
        "igår": "e gore",
        "inte": "inteh",
        "isse": "issuh",
        "jag": "yahg",
        "ju": "you",
        "kalle": "kall leh",
        "kunskap": "kuunskaaap",
        "lite": "leet eh",
        "liten": "leeten",
        "lolle": "loo leh",
        "lärdom": "lairdom",
        "lät": "let",
        "man": "mahn",
        "meddela": "meadeela",
        "mig": "may",
        "mot": "mote",
        "måste": "mohsteh",
        "när": "nair",
        "också": "och so",
        "okej": "okay",
        "produktiva": "product eva",
        "produktivt": "product eeft",
        "pungsäck": "poong seck",
        "på": "poe",
        "robbe": "rob eh",
        "sig": "say",
        "spela": "speela",
        "spöka": "spuh kah",
        "spökar": "spuh kar",
        "staben": "staaaben",
        "sär": "sair",
        "trafik": "trahfeek",
        "trafiken": "trahfeek en",
        "tro": "troh",
        "under": "oonder",
        "uppgradering": "ooopgrad earring",
        "vad": "vahd",
        "valle": "valleh",
        "vare": "var eh",
        "varit": "var it",
        "vetenskap": "vet en skaap",
        "vi": "ve",
        "våra": "vora",
        "älskar": "elskair",
        "är": "air",
        "över": "uhver"}
punctuation = [".", ",", "!", "?", ":"]

def tts(text):
        translated = ""

        text = text.lower()
        for p in punctuation:
                text = text.replace(p, f" {p} ")
        text = text.split()

        for split in text:
                if split in punctuation:
                        translated += split
                elif split in tts_dict:
                        translated += " " + tts_dict[split]
                else:
                        translated += " " + split

        return translated