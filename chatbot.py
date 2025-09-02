import random
# print("hallo")
begroetingen = ["hallo","goedendag","hoi, hoe gaat het","welkom"]


def pickanswer(list):
    print(random.choice(list))

pickanswer(begroetingen)