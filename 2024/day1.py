#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 15:04:30 2024
@author: natalierobinson
"""

###########################################################
day = 1

dir_path = '/users/natalierobinson/Desktop/github/advent_of_code/2024/'
puzzle_path = dir_path + 'day' + str(day) + '.txt'

with open(puzzle_path, 'r') as f:
    puzzle_input = f.read().strip().split('\n')
    
###########################################################
# Example data
l1 = [3,4,2,1,3,3]
l2 = [4,3,5,3,9,3]

###########################################################
# Puzzle 1
l1 = [int(p.split()[0]) for p in puzzle_input.split('\n')]
l2 = [int(p.split()[1]) for p in puzzle_input.split('\n')]

l1.sort()
l2.sort()

diffs = [abs(l2[i] - l1[i]) for i in range(len(l1))]
sum(diffs)  # 936063

###########################################################
# Puzzle 2
sim_list = []
for l in l1:
    sim_list += [l * l2.count(l)]

sim_score = sum(sim_list)
