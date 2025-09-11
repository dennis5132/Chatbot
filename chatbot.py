import random
from datetime import datetime
import json

# alle commands
begroetingen = ["hallo","goedendag","hoi, hoe gaat het","welkom","goed je te zien"]
grappen = ["Een man komt bij de dokter...", "Fred gaat naar de dokter...", "Hoe noem je een ijsbeer met oorwarmers? Laat maar..."]
rps = ["steen","schaar","papier"]
rpsstart = ["steen, papier, schaar:"]
commandoError = ["geen flauw idee wat dat is","kun je ook echte commando's geven?"]
irritatie = ["tjonge, jij stelt veel vragen", "alweer een vraag?"]
afsluit = ["doei","tot ziens","eindelijk rust"]

# voor het afsluiten vd bot
running = True

# voor de irritatie functie
askedQ = 0
herinneringen = []

# kiest ie een willekeurig antwoord
def pickanswer(lst):
    print(random.choice(lst))

try:
    with open("geheugen.JSON", "r") as f:
        herinnering = json.load(f)
except (FileNotFoundError, json.JSONDecodeError):
    herinnering = []


pickanswer(begroetingen)

# doet ie altijd terwijl hij runt zodat je alle mogelijkheden ziet
while running:
    print("\nwat wil je doen:")
    print("- vertel een grap")
    print("- hoe laat is het")
    print("- speel een spel")
    print("- herinner me aan iets")
    print("- eindig programma")
    
    command = input("> ")
    # plus 1 voor elk commando om irritatie op te doen
    askedQ += 1

    # irritatie check
    if askedQ > 3:
        pickanswer(irritatie)

    # Commando's
    if command == "vertel een grap":
        pickanswer(grappen)

    elif command == "hoe laat is het":
        now = datetime.now()
        print("het is nu", now.hour,"uur en", now.minute,"minuten")

    elif command == "speel een spel":
        pickanswer(rpsstart)
        rps1 = input("> ")
        rps2 = random.choice(rps)
        print("ik kies:", rps2)
        if rps1 == rps2:
            print("gelijk!")
        elif (rps1 == "steen" and rps2 == "schaar") or \
             (rps1 == "papier" and rps2 == "steen") or \
             (rps1 == "schaar" and rps2 == "papier"):
            print("jij wint!")
        else:
            print("ik win!")

    elif command == "herinner me aan iets":
        ding = input("waaraan moet ik je herinneren?: ")
        herinnering.append(ding)
        print("oké, ik onthoud:", ding)

    elif command == "toon herinneringen":
        if herinnering:
            print("Dit zijn je herinneringen:")
            for h in herinnering:
                print("-", h)
        else:
            print("Je hebt nog geen herinneringen.")

    elif command == "eindig programma":
        if herinnering:  # eerst herinneringen tonen
            print("Ojah, vergeet niet:")
            for h in herinnering:
                print("-", h)
                # dan sluit het progamma af
        pickanswer(afsluit)
        running = False

    else:
        pickanswer(commandoError)

    # Herinneringen check (blijven staan)
    if herinnering and command != "herinner me aan iets" and command != "toon herinneringen" and command != "eindig programma":
        print("Ik onthoud nog steeds:")
        for ding in herinnering:
            print("-", ding)

