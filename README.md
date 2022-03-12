# Rocks

## Setup

1. Download [Blender](https://www.blender.org/download/).
2. Install [scipy](https://scipy.org/install/).
3. Run Blender command line:

```bash
blender -b -P your_blender_script.py -- --data='{JSON object}' --dist='/app/dist/'
```

If you're running on your local Mac machine, use this:

```bash
/Applications/Blender.app/Contents/MacOS/Blender -b -P your_blender_script.py -- --data='{JSON object}' --dist='/app/dist/'
```

## Command Line Arguments Example

### Data

```text
--data='{"childId": "2","parent1": {"id": "0", "properties": {"family": "voronoi", "density": 2000, "radius": 2, "palette": [[89, 91, 90], [20, 195, 162], [13, 229, 168], [124, 244, 154], [184, 253, 153]]}}, "parent2": {"id": "1", "properties": {"family": "voronoi", "density": 2000, "radius": 2, "palette": [[244, 101, 160], [168, 111, 179], [201, 21, 85], [107, 40, 129], [47, 21, 37]]}}}'
```

### Dist

```text
--dist='/app/dist/'
```

## Render Rocks

```bash
blender -b -P render_rock.py -- --data='{JSON object}' --dist='/app/dist/'
```

### The Voronoi Family

[Rock 0 DNA](https://github.com/rove-to/rocks/blob/main/dna/rock0.json)

![Rock 0](https://raw.githubusercontent.com/rove-to/rocks/main/rocks/rock0.png)

[Rock 1 DNA](https://github.com/rove-to/rocks/blob/main/dna/rock1.json)

![Rock 1](https://raw.githubusercontent.com/rove-to/rocks/main/rocks/rock1.png)

### The Metaball Family

[Rock 3 DNA](https://github.com/rove-to/rocks/blob/main/dna/rock3.json)

![Rock 3](https://raw.githubusercontent.com/rove-to/rocks/main/rocks/rock3.png)

[Rock 4 DNA](https://github.com/rove-to/rocks/blob/main/dna/rock4.json)

![Rock 4](https://raw.githubusercontent.com/rove-to/rocks/main/rocks/rock4.png)

## Breed Rocks

```bash
blender -b -P breed_rock.py -- --data='{JSON object}' --dist='/app/dist/'
```

### Voronoi Spawning

Rock 0 + Rock 1 = Rock 2

[Rock 2 DNA](https://github.com/rove-to/rocks/blob/main/dna/rock2.json)

![Rock 2](https://raw.githubusercontent.com/rove-to/rocks/main/rocks/rock2.png)

### Metaball Spawning

Rock 3 + Rock 4 = Rock 5

[Rock 5 DNA](https://github.com/rove-to/rocks/blob/main/dna/rock5.json)

![Rock 5](https://raw.githubusercontent.com/rove-to/rocks/main/rocks/rock5.png)
