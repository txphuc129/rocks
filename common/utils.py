import argparse
import json
import sys

from common.exceptions import MISSING_SEPARATOR, MISSING_VALUE
from common.constants import FAMILY, PROPERTIES


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
        raise ValueError(MISSING_SEPARATOR)

    # get the args after '--'
    argv = argv[argv.index('--') + 1:]
    if len(argv) != 4:
        raise ValueError(MISSING_VALUE + ': arguments')

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


def get_family(dna):
    """Return the family property of a dna

    Args:
        dna (dict): data of a rock

    Raises:
        ValueError: Missing properties
        ValueError: Missing family

    Returns:
        str: a str of family
    """
    if PROPERTIES not in dna:
        raise ValueError(MISSING_VALUE + ': properties')
    properties = dna[PROPERTIES]

    if FAMILY not in properties:
        raise ValueError(MISSING_VALUE + ': family')
    family = properties[FAMILY]
    return family
