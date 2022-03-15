import sys
sys.path.append("")  # NOQA
from common.parser_utils import parse_argv
from render_rock.render_utils import parse_render_data, render_metaball, render_voronoi


def render(dna, dist):
    properties = dna['properties']
    family = properties['family']
    if family == 'voronoi':
        render_voronoi(dna, dist)
    elif family == 'metaball':
        render_metaball(dna, dist)


def render_rock(data, dist):
    try:
        parse_render_data(data)
        render(data, dist)
    except ValueError as e:
        print(e)
