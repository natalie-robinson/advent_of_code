#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 12:00:06 2024
@author: natalierobinson
"""
###########################################################
import re
import itertools
from collections import Counter

day = 3

dir_path = '/users/natalierobinson/Desktop/github/advent_of_code/2024/'
puzzle_path = dir_path + 'day' + str(day) + '.txt'
    
with open(puzzle_path, 'r') as f:
    puzzle_input = f.read().strip().split('\n')

puzzle_input = ''.join([l for l in puzzle_input])
    
###########################################################
def decode(instructions):
    inst = re.findall('mul\(\d+,\d+\)', instructions)
    muls = list(map(lambda i: int(re.search('\d+', i).group(0)) * int(re.search(',\d+', i).group(0).replace(',','')), inst))
    return(sum(muls))


def dos_and_donts(instructions):
    do_pattern = r'mul\(\d+,\d+\)'
    dont_pattern = r"don't.*?do(?!n't)|don't.*?$"
   
    # Get all multiplication instructions under consideration 
    inst_do = re.findall(do_pattern, instructions)
    muls_do = list(map(lambda i: re.search(do_pattern, i).group(0), inst_do))
    # Remove multiplication instructions between a don't and a do
    inst_ignore = re.findall(dont_pattern,instructions)
    muls_ignore = list(map(lambda i: re.findall(do_pattern, i) if re.findall(do_pattern, i) else None, inst_ignore))
    muls_ignore = list(itertools.chain(*[m for m in muls_ignore if m]))
    # Remove elements to ignore
    inst = list((Counter(muls_do)-Counter(muls_ignore)).elements())
    muls = list(map(lambda i: int(re.search('\d+', i).group(0)) * int(re.search(',\d+', i).group(0).replace(',','')), inst))
    return(sum(muls))


###########################################################
# puzzle_input = 'xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))'
# puzzle_input = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))don't_mul(1,2)sye*don'tkmul(1,2)"

###########################################################
# Puzzle 1
total = decode(puzzle_input) # 182780583

###########################################################
# Puzzle 2
total = dos_and_donts(puzzle_input)

