import argparse
import json
import sys


def parse_argv():
    """Parge the arguments received through the sys.argv from the command line

    Raises:
            ValueError: invalid command in command line

    Returns:
            str: json object containing info of parents and child
            str: file location
    """

    argv = sys.argv

    if '--' not in argv:
        raise ValueError(
            'Missing \'--\' to separate blender and python arguments')

    # get the args after '--'
    argv = argv[argv.index('--') + 1:]
    if len(argv) != 2:
        # TODO: raise error
        raise

    usage_text = ('Process the parents and child data')
    parser = argparse.ArgumentParser(description=usage_text)

    parser.add_argument(
        '--data', dest='data', type=str, required=True,
        help='JSON object containing info of parents and child',
    )
    parser.add_argument(
        '--dist', dest='dist', type=str, required=True,
        help='File location',
    )

    parser.print_help()

    args = parser.parse_args(argv)

    return parse_data(args.data), args.dist


def parse_data(data):
    """Reformat the data to match python convention then convert it to a dictionary

    Args:
            data (str): a string of json object

        Returns:
            dict: a dictionary of parent_1, parent_2, and child_id
    """

    data = json.loads(data)
    if 'childId' in data:
        data['child_id'] = data['childId']
        del data['childId']
    if 'parent1' in data:
        data['parent_1'] = data['parent1']
        del data['parent1']
    if 'parent2' in data:
        data['parent_2'] = data['parent2']
        del data['parent2']

    if 'parent_1' in data:
        parent_1 = data['parent_1']
        if 'properties' in parent_1:
            properties = parent_1['properties']
            if 'radius0' in properties:
                properties['radius_0'] = properties['radius0']
                del properties['radius0']
            if 'radius1' in properties:
                properties['radius_1'] = properties['radius1']
                del properties['radius1']

    return data
