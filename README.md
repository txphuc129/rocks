# Rocks

## Setup

1. Download [Blender](https://www.blender.org/download/).
2. Install [scipy](https://scipy.org/install/).
3. Run Blender command line:

```bash
blender -b -P root.py -- --data='{JSON object}' --dist_rendered='rendered_png_location' --dist_dna='dna_location' --file_exec='your_blender_script'
```

If you're running on your local Mac machine, use this:

```bash
/Applications/Blender.app/Contents/MacOS/Blender -b -P root.py -- --data='{JSON object}' --dist_rendered='rendered_png_location' --dist_dna='dna_location' --file_exec='your_blender_script'
```

## Render Rocks

```bash
blender -b -P root.py -- --data='{JSON object}' --dist_rendered='/rocks/dist/rendered' --dist_dna='' --file_exec='render_rock'
```

### The Voronoi Family

```bash
/Applications/Blender.app/Contents/MacOS/Blender -b -P root.py -- --data='{"id": "1", "properties": { "family": "voronoi", "density": 2000, "radius": 2, "palette": [[244, 101, 160], [168, 111, 179], [201, 21, 85], [107, 40, 129], [47, 21, 37]]}}' --dist_rendered='/rocks/dist/rendered' --dist_dna='' --file_exec='render_rock'
```

[Rock 0 DNA](https://github.com/rove-to/rocks/blob/main/dna/rock0.json)

![Rock 0](https://raw.githubusercontent.com/rove-to/rocks/main/rocks/rock0.png)

[Rock 1 DNA](https://github.com/rove-to/rocks/blob/main/dna/rock1.json)

![Rock 1](https://raw.githubusercontent.com/rove-to/rocks/main/rocks/rock1.png)

### The Metaball Family

```bash
/Applications/Blender.app/Contents/MacOS/Blender -b -P root.py -- --data='{"id": "4", "properties": {"family": "metaball", "density": 1000, "radius0": 2, "radius1": 4, "energy": 50}}' --dist_rendered='/rocks/dist/rendered' --dist_dna='' --file_exec='render_rock'
```

[Rock 3 DNA](https://github.com/rove-to/rocks/blob/main/dna/rock3.json)

![Rock 3](https://raw.githubusercontent.com/rove-to/rocks/main/rocks/rock3.png)

[Rock 4 DNA](https://github.com/rove-to/rocks/blob/main/dna/rock4.json)

![Rock 4](https://raw.githubusercontent.com/rove-to/rocks/main/rocks/rock4.png)

## Breed Rocks

```bash
blender -b -P root.py -- --data='{JSON object}' --dist_rendered='/rocks/dist/rendered' --dist_dna='/rocks/dist/dna' --file_exec='breed_rock'
```

### Voronoi Spawning

```bash
/Applications/Blender.app/Contents/MacOS/Blender -b -P root.py -- --data='{"childId": "2","parent1": {"id": "0", "properties": {"family": "voronoi", "density": 2000, "radius": 2, "palette": [[89, 91, 90], [20, 195, 162], [13, 229, 168], [124, 244, 154], [184, 253, 153]]}}, "parent2": {"id": "1", "properties": {"family": "voronoi", "density": 2000, "radius": 2, "palette": [[244, 101, 160], [168, 111, 179], [201, 21, 85], [107, 40, 129], [47, 21, 37]]}}}' --dist_rendered='/rocks/dist/rendered' --dist_dna='/rocks/dist/dna' --file_exec='breed_rock'
```

Rock 0 + Rock 1 = Rock 2

[Rock 2 DNA](https://github.com/rove-to/rocks/blob/main/dna/rock2.json)

![Rock 2](https://raw.githubusercontent.com/rove-to/rocks/main/rocks/rock2.png)

### Metaball Spawning

```bash
/Applications/Blender.app/Contents/MacOS/Blender -b -P root.py -- --data='{"childId": "5","parent1": {"id": "3", "properties": {"family": "metaball", "density": 150, "radius0": 4, "radius1": 2.5, "energy": 100}}, "parent2": {"id": "4", "properties": {"family": "metaball", "density": 1000, "radius0": 2, "radius1": 4, "energy": 50}}}' --dist_rendered='/rocks/dist/rendered' --dist_dna='/rocks/dist/dna' --file_exec='breed_rock'
```

Rock 3 + Rock 4 = Rock 5

[Rock 5 DNA](https://github.com/rove-to/rocks/blob/main/dna/rock5.json)

![Rock 5](https://raw.githubusercontent.com/rove-to/rocks/main/rocks/rock5.png)
