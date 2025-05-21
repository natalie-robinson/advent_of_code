#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 08:15:09 2025
@author: natalierobinson
"""
import heapq
import re
import time


############################################################
day = 13
dir_path = '/users/natalierobinson/Desktop/github/advent_of_code/2024/'
puzzle_path = dir_path + 'day' + str(day) + '.txt'

f = open(puzzle_path, 'r').read().strip()
a = re.findall(r'Button A: (.*)', f)    
b = re.findall(r'Button B: (.*)', f)
prize = re.findall(r'Prize: (.*)', f)

# a = 'X+94, Y+34'
# b = 'X+22, Y+67'
# prize = 'X=8400, Y=5400'

############################################################
def parse_movement(button_str):
    x = int(re.search(r'X\+(\d+)', button_str).group(1))
    y = int(re.search(r'Y\+(\d+)', button_str).group(1))
    return (x, y)


def parse_prize(prize_str):
    x = int(re.search(r'X=(\d+)', prize_str).group(1))
    y = int(re.search(r'Y=(\d+)', prize_str).group(1))
    return (x, y)


def min_cost_path(start, destination, move_a, cost_a, move_b, cost_b):
    visited = set()
    heap = [(0, start, [])]  # (tokens, current_position, path_taken)

    while heap:
        tokens, (x, y), path = heapq.heappop(heap)

        if (x, y) == destination:
            return {
                "total_tokens": tokens,
                "path": path + [(x, y)]
            }

        if (x, y) in visited:
            continue
        visited.add((x, y))

        # Try both moves
        for move, cost, label in [(move_a, cost_a, "A"), (move_b, cost_b, "B")]:
            nx, ny = x + move[0], y + move[1]

            # Don't exceed destination coordinates (only positive moves allowed)
            if nx <= destination[0] and ny <= destination[1]:
                heapq.heappush(heap, (
                    tokens + cost,
                    (nx, ny),
                    path + [(x, y, label)]
                ))  # The less costly path will be pushed to the first position of the heap, by heapq
        
    return False  # Destination cannot be reached
    
############################################################
# Initialize
max_push = 100
start = (0, 0)
cost_a = 3
cost_b = 1

############################################################
# Puzzle 1
t0 = time.time()
      
tokens_spent = []
puz=0
for puz in range(len(a)):
    # Parse input
    move_a = parse_movement(a[puz])
    move_b = parse_movement(b[puz])
    destination = parse_prize(prize[puz])
    
    result = min_cost_path(start, destination, move_a, cost_a, move_b, cost_b)
    
    if result:
        total_a = len([r[-1] for r in result['path'] if r[-1] == 'A'])
        total_b = len([r[-1] for r in result['path'] if r[-1] == 'B'])
        if total_a <= max_push and total_b <= max_push:
            tokens_spent += [result["total_tokens"]]

sum(tokens_spent)   

t1 = time.time()
t1-t0  
  


############################################################
        
        