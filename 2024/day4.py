#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 12:10:51 2024
@author: natalierobinson
"""
###########################################################
import numpy as np

day = 4
dir_path = '/users/natalierobinson/Desktop/github/advent_of_code/2024/'
puzzle_path = dir_path + 'day' + str(day) + '.txt'
    
with open(puzzle_path, 'r') as f:
    puzzle_input = f.read().strip().split('\n')

puz = np.array([list(i) for i in puzzle_input])
    
###########################################################
# puzzle_input = 'MMMSXXMASM MSAMXMSMSA AMXSXMAAMM MSAMASMSMX XMASAMXAMM XXAMMXXAMA SMSMSASXSS SAXAMASAAA MAMMMXMMMM MXMXAXMASX'
# puz = np.array([list(puzzle_input.split(' ')[i]) for i in range(len(puzzle_input.split(' ')))])

###########################################################
# Puzzle 1

def find_word(arr, word_oi):
    # Get locations of desired first letter
    starts = np.argwhere(arr == word_oi[0])
    word_count = 0
    
    for s in starts:
        r = s[0]
        c = s[1]
        
        # Define windows to check
        check_these = []
        for i in range(-1,len(word_oi)-2):
            if i == 0:
                for j in [-1,1]:
                    check_these += [[(r, c+(adv * j)) for adv in range(len(word_oi))]]
            else:
                for j in range(-1,len(word_oi)-2):
                    check_these += [[(r+(adv * i), c+(adv * j)) for adv in range(len(word_oi))]]
        # Check for XMAS if window allows           
        for chk in check_these:
            if max([chk[i][0] for i in range(len(chk))]) < puz.shape[0] and min([chk[i][0] for i in range(len(chk))]) >= 0:
                if max([chk[i][1] for i in range(len(chk))]) < puz.shape[1] and min([chk[i][1] for i in range(len(chk))]) >= 0:
                    spells = ''.join([puz[i] for i in chk])
                    if spells ==  word_oi:
                        word_count += 1
            
    return(word_count)

find_word(puz, 'XMAS')  # 2685

###########################################################
# Puzzle 2
def find_word(arr, word_oi):
    # Get locations of desired first letter
    starts = np.argwhere(arr == word_oi[1])
    word_count = 0
    these = []
    
    for s in starts:
        r = s[0]
        c = s[1]
        
        # Define windows to check
        i = 1
        check_these = [[(r+(adv * i)-i, c+(adv * i)-i) for adv in range(len(word_oi))]]
        check_these += [[(r+(adv * -i)+i, c+(adv * i)-i) for adv in range(len(word_oi))]]
        # Check for XMAS if window allows     
        words = []
        for chk in check_these:
            if max([chk[i][0] for i in range(len(chk))]) < puz.shape[0] and min([chk[i][0] for i in range(len(chk))]) >= 0:
                if max([chk[i][1] for i in range(len(chk))]) < puz.shape[1] and min([chk[i][1] for i in range(len(chk))]) >= 0:
                    words += [''.join([puz[i] for i in chk])] 

        if len(words) == 2 and (words[0] == word_oi or words[0] == word_oi[::-1]) and (words[1] == word_oi or words[1] == word_oi[::-1]):
             word_count += 1   
             these += [[r,c]]
        
    return(word_count)

find_word(puz, 'MAS')  
