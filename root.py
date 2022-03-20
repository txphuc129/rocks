import sys
sys.path.append("")  # NOQA
from common.constants import BREED_ROCK, RENDER_ROCK
from common.exceptions import INVALID_FILE
from breed_rock.breed_rock import breed_rock
from common.utils import parse_argv
from render_rock.render_rock import render_rock


if __name__ == '__main__':
    try:
        data, dist_rendered, dist_dna, file_exec = parse_argv()
        if file_exec == BREED_ROCK:
            breed_rock(data, dist_rendered, dist_dna)
        elif file_exec == RENDER_ROCK:
            render_rock(data, dist_rendered)
        else:
            raise ValueError(INVALID_FILE)
    except BaseException as e:
        print(e)
