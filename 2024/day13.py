#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 08:15:09 2025
@author: natalierobinson
"""
import numpy as np 
import pandas as pd
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

############################################################
max_pushes = 100

############################################################
push_a = 0  # Counter for button pushes
push_b = 0
x_list = [0]
y_list = [0]
a_cost = 3
b_cost = 1

i = 0

final_x = int(re.findall(r'X=(.*),', prize[i])[0])
final_y = int(re.findall(r'Y=(.*)', prize[i])[0]) 
while push_a < 101 and push_b < 101 and final_x not in x_list and final_y not in y_list:
    
   
    

############################################################
# Initialize

############################################################
# Puzzle 1
t0 = time.time()

        
t1 = time.time()
t1-t0  
  


############################################################
        
        