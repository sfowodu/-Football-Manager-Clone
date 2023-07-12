import random
import time
import json


with open('teams.txt') as f:
    data = json.load(f)

def createtable(data):

    dictionary = {}

    for team in data:
        dictionary[data[team]['name']] = data[team]["score"]

    new_dictionary = sorted(dictionary, key=dictionary.get, reverse=True)

    position = 1
    for team in new_dictionary:
        p = str(position) + '. ' + team
        print(p)
        position += 1
