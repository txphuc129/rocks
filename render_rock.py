import os
import sys
import json
sys.path.append("")
from voronoi import render_voronoi
from metaball import render_metaball
import breed_utils


def render(dna):
    family = dna['family']
    if family == 'voronoi':
        render_voronoi(dna)
    elif family == 'metaball':
        render_metaball(dna)


if __name__ == '__main__':
    dna = breed_utils.load_rock(0)
    render(dna)
