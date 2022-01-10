import bpy
import random
import sys
from mathutils import Vector
import render_utils
import breed_utils


def createMetaball(origin=(0, 0, 0), n=30, r0=4, r1=2.5):
    metaball = bpy.data.metaballs.new('MetaBall')
    obj = bpy.data.objects.new('MetaBallObject', metaball)
    bpy.context.collection.objects.link(obj)

    metaball.resolution = 0.2
    metaball.render_resolution = 0.05

    for i in range(n):
        location = Vector(origin) + Vector(random.uniform(-r0, r0) for i in range(3))

        element = metaball.elements.new()
        element.co = location
        element.radius = r1

    return obj


def breed_metaball(dad, mom, id):
    child = {}
    child['id'] = id
    child['family'] = "metaball"
    child['density'] = breed_utils.int(dad['density'], mom['density'], 0, 10000)
    child['radius_0'] = breed_utils.float(dad['radius_0'], mom['radius_0'], 0, 4)
    child['radius_1'] = breed_utils.float(dad['radius_1'], mom['radius_1'], 0, 4)
    child['energy'] = breed_utils.int(dad['energy'], mom['energy'], 0, 100)
    return child


def render_metaball(dna):

    # Remove all elements
    render_utils.remove_all()

    # Create camera
    target = render_utils.create_target()
    camera = render_utils.create_camera((-10, -10, 10), target)

    # Create lights
    render_utils.rainbow_lights(10, 100, 3, energy=dna['energy'])

    # Create metaball
    obj = createMetaball(n=dna['density'], r0=dna['radius_0'], r1=dna['radius_1'])

    # Create material
    mat = render_utils.create_material(metalic=0.5)
    obj.data.materials.append(mat)

    # transparent background
    bpy.context.scene.render.film_transparent = True
    bpy.context.scene.render.image_settings.color_mode = 'RGBA'

    # Render scene
    render_utils.render('rocks', 'rock' + str(dna['id']), 512, 512)
