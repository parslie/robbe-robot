import random

quotes = ["STABEN har kilten under ingenting",
        "Jesus kunde gå på vatten, men GENERALEN kan simma i vakuum",
        "STABEN kan surfa utan nätuppkoppling",
        "STABEN vet sista decimalen i π",
        "STABEN släppte ut hundarna",
        "STABEN byggde Rom på en dag",
        "STABEN har fräsigaste kärran",
        "STABEN ger allt",
        "STABEN är den fjärde dimensionen",
        "STABEN får lök att gråta",
        "STABEN kan stegra med en enhjuling",
        "STABEN upptäckte Amerika",
        "Det fanns en gång en gata döpt efter STABEN, men den döptes om eftersom ingen korsar STABEN",
        "STABEN lärde Jesus gå på vatten",
        "STABEN kan lyfta allas mammor",
        "STABEN förstod tidslinjen i The Witcher",
        "STABEN 👌",
        "Det går inte att hitta STABEN i en höstack",
        "Bakom STABENS skägg finns mer skägg",
        "STABEN har besökt alla tidepoker",
        "STABEN vet Victorias hemlighet",
        "STABEN räknade till oändligheten - två gånger",
        "Före STABEN fanns inget",
        "STABEN har örnar i nacken",
        "STABEN kan häfva en tsunami",
        "STABEN stoppar Fronda när han rullar fram",
        "STABEN kan vinna en match i fyra i rad på tre drag",
        "STABEN kan bänka, asså såå mycket",
        "STABEN snor leksaken ur ditt Happy Meal",
        "STABEN har nackar i ögonen",
        "Borta bra men STABEN bäst",
        "STABEN kan prata i blindskrift",
        "STABEN är det bästa försvaret",
        "En solförmörkelse är när solen försöker gömma sig från STABEN",
        "STABEN behöver aldrig sprätta",
        "Näsan går dit STABEN pekar",
        "STABEN har slut på toapapper 😢",
        "STABEN är det sjätte sinnet",
        "aard, igni, yrden, quen, axii, STABEN",
        "STABEN kastar glas i stenhus",
        "STABEN kan dividera med noll",
        "STABEN rullar ut och rullar på"]
last_quote_index = 0

def get_quote():
    global last_quote_index
    quote_index = last_quote_index

    while quote_index == last_quote_index:
        quote_index = random.randrange(len(quotes))

    last_quote_index = quote_index
    return quotes[quote_index]
