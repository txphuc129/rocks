import argparse
import json
import sys


def parse_argv():
	"""
	Parge the arguments received through the sys.argv from the command line
	:return: args.data, args.dist
	"""
	argv = sys.argv

	if "--" not in argv:
		raise ValueError('Error: Missing \'--\' to separate blender and python arguments')
	
	# get the args after "--"
	argv = argv[argv.index("--") + 1:]
	if len(argv) != 2:
		# TODO: raise error
		raise 

	usage_text = ("Process the parents and child data")
	parser = argparse.ArgumentParser(description=usage_text)

	parser.add_argument(
		"--data", dest="data", type=str, required=True,
		help="JSON object containing info of parents and child",
	)
	parser.add_argument(
		"--dist", dest="dist", type=str, required=True,
		help="File location",
	)

	parser.print_help()

	args = parser.parse_args(argv)

	return parse_data(args.data), args.dist


def parse_data(data):
	data = json.loads(data)
	data["child_id"] = data["childId"]
	del data["childId"]
	return data
