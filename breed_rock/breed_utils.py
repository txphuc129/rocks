import os
import json
import random
from common.constants import DENSITY, ENERGY, FAMILY, ID, METABALL, PALETTE, PROPERTIES, RADIUS, RADIUS0, RADIUS1, VORONOI
from common.exceptions import FAMILIES_NOT_EQUAL, INVALID_FAMILY, MISSING_VALUE
from common.rock import Metaball, Voronoi
from common.utils import get_family


def save_rock(dna, dna_folder):
    """Save rock json to a folder

    Args:
        dna (Voronoi | Metaball): an object of either Voronoi or Metaball
        dna_folder (str): destination folder
    """
    goal_path = os.path.join(os.getcwd(), ('..' + dna_folder))
    dna_folder = os.path.abspath(goal_path)
    if not os.path.exists(dna_folder):
        os.makedirs(dna_folder, exist_ok=True)
    file_path = os.path.join(
        dna_folder,
        dna.id + '.json')
    with open(file_path, 'w') as f:
        rock = {}
        rock[ID] = dna.id
        rock[PROPERTIES] = dna.properties
        json.dump(rock, f)


def rand_int(parent1, parent2, min_value, max_value):
    r = random.random()

    # offspring
    if r < 0.2:
        child = parent1
    elif r < 0.4:
        child = parent2
    elif r < 0.6:
        child = (parent1 + parent2) // 2
    elif r < 0.8:
        child = max(parent1, parent2) * 120 // 100
    else:
        child = min(parent1, parent2) * 80 // 100

    # mutation

    # range check
    child = max(min_value, child)
    child = min(max_value, child)

    return child


def rand_float(parent1, parent2, min_value, max_value):
    r = random.random()

    # offspring
    if r < 0.2:
        child = parent1
    elif r < 0.4:
        child = parent2
    elif r < 0.6:
        child = (parent1 + parent2) / 2
    elif r < 0.8:
        child = max(parent1, parent2) * 120 / 100
    else:
        child = min(parent1, parent2) * 80 / 100

    # mutation

    # range check
    child = max(min_value, child)
    child = min(max_value, child)

    return child


def rand_palette(parent1, parent2):
    return [random.choice(x) for x in zip(parent1, parent2)]


def breed_metaball(parent1_dna, parent2_dna, child_id, family):
    """Use parents' dna to randomize child's dna

    Args:
        parent1_dna (dict): dna of the first parent
        parent2_dna (dict): dna of the second parent
        child_id (str): child id
        family (str): the mutual family property

    Returns:
        Metaball: an child entity of metaball
    """
    # randomize the properties
    props = {}
    props[FAMILY] = family
    props[DENSITY] = rand_int(
        parent1_dna[DENSITY], parent2_dna[DENSITY], 0, 100000)
    props[RADIUS0] = rand_float(
        parent1_dna[RADIUS0], parent2_dna[RADIUS0], 0, 4)
    props[RADIUS1] = rand_float(
        parent1_dna[RADIUS1], parent2_dna[RADIUS1], 0, 4)
    props[ENERGY] = rand_int(
        parent1_dna[ENERGY], parent2_dna[ENERGY], 0, 100)

    child = Metaball()
    child.id = child_id
    child.properties = props
    return child


def breed_voronoi(parent1_dna, parent2_dna, child_id, family):
    """Use parents' dna to randomize child's dna

    Args:
        parent1_dna (dict): dna of the first parent
        parent2_dna (dict): dna of the second parent
        child_id (str): child id
        family (str): the mutual family property

    Returns:
        Voronoi: an child entity of voronoi
    """
    # randomize the properties
    props = {}
    props[FAMILY] = family
    props[DENSITY] = rand_int(
        parent1_dna[DENSITY], parent2_dna[DENSITY], 0, 100000)
    props[RADIUS] = rand_int(
        parent1_dna[RADIUS], parent2_dna[RADIUS], 0, 4)
    props[PALETTE] = rand_palette(
        parent1_dna[PALETTE], parent2_dna[PALETTE])

    child = Voronoi()
    child.id = child_id
    child.properties = props
    return child


def parse_breed_data(data):
    """Reformat the input data

    Args:
        data (dict): input data

    Raises:
        ValueError: Missing childId
        ValueError: Missing parent1
        ValueError: Missing parent2
    """
    if 'childId' not in data:
        raise ValueError(MISSING_VALUE + ': childId')
    data['child_id'] = data['childId']
    del data['childId']

    if 'parent1' not in data:
        raise ValueError(MISSING_VALUE + ': parent1')

    if 'parent2' not in data:
        raise ValueError(MISSING_VALUE + ':  parent2')


def create_parents(parent1, parent2):
    """Create entities of parents

    Args:
        parent1 (dict): parent1 dna
        parent2 (dict): parent2 dna

    Raises:
        ValueError: families of two parents are unequal
        ValueError: invalid family

    Returns:
        Voronoi | Metaball: an entity of parent1
        Voronoi | Metaball: an entity of parent2
        str: a str of family
    """
    family1 = get_family(parent1)
    family2 = get_family(parent2)
    family = family1 if family1 == family2 else None

    # validation
    if family is None:
        raise ValueError(FAMILIES_NOT_EQUAL)

    if family != VORONOI and family != METABALL:
        raise ValueError(INVALID_FAMILY)

    # init entities
    if family == VORONOI:
        parent_entity1 = Voronoi()
        parent_entity2 = Voronoi()
    else:
        parent_entity1 = Metaball()
        parent_entity2 = Metaball()

    # setter
    parent_entity1.id = parent1[ID]
    parent_entity1.properties = parent1[PROPERTIES]

    parent_entity2.id = parent2[ID]
    parent_entity2.properties = parent2[PROPERTIES]

    return parent_entity1, parent_entity2, family
