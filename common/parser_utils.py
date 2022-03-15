import argparse
import json
import sys


def parse_argv():
    """Parge the arguments received through the sys.argv from the command line

    Raises:
            ValueError: invalid command in command line

    Returns:
            str: json object containing info of parents and child
            str: rendered png location
            str: json dna location
            str: file to execute
    """

    argv = sys.argv

    if '--' not in argv:
        raise ValueError(
            'Missing \'--\' to separate blender and python arguments')

    # get the args after '--'
    argv = argv[argv.index('--') + 1:]
    if len(argv) != 4:
        # TODO: raise error
        raise ValueError('Missing arguments')

    usage_text = ('Process the parents and child data')
    parser = argparse.ArgumentParser(description=usage_text)

    parser.add_argument(
        '--data', dest='data', type=str, required=True,
        help='JSON object containing info of parents and child',
    )
    parser.add_argument(
        '--dist_rendered', dest='dist_rendered', type=str, required=True,
        help='Rendered png location',
    )
    parser.add_argument(
        '--dist_dna', dest='dist_dna', type=str, required=True,
        help='JSON dna location',
    )
    parser.add_argument(
        '--file_exec', dest='file_exec', type=str, required=True,
        help='File to execute',
    )

    parser.print_help()

    args = parser.parse_args(argv)

    return json.loads(args.data), args.dist_rendered, args.dist_dna, args.file_exec


def parse_voronoi_props(properties):
    # check the remaining properties for voronoi
    if 'density' not in properties:
        raise ValueError('Missing density')
    if 'radius' not in properties:
        raise ValueError('Missing radius')
    if 'palette' not in properties:
        raise ValueError('Missing palette')


def parse_metaball_props(properties):
    # check the remaining properties for metaball and replace the data with pythonic syntax
    if 'density' not in properties:
        raise ValueError('Missing density')
    if 'radius0' not in properties:
        raise ValueError('Missing radius0')
    properties['radius_0'] = properties['radius0']
    del properties['radius0']
    if 'radius1' not in properties:
        raise ValueError('Missing radius1')
    properties['radius_1'] = properties['radius1']
    del properties['radius1']
    if 'energy' not in properties:
        raise ValueError('Missing energy')
