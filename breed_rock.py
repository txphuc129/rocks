import sys
sys.path.append("")

from breed_utils import save_rock
from parser_utils import parse_argv
from render_rock import render
from voronoi import breed_voronoi
from metaball import breed_metaball


def breed(parent1, parent2, child_id):
	parent_properties1 = parent1['properties']
	parent_properties2 = parent2['properties']
	print(parent_properties1)
	if (parent_properties1['family'] == parent_properties2['family']):
		family = parent_properties1['family']
		if family == 'voronoi':
			child = breed_voronoi(parent_properties1, parent_properties2, child_id)
		elif family == 'metaball':
			child = breed_metaball(parent_properties1, parent_properties2, child_id)
		else:
			raise ValueError('Unidentifiable family')
	return child


if __name__ == '__main__':
	try:
		data, dist = parse_argv()
		# print(f'Data: {data}')
		# print(f'Dist: {dist}')
		parent1 = data['parent1']
		parent2 = data['parent2']
		child_id = data['child_id']
		
		child = breed(parent1, parent2, child_id)

		save_rock(child, child_id)

		render(child)
	except ValueError as e:
		# TODO: do something else with the error
		print(e)
    
