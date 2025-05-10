#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 05:46:32 2024
@author: natalierobinson
"""
###########################################################
import operator
import time

day = 7
dir_path = '/users/natalierobinson/Desktop/github/advent_of_code/2024/'
puzzle_path = dir_path + 'day' + str(day) + '.txt'

with open(puzzle_path, 'r') as f:
    equns = f.read().strip().split('\n')

############################################################
# dat = '190: 10 19\n3267: 81 40 27\n83: 17 5\n156: 15 6\n7290: 6 8 6 15\n161011: 16 10 13\n192: 17 8 14\n21037: 9 7 18 13\n292: 11 6 16 20'
# equns = dat.split('\n')
 
###########################################################
def operate(a, b, puz=1):
    # Define available operations
    ops = {
        '+': operator.add,
        '*': operator.mul
    }
    if puz == 2:
        ops[''] = lambda x, y: int(str(x) + str(y))
    # Apply operations
    results = set()
    for op, func in ops.items():
        try:
            results.add(func(int(a), int(b)))
        except ValueError:
            pass  # Handle invalid operations gracefully
    return results


def correct_calibrations(equns, puz):
    correct_outcomes = []
    for eq in equns:
        ans, nums = int(eq.split(':')[0]), eq.split(': ')[1].split()
        results = set(operate(nums[0], nums[1], puz))
        nums = nums[2:]
        
        while nums:
            next_num = nums.pop(0)
            results = {res for r in results for res in operate(r, next_num, puz)}
        
        if ans in results:
            correct_outcomes.append(ans)
    
    return correct_outcomes


###########################################################
# Puzzle 1
t0 = time.time()

correct_outcomes = correct_calibrations(equns, 1)
sum(correct_outcomes)  # 4555081946288

t1 = time.time()
t1-t0  # 0.1293017864227295

###########################################################
# Puzzle 2
t0 = time.time()

correct_outcomes = correct_calibrations(equns,puz=2)
sum(correct_outcomes)  # 227921760109726

t1 = time.time()
t1-t0  # 7.452789068222046