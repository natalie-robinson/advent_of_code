###########################################################
import itertools
import  re
import time

############################################################
def get_ant_locations(in_map):
    out_dict={}
    for r in range(len(in_map)):
        for m in re.finditer('\d|[a-z]|[A-Z]', in_map[r]):
            out_dict[m.group()] = [(r,m.start())] if not m.group() in out_dict.keys() else out_dict[m.group()] + [(r,m.start())]
    return(out_dict)


def get_antinodes(antinodes, a, b, max_r, max_c):
    diff = (a[0] - b[0], a[1] - b[1])
    try:
        if 0 <= a[0]+diff[0] < max_r and 0 <= a[1]+diff[1] < max_c:
            antinodes.add((a[0]+diff[0], a[1]+diff[1]))
        if 0 <= b[0]-diff[0] < max_r and 0 <= b[1]-diff[1] < max_c:
            antinodes.add((b[0]-diff[0], b[1]-diff[1]))
    except ValueError:
            pass  # Handle invalid operations gracefully
    return (antinodes)

def get_t_antinodes(antinodes, a, b, max_r, max_c):
    diff = (a[0] - b[0], a[1] - b[1])
    try:
        while 0 <= a[0]+diff[0] < max_r and 0 <= a[1]+diff[1] < max_c:
            antinodes.add((a[0]+diff[0], a[1]+diff[1]))
            a = [a[0]+diff[0], a[1]+diff[1]]
        while 0 <= b[0]-diff[0] < max_r and 0 <= b[1]-diff[1] < max_c:
            antinodes.add((b[0]-diff[0], b[1]-diff[1]))
            b = [b[0]-diff[0], b[1]-diff[1]]
    except ValueError:
            pass  # Handle invalid operations gracefully
    return (antinodes)

############################################################
day = 8
dir_path = '/users/natalierobinson/Desktop/github/advent_of_code/2024/'
puzzle_path = dir_path + 'day' + str(day) + '.txt'

with open(puzzle_path, 'r') as f:
    ant_map = f.read().strip().split('\n')

############################################################
# ant_map = '............ ........0... .....0...... .......0.... ....0....... ......A..... ............ ............ ........A... .........A.. ............ ............'
# ant_map = ant_map.split(' ')

############################################################
ant_dict = get_ant_locations(ant_map)

############################################################
# Puzzle 1
t0 = time.time()

antinodes = set()
for k in ant_dict:
    for pair in itertools.combinations(ant_dict[k], 2):
        antinodes = get_antinodes(antinodes, *pair, len(ant_map), len(ant_map[0]))
       
print(len(antinodes))
    
t1 = time.time()
t1-t0  # 0006120204925537109

############################################################
# Puzzle 2
t0 = time.time()

antinodes = set()
for k in ant_dict:
    type_antinodes = set(ant_dict[k])
    for pair in itertools.combinations(ant_dict[k], 2):
        # antinodes = get_t_antinodes(antinodes, *pair, len(ant_map), len(ant_map[0]))
        type_antinodes = get_t_antinodes(type_antinodes, *pair, len(ant_map), len(ant_map[0]))
        antinodes = antinodes.union(type_antinodes)

print(len(antinodes))

t1 = time.time()
t1-t0  # 0.003831148147583008