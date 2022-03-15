import sys
sys.path.append("")  # NOQA
from breed_rock.breed_rock import breed_rock
from common.parser_utils import parse_argv
from render_rock.render_rock import render_rock


if __name__ == '__main__':
    try:
        data, dist_rendered, dist_dna, file_exec = parse_argv()
        if file_exec == 'breed_rock':
            breed_rock(data, dist_rendered, dist_dna)
        elif file_exec == 'render_rock':
            render_rock(data, dist_rendered)
        else:
            raise ValueError('Invalid file to execute')
    except ValueError as e:
        print(e)
