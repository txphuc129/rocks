import os
import json
import random

from common.parser_utils import parse_metaball_props, parse_voronoi_props


def save_rock(dna, rock_id, dna_folder):
    goal_path = os.path.join(os.getcwd(), ('..' + dna_folder))
    dna_folder = os.path.abspath(goal_path)
    if not os.path.exists(dna_folder):
        os.makedirs(dna_folder, exist_ok=True)
    file_path = os.path.join(
        dna_folder,
        rock_id + '.json')
    with open(file_path, 'w') as f:
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


def breed_metaball(parent_1, parent_2, child_id):
    # randomize the properties
    properties = {}
    properties['family'] = parent_1['family']
    properties['density'] = rand_int(
        parent_1['density'], parent_2['density'], 0, 100000)
    properties['radius_0'] = rand_float(
        parent_1['radius_0'], parent_2['radius_0'], 0, 4)
    properties['radius_1'] = rand_float(
        parent_1['radius_1'], parent_2['radius_1'], 0, 4)
    properties['energy'] = rand_int(
        parent_1['energy'], parent_2['energy'], 0, 100)

    child = {}
    child['id'] = child_id
    child['properties'] = properties
    return child


def breed_voronoi(parent_1, parent_2, child_id):
    # randomize the properties
    properties = {}
    properties['family'] = parent_1['family']
    properties['density'] = rand_int(
        parent_1['density'], parent_2['density'], 0, 100000)
    properties['radius'] = rand_int(
        parent_1['radius'], parent_2['radius'], 0, 4)
    properties['palette'] = rand_palette(
        parent_1['palette'], parent_2['palette'])

    child = {}
    child['id'] = child_id
    child['properties'] = properties
    return child


def parse_breed_data(data):
    # check for childId
    if 'childId' not in data:
        raise ValueError('Missing childId')
    data['child_id'] = data['childId']
    del data['childId']

    # check for parent1 and replace the data with pythonic syntax
    if 'parent1' not in data:
        raise ValueError('Missing parent1')
    data['parent_1'] = data['parent1']
    del data['parent1']

    # check for data in parent1
    parent_1 = data['parent_1']
    if 'id' not in parent_1:
        raise ValueError('Missing id')
    if 'properties' not in parent_1:
        raise ValueError('Missing properties')
    properties_1 = parent_1['properties']
    if 'family' not in properties_1:
        raise ValueError('Missing family')

    # check for parent2 and replace the data with pythonic syntax
    if 'parent2' not in data:
        raise ValueError('Missing parent2')
    data['parent_2'] = data['parent2']
    del data['parent2']

    # check for data in parent2
    parent_2 = data['parent_2']
    if 'id' not in parent_2:
        raise ValueError('Missing id')
    if 'properties' not in parent_2:
        raise ValueError('Missing properties')
    properties_2 = parent_2['properties']
    if 'family' not in properties_2:
        raise ValueError('Missing family')

    # check if the families are the same
    if properties_1['family'] != properties_2['family']:
        raise ValueError('Mismatched families')

    # parse the properties
    if properties_1['family'] == 'voronoi':
        parse_voronoi_props(properties_1)
        parse_voronoi_props(properties_2)
    elif properties_1['family'] == 'metaball':
        parse_metaball_props(properties_1)
        parse_metaball_props(properties_2)
    else:
        raise ValueError('Invalid family')
