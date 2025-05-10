#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 08:15:09 2025

@author: natalierobinson
"""
import numpy as np 
import time

############################################################
day = 10
dir_path = '/users/natalierobinson/Desktop/github/advent_of_code/2024/'
puzzle_path = dir_path + 'day' + str(day) + '.txt'
    
with open(puzzle_path, 'r') as f:
    trail_map = f.read().strip().split('\n')

trail_map = np.array([list(i) for i in trail_map])

############################################################

trail_map = '89010123 78121874 87430965 96549874 45678903 32019012 01329801 10456732'
# trail_map = '4490449 4441498 4442447 6543456 7651987 8764444 9874444'   # sm example for puzzle 2
# trail_map = '012345 123456 234567 345678 416789 567891'  # seconde sm example for puzzle 2
trail_map = np.array([list(trail_map.split(' ')[i]) for i in range(len(trail_map.split(' ')))])

############################################################
# Initiate
starts = np.argwhere(trail_map == '0')
dirs = [(-1,0),(0,1),(1,0),(0,-1)]  # N/E/S/W row and columns changes

############################################################
# Puzzle 1
t0 = time.time()
tr_sum = 0
for st in starts:
    i = 0
    check_set = {tuple(st)}  # Use a set for efficient duplicate checks
    while i < 9:
        new_positions = set()
        for x, y in check_set:
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                # Check boundaries and the trail map value
                if 0 <= nx < trail_map.shape[0] and 0 <= ny < trail_map.shape[1]:
                    if int(trail_map[nx, ny]) == i + 1:
                        new_positions.add((nx, ny))
        check_set = new_positions  # Update to new positions
        i += 1
    tr_sum += len(check_set)

t1 = time.time()
t1-t0  # 0.01674485206604004
    
############################################################
# Puzzle 2    
t0 = time.time()    
all_tr_sum = 0
for st in starts:
    check_num = 0
    check_set = {tuple(st)}  # Use a set for efficient duplicate checks
    while check_num < 9:
        tr_sum = 0
        new_positions = []
        for x, y in check_set:
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                # Check boundaries and the trail map value
                if 0 <= nx < trail_map.shape[0] and 0 <= ny < trail_map.shape[1]:
                    if int(trail_map[nx, ny]) == check_num + 1:
                        new_positions.append((nx, ny))
        check_set = new_positions  # Update to new positions
        tr_sum += len(check_set)
        check_num += 1
    all_tr_sum += tr_sum

print(all_tr_sum)

t1 = time.time()
t1-t0  # 0.021353960037231445