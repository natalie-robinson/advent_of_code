#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 08:15:09 2025
@author: natalierobinson
"""
import numpy as np 
import time

############################################################
day = 12
dir_path = '/users/natalierobinson/Desktop/github/advent_of_code/2024/'
puzzle_path = dir_path + 'day' + str(day) + '.txt'
    
# with open(puzzle_path, 'r') as f:
#     garden_map = f.read().strip().split('\n')

# garden_map = np.array([list(i) for i in garden_map])

############################################################
garden_map = 'AAAA BBCD BBCC EEEC'
# garden_map = 'RRRRIICCFF RRRRIICCCF VVRRRCCFFF VVRCCCJFFF VVVVCJJCFE VVIVCCJJEE VVIIICJJEE MIIIIIJJEE MIIISIJEEE MMMISSJEEE'
garden_map = np.array([list(i) for i in garden_map.split(' ')])

############################################################


############################################################
# Initialize
neighbors = [(-1,0),(0,1),(1,0),(0,-1)]
fences = []

############################################################
# Puzzle 1
t0 = time.time()
plants = [(x, y) for x in range(len(garden_map)) for y in range(len(garden_map[0]))]

# Depth-first search to find all connected 1s and count fences as you go
while plants:
    start = plants[0]  # Grab a plant
    patch = [start]
    area, perim = 0, 0
    plant_type = garden_map[start]

    while patch:
        check_row, check_col = patch.pop()
        area += 1

        for dr, dc in neighbors:
            new_row, new_col = check_row + dr, check_col + dc

            if (new_row < 0 or new_row >= garden_map.shape[0] or new_col < 0 or new_col >= garden_map.shape[1]):
                perim += 1
            elif garden_map[new_row][new_col] != plant_type:
                perim += 1
            else:
                neighbor = (new_row, new_col)
                if neighbor in plants:
                    plants.remove(neighbor)
                    patch.append(neighbor)

    fences.append(area * perim)
        
t1 = time.time()
t1-t0  # 0.049139976501464844
  
sum(fences) # 1396562

############################################################
corners = []

def check_next_plant(area, perim, r, c, in_map, plant_oi):
    check_next = []
    for col in range(c,in_map.shape[1]):
        p = in_map[r][col]
        if p == plant_oi:
            if len(check_next) == 0:
                perim += 1    # Top edge
            area += 1    
            if (r,col) in all_coords:
                all_coords.remove((r,col))

            # Check plant in next column
            if col+1 > in_map.shape[0]-1:
                perim += 1   # Right edge
                pass
            else:
                if in_map[r][c+1] != plant_oi:
                    perim += 1    # Right edge
            # Check plant in next row down
            if r+1 > in_map.shape[0]-1 or in_map[r+1][c] != plant_oi:
                perim += 1    # Bottom edge
            else:
                check_next += [(r+1,col)]  # Stash to keep checking in next row
        else:
            perim += 1   # Right edge
    if len(check_next) > 0:
        area, perim, check_next = check_next_plant(area, perim, check_next[0][0], check_next[0][1], in_map, plant_oi)
                
    return area, perim, check_next
                

all_coords = set((x, y) for x in range(len(garden_map)) for y in range(len(garden_map[0])))
fences = []
while all_coords:
    ac = all_coords.pop()
    plant_oi = garden_map[ac]
    area, perim = 0, 1 # Initiate area and left fence
    
    area, perim, check_next = check_next_plant(area, perim, ac[0], ac[1], garden_map, plant_oi)
    fences.append(area * perim)
        
        