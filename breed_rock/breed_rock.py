import sys
sys.path.append("")  # NOQA
from breed_rock.constants import CHILD_ID, PARENT1, PARENT2
from common.constants import VORONOI
from breed_rock.breed_utils import breed_metaball, breed_voronoi, create_parents, parse_breed_data, save_rock
from render_rock.render_rock import render


def breed(parent1_dna, parent2_dna, child_id, family):
    """	Breed a child rock by randomizing the parents' properties

    Args:
        parent1 (dict): properties of the first parent
        parent2 (dict): properties of the second parent
        child_id (str): child id
        family (str): parents' family

    Returns:
        Voronoi | Metaball: child entity
    """
    if family == VORONOI:
        child = breed_voronoi(parent1_dna, parent2_dna, child_id, family)
    else:
        child = breed_metaball(parent1_dna, parent2_dna, child_id, family)
    return child


def breed_rock(data, dist_rendered, dist_dna):
    """Reformat the input data
       Create and save the child entity
       Render the child entity

    Args:
        data (dict): _description_
        dist_rendered (str): destination of the child's image (.png)
        dist_dna (str): destination of the child's dna (.json)
    """
    try:
        # parse input
        parse_breed_data(data)

        # init child entity
        parent1, parent2, family = create_parents(
            data[PARENT1], data[PARENT2])
        child_id = data[CHILD_ID]
        child = breed(parent1.properties, parent2.properties, child_id, family)

        # save and render child entity
        save_rock(child, dist_dna)
        render(child, family, dist_rendered)
    except ValueError as e:
        print(e)
