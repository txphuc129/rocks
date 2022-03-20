import sys
sys.path.append("")  # NOQA

from render_rock.render_utils import create_rock, render_metaball, render_voronoi
from common.constants import METABALL, VORONOI
from common.utils import get_family


def render(rock, family, dist):
    if family == VORONOI:
        render_voronoi(rock, dist)
    elif family == METABALL:
        render_metaball(rock, dist)


def render_rock(data, dist):
    try:
        family = get_family(data)
        rock = create_rock(data, family)
        render(rock, family, dist)
    except BaseException as e:
        print(e)
