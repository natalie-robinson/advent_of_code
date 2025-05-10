#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 08:15:09 2025
@author: natalierobinson
"""
import time

############################################################
day = 11
dir_path = '/users/natalierobinson/Desktop/github/advent_of_code/2024/'
puzzle_path = dir_path + 'day' + str(day) + '.txt'
    
with open(puzzle_path, 'r') as f:
    stone_map = f.read().strip().split('\n')

stone_map = {n: 1 for n in stone_map[0].split(' ')}

############################################################

# stone_map = '0 1 10 99 999'
# stone_map = '125 17'
# stone_map =  {n: 1 for n in stone_map.split(' ')}

############################################################
# Puzzle 1
t0 = time.time()
iterations = 75   # Puzzle 1 = 25 iterations, puzzle 2 = 75 iterations
for i in range(iterations):
    # new_dict = defaultdict(int)
    new_dict = {}
    for k, v in stone_map.items():
        if k == '0':
            new_dict['1'] = v if not '1' in new_dict.keys() else v + new_dict['1']
        elif len(k) % 2 != 0:
            new_dict[str(int(k)*2024)] = v if not str(int(k)*2024) in new_dict.keys() else v + new_dict[str(int(k)*2024)]
        else:
            mid = len(k) // 2
            left = k[:mid].lstrip('0') or '0'
            right = k[mid:].lstrip('0') or '0'
            new_dict[left] = v if not left in new_dict.keys() else v + new_dict[left]
            new_dict[right] = v if not right in new_dict.keys() else v + new_dict[right]
    stone_map = new_dict
            
t1 = time.time()
t1-t0  # 0.0021545886993408203 for puzzle 1, 217812 stones. 0.07508182525634766 for puzzle 2, 259112729857522 stones

sum(stone_map.values())
