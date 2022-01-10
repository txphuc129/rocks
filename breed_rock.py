import os
import sys
import json
sys.path.append("")
import breed_utils
from rock_render import render
from voronoi import breed_voronoi
from metaball import breed_metaball


def breed(dad_id, mom_id, child_id):
    dad = breed_utils.load_rock(dad_id)
    mom = breed_utils.load_rock(mom_id)
    if (dad['family'] == mom['family']):
        family = dad['family']
        if family == 'voronoi':
            child = breed_voronoi(dad, mom, child_id)
        elif family == 'metaball':
            child = breed_metaball(dad, mom, child_id)

    return child


if __name__ == '__main__':

    dad_id = 3
    mom_id = 4
    child_id = 5

    child = breed(dad_id, mom_id, child_id)

    breed_utils.save_rock(child, child_id)

    render(child)
