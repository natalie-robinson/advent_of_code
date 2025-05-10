#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 12:13:27 2024
@author: natalierobinson
"""
###########################################################
import re

###########################################################
day = 6
dir_path = '/users/natalierobinson/Desktop/github/advent_of_code/2024/'
puzzle_path = dir_path + 'day' + str(day) + '.txt'

with open(puzzle_path, 'r') as f:
    guard_map = f.read().strip().split('\n')

###########################################################
guard_map = '....#..... .........# .......... ..#....... .......#.. .......... .#..^..... ........#. #......... ......#...'
import numpy as np
guard_map = np.array(guard_map.split(' '))

###########################################################
# Initialize
pattern = '.*(<|>|v|\\^)'
move_dirs = ['^','>','v','<']
r_c_changes = [(-1,0),(0,1),(1,0),(0,-1)]

(r, c, move_dir) = [(r, len(re.search(pattern, guard_map[r])[0]) - 1, re.search(pattern, guard_map[r])[1]) for r in range(len(guard_map)) if re.search(pattern, guard_map[r])][0]
idx = [i for i in range(len(move_dirs)) if move_dirs[i] == move_dir][0]
move_row, move_col = r_c_changes[idx][0], r_c_changes[idx][1]

###########################################################
# Puzzle 1
steps = []
all_clear = True
while all_clear:
    if (r >= 0 and r < len(guard_map)) and (c >= 0 and c < len(guard_map[0])):
        new_row, new_col = r + move_row, c + move_col
        if guard_map[new_row][new_col] == '#':
            idx += 1
            if idx > len(move_dirs) - 1:
                idx = idx - len(move_dirs)
            move_dir, move_row, move_col = move_dirs[idx], r_c_changes[idx][0], r_c_changes[idx][1]
        else:
            r, c = new_row, new_col
            if [r,c] not in steps:
                steps += [[r,c]]
    else:
        all_clear = False

len(steps)  # 4696

###########################################################
# Puzzle 2
# For each step taken, test if adding an obstacle will result in the guard coming back to that position
steps = []
obstacles = 0
all_clear = True
while all_clear:
    if (r >= 0 and r < len(guard_map)) and (c >= 0 and c < len(guard_map[0])):
        # Place obstacle and test path
        inner_r, inner_c = r, c
        inner_loop = [[inner_r, inner_c]]
        inner_idx = idx+1
        if inner_idx > len(move_dirs) - 1:
            inner_idx = inner_idx - len(move_dirs)
        inner_move_dir, inner_move_row, inner_move_col = move_dirs[inner_idx],  r_c_changes[inner_idx][0], r_c_changes[inner_idx][1]
        inf_loop = False
        while not inf_loop:
            new_inner_row, new_inner_col = inner_r + inner_move_row, inner_c + inner_move_col
            if (new_inner_row >= 0 and new_inner_row < len(guard_map)) and (new_inner_col >= 0 and new_inner_col < len(guard_map[0])):
                if guard_map[new_inner_row][new_inner_col] == '#':
                    inner_idx += 1
                    if inner_idx > len(move_dirs) - 1:
                        inner_idx = inner_idx - len(move_dirs)
                    inner_move_dir, inner_move_row, inner_move_col = move_dirs[inner_idx], r_c_changes[inner_idx][0], r_c_changes[inner_idx][1]
                else:
                    inner_r, inner_c = new_inner_row, new_inner_col
                    if inner_loop[0] != [inner_r,inner_c]:
                        inner_loop += [[inner_r,inner_c]]
                    else:
                        obstacles += 1
                        inf_loop = True
            else:
                inf_loop = True
    
        # Carry on with normal walk
        new_row, new_col = r + move_row, c + move_col
        next_step = '#'
        if guard_map[new_row][new_col] == '#':
            idx += 1
            if idx > len(move_dirs) - 1:
                idx = idx - len(move_dirs)
            move_dir, move_row, move_col = move_dirs[idx], r_c_changes[idx][0], r_c_changes[idx][1]
        else:
            r, c = new_row, new_col
            if [r,c] not in steps:
                steps += [[r,c]]
    else:
        all_clear = False

# I give up - I don't care anymore. The answer is 1443