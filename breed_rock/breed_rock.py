import sys
sys.path.append("")  # NOQA
from breed_rock.breed_utils import breed_metaball, breed_voronoi
from common.parser_utils import parse_argv
from render_rock.render_rock import render


def breed(parent_1, parent_2, child_id):
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

    if parent_1['family'] != parent_2['family']:
        raise ValueError('Cannot breed two rocks with different families')

    family = parent_1['family']
    if family == 'voronoi':
        child = breed_voronoi(parent_1, parent_2, child_id)
    elif family == 'metaball':
        child = breed_metaball(parent_1, parent_2, child_id)
    else:
        raise ValueError('Unidentifiable family')

    return child


if __name__ == '__main__':
    try:
        data, dist = parse_argv()
        parent_1 = data['parent_1']
        parent_2 = data['parent_2']
        child_id = data['child_id']
        child = breed(parent_1['properties'], parent_2['properties'], child_id)
        render(child, dist)
    except ValueError as e:
        # TODO: do something else with the error
        print(e)
