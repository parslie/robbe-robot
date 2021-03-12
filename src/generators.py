import random
import datetime


staben_quotes = ["Borta bra men STABEN bäst",
        "Det fanns en gång en gata döpt efter STABEN, men den döptes om eftersom ingen korsar STABEN",
        "Det går inte att hitta STABEN i en höstack",
        "Det var STABEN som kasta",
        "En solförmörkelse är när solen försöker gömma sig från STABEN",
        "Före STABEN fanns inget",
        "Jesus kunde gå på vatten, men Generalen kan simma i vakuum",
        "Näsan går dit STABEN pekar",
        "Bakom STABENS skägg finns mer skägg",
        "STABEN 👌",
        "STABEN byggde Rom på en dag",
        "STABEN får lök att gråta",
        "STABEN har besökt alla tidsepoker",
        "STABEN har fräsigaste kärran",
        "STABEN har kilten under ingenting",
        "STABEN har nackar i ögonen",
        "STABEN kan bänka, asså såå mycket",
        "STABEN kan dividera med noll",
        "STABEN kan häfva en tsunami",
        "STABEN kan komma ihåg framtiden",
        "STABEN kan lyfta allas mammor",
        "STABEN kan prata i blindskrift",
        "STABEN kan segla förutan vind",
        "STABEN kan stegra med en enhjuling",
        "STABEN kan surfa utan nätuppkoppling",
        "STABEN kan vinna en match i fyra i rad på tre drag",
        "STABEN kastar glas i stenhus",
        "STABEN lärde Jesus gå på vatten",
        "STABEN rullar ut och rullar på",
        "STABEN räknade till oändligheten - två gånger",
        "STABEN släppte ut hundarna",
        "STABEN smälter in överallt",
        #Vem fan är Fronda?# "STABEN stoppar Fronda när han rullar fram",
        "STABEN uppfann skivat bröd",
        "STABEN upptäckte Amerika",
        "STABEN vet sista decimalen i π",
        "STABEN vet Victorias hemlighet",
        "STABEN är den fjärde dimensionen",
        "STABEN är det bästa försvaret",
        "STABEN är det sjätte sinnet",
        "STABEN behöver aldrig sprätta",
        "STABEN snor leksaken ur ditt Happy Meal",
        #WITCHER# "aard, igni, yrden, quen, axii, STABEN",
        "STABEN förstod tidslinjen i The Witcher",
        "STABEN ger allt",
        "STABEN har örnar i nacken",        
        "STABEN har slut på toapapper 😢"]

def staben():
        return random.choice(staben_quotes)


erik_quotes = ["PÖHÖHÖHÖ",
        "Tjena, har du tid att snacka eller?",
        "Vad är en pekare?",
        "Jag testar att ringa Isak.",
        "Jag testar att ringa Viktor.", 
        "STABEN är ju rätt cringe, faktiskt.",
        "Jag var bara ironisk, pöhöhö.",
        "Sorry jag blir sen, behövde panikstryka min skjorta.",
        "Finn 5 fel!",
        "Jag hade ont i vaden innan, så nu kan jag inte labba.",
        "Min pappa är polis.",
        "Min mamma är biljettkontrollant.",
        "Det känns fel att gå över vägen när det inte finns ett övergångsställe.",
        "Jag bad John att flytta men sen hittade han en lägenhet i Ullevi åt mig.",
        "Hur kan du göra så här mot mig, vi har ju ändå varit vänner i typ ett och ett halvt å- Det var inget jag hittade en ny partner.",
        "Ska vi labba kl 7:00 imorgon? Nej? Men nu blir det så här!",
        "Låt mig bara höja mitt bord. *EEEEEEEEEEEEEEEEEEEEEEE*",
        "Kan du skjutsa mig till akuten? Jag känner mig lite förkyld.",
        "Jag tycker faktiskt om 68ans pizzor, pöhöhöhö!"]

def erik():
        return random.choice(erik_quotes)


donken_menus = ["Big Mac & Co", "Trippel Cheese & Co", "McFeast & Co", "El Maco & Co",
        "Chicken McNuggets & Co", "Chicken McFeast & Co", "Chicken El Maco & Co",
        "McVegan & Co", "Veggie El Maco & Co"]

donken_desserts = ["McFlurry Salted Caramel", "McFlurry Oreo", "McFlurry Daim",
        "Unicorn Freakshake", "Frappé Mocha", "Frappé Caramel",
        "Äppelpaj", "Sundae Deluxe Daim"]

def donken(seed):
        curr_date = datetime.datetime.now()
        oldstate = random.getstate()
        random.seed(seed + curr_date.strftime("%j%Y%H"))

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
        "där": "dare",
        "dära": "daira",
        "er": "eer",
        "fika": "feeka",
        "finns": "fins",
        "ganska": "gaanska",
        "gitarr": "jituhr",
        "gå": "gall",
        "göra": "yöra",
        "göras": "yöras",
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
        "valle": "valleh",
        "varit": "var it",
        "vetenskap": "vet en skaap",
        "vi": "ve",
        "våra": "vora",
        "älskar": "elskair",
        "är": "air"}
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