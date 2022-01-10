import os
import json
import random


def load_rock(rock_id):
    file = os.path.join(os.path.dirname(__file__), "dna/rock" + str(rock_id) + ".json")
    with open(file, 'r') as f:
        dna = json.load(f)
    return dna


def save_rock(dna, rock_id):
    file = os.path.join(os.path.dirname(__file__), "dna/rock" + str(rock_id) + ".json")
    with open(file, 'w') as f:
        json.dump(dna, f)


def int(dad, mom, min_value, max_value):
    r = random.random()

    # offspring
    if r < 0.2:
        child = dad
    elif r < 0.4:
        child = mom
    elif r < 0.6:
        child = (dad + mom) // 2
    elif r < 0.8:
        child = max(dad, mom) * 120 // 100
    else:
        child = min(dad, mom) * 80 // 100

    # mutation



    # range check
    child = max(min_value, child)
    child = min(max_value, child)

    return child


def float(dad, mom, min_value, max_value):
    r = random.random()

    # offspring
    if r < 0.2:
        child = dad
    elif r < 0.4:
        child = mom
    elif r < 0.6:
        child = (dad + mom) / 2
    elif r < 0.8:
        child = max(dad, mom) * 120 / 100
    else:
        child = min(dad, mom) * 80 / 100

    # mutation



    # range check
    child = max(min_value, child)
    child = min(max_value, child)

    return child


def palette(dad, mom):
    return [random.choice(x) for x in zip(dad, mom)]
