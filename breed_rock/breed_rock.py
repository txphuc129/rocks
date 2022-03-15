import sys
sys.path.append("")  # NOQA
from breed_rock.breed_utils import breed_metaball, breed_voronoi, parse_breed_data, save_rock
from common.parser_utils import parse_argv
from render_rock.render_rock import render


def breed(parent_props_1, parent_props_2, child_id):
    """	Breed a child rock by randomizing the parents' properties

    Args:
            parent_1 (dict): properties of the first parent
            parent_2 (dict): properties of the second parent
            child_id (str): child id

    Raises:
            ValueError: different families
            ValueError: unidentifiable family

    Returns:
            dict: child DNA
    """

    family = parent_props_1['family']
    if family == 'voronoi':
        child = breed_voronoi(parent_props_1, parent_props_2, child_id)
    else:
        child = breed_metaball(parent_props_1, parent_props_2, child_id)

    return child


def breed_rock(data, dist_rendered, dist_dna):
    try:
        parse_breed_data(data)
        parent_1 = data['parent_1']
        parent_2 = data['parent_2']
        child_id = data['child_id']
        child = breed(parent_1['properties'], parent_2['properties'], child_id)
        save_rock(child, child_id, dist_dna)
        render(child, dist_rendered)
    except ValueError as e:
        print(e)
