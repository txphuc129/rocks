import os
import json
import random


def save_rock(dna, rock_id):
    file = os.path.join(os.path.dirname(__file__),
                        "../dna/rock" + str(rock_id) + ".json")
    with open(file, 'w') as f:
        json.dump(dna, f)


def rand_int(parent_1, parent_2, min_value, max_value):
    r = random.random()

    # offspring
    if r < 0.2:
        child = parent_1
    elif r < 0.4:
        child = parent_2
    elif r < 0.6:
        child = (parent_1 + parent_2) // 2
    elif r < 0.8:
        child = max(parent_1, parent_2) * 120 // 100
    else:
        child = min(parent_1, parent_2) * 80 // 100

    # mutation

    # range check
    child = max(min_value, child)
    child = min(max_value, child)

    return child


def rand_float(parent_1, parent_2, min_value, max_value):
    r = random.random()

    # offspring
    if r < 0.2:
        child = parent_1
    elif r < 0.4:
        child = parent_2
    elif r < 0.6:
        child = (parent_1 + parent_2) / 2
    elif r < 0.8:
        child = max(parent_1, parent_2) * 120 / 100
    else:
        child = min(parent_1, parent_2) * 80 / 100

    # mutation

    # range check
    child = max(min_value, child)
    child = min(max_value, child)

    return child


def rand_palette(parent_1, parent_2):
    return [random.choice(x) for x in zip(parent_1, parent_2)]


def breed_metaball(parent_1, parent_2, id):
    child = {}
    child['id'] = id
    child['family'] = parent_1['family']
    child['density'] = rand_int(
        parent_1['density'], parent_2['density'], 0, 100000)
    child['radius_0'] = rand_float(
        parent_1['radius_0'], parent_2['radius_0'], 0, 4)
    child['radius_1'] = rand_float(
        parent_1['radius_1'], parent_2['radius_1'], 0, 4)
    child['energy'] = rand_int(parent_1['energy'], parent_2['energy'], 0, 100)
    return child


def breed_voronoi(parent_1, parent_2, id):
    child = {}
    child['id'] = id
    child['family'] = parent_1['family']
    child['density'] = rand_int(
        parent_1['density'], parent_2['density'], 0, 100000)
    child['radius'] = rand_int(
        parent_1['radius'], parent_2['radius'], 0, 4)
    child['palette'] = rand_palette(parent_1['palette'], parent_2['palette'])
    return child
