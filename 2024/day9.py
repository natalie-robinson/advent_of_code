#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 08:15:09 2025
@author: natalierobinson
"""
import itertools
import time

############################################################
def collapse_blocks(keys, in_dict):
    out_nums = []
    for k in keys:
        if k in in_dict.keys():
            out_nums += [int(str(in_dict[k][0][0]))] * in_dict[k][0][1]
            in_dict[k] = in_dict[k][1:][0]
            if in_dict[k] == 0:
                pass
            else:
                fill_space = in_dict[k]
                # Move blocks from the back
                while fill_space > 0:
                    # Identify available blocks
                    pull_from = list(in_dict.keys())[-1]
                    if pull_from > k:
                        pull_num = in_dict[pull_from][0]
                        # Move whole block
                        if pull_num[1] <= fill_space:
                            fill_space -= pull_num[1]
                            # Update the list
                            out_nums += [int(str(in_dict[pull_from][0][0]))] * in_dict[pull_from][0][1]
                            in_dict[0] = [fill_space]
                            in_dict.pop(pull_from, None)
                        else:
                            out_nums += [int(str(in_dict[pull_from][0][0]))] * fill_space
                            in_dict[pull_from][0] = (in_dict[pull_from][0][0], in_dict[pull_from][0][1] - fill_space)
                            fill_space = 0
                    else:
                        break
    return(in_dict, out_nums)


def collapse_blocks_2(keys, in_dict):
    out_nums = []
    k_rev = keys[-1]
    k = keys[0]
    while k < k_rev:
        fill_space = in_dict[k][-1]
        if in_dict[k_rev][0][1] <= fill_space:
            moved = in_dict[k_rev][0][1]
            fill_space -= moved
            in_dict[k] = in_dict[k][:-1] + [in_dict[k_rev][0]] + [fill_space]
            in_dict[k_rev].pop(0)
            in_dict[(k_rev - 1)][-1] += moved
            k_rev -= 1
            k = 0
            pass
        else:
            k += 1
            if k == k_rev:
                k_rev -= 1
                k = 0
                pass
    
    for k in in_dict.keys():
        out_nums += list(itertools.chain(*[[int(str(elem[0]))] * elem[1] if isinstance(elem, tuple) else [0] * elem for elem in in_dict[k] ]))
    return(in_dict, out_nums)
       

def create_dict(in_map):
    out_dict = {}
    
    if len(in_map) % 2 > 0:
        in_map += '0'
        
    keys = []
    for i in range(0,len(in_map), 2):
        keys += [int(i/2)]
        out_dict[int(i/2)] = [(int(i/2), int(in_map[i])), int(in_map[(i+1)])]
    
    return(out_dict, keys)


############################################################
day = 9
dir_path = '/users/natalierobinson/Desktop/github/advent_of_code/2024/'
puzzle_path = dir_path + 'day' + str(day) + '.txt'

with open(puzzle_path, 'r') as f:
    disk_map = f.read().strip().split('\n')[0]

############################################################

# disk_map = '2333133121414131402'

############################################################
# Puzzle 1
t0 = time.time()

# Create dictionary
disk_dict, keys = create_dict(disk_map)

# Collapse blocks
disk_dict, final_nums = collapse_blocks(keys, disk_dict)         

# Get checksum
check_sum = 0
for i, value in enumerate(final_nums):
    check_sum += i * value

print(check_sum)  # 6370402949053

t1 = time.time()
t1-t0  # 0.2777121067047119

############################################################
# Puzzle 2
t0 = time.time()

# Create dictionary
disk_dict, keys = create_dict(disk_map)
# in_dict = disk_dict

# Collapse blocks
disk_dict, final_nums = collapse_blocks_2(keys, disk_dict)   

# Get checksum
check_sum = 0
for i, value in enumerate(final_nums):
    check_sum += i * value
   
print(check_sum)  # 6398096697992

t1 = time.time()
t1-t0  # 2.4789929389953613
