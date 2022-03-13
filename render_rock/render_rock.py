import sys
sys.path.append("")  # NOQA
from common.parser_utils import parse_argv
from render_rock.render_utils import render_metaball, render_voronoi


def render(dna, dist):
    family = dna['family']
    if family == 'voronoi':
        render_voronoi(dna, dist)
    elif family == 'metaball':
        render_metaball(dna, dist)


if __name__ == '__main__':
    try:
        data, dist = parse_argv()
        render(data, dist)
    except ValueError as e:
        # TODO: do something else with the error
        print(e)
