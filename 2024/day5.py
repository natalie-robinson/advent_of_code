#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 12:12:04 2024
@author: natalierobinson
"""
###########################################################
day = 5
import functools

dir_path = '/users/natalierobinson/Desktop/github/advent_of_code/2024/'
puzzle_path = dir_path + 'day' + str(day) + '.txt'
    
with open(puzzle_path, 'r') as f:
    orders, updates = f.read().strip().split('\n\n')

orders = [tuple(line.split('|')) for line in orders.split()]
updates = (i.split(',') for i in updates.splitlines())

###########################################################
orders = '47|53 97|13 97|61 97|47 75|29 61|13 75|53 29|13 97|29 53|29 61|53 97|53 61|29 47|13 75|47 97|75 47|61 75|61 47|29 75|13 53|13'
orders = [tuple(line.split('|')) for line in orders.split()]

updates = '75,47,61,53,29 97,61,53,29,13 75,29,13 75,97,47,61,53 61,13,29 97,13,75,29,47'
updates = [i.split(',') for i in updates.split(' ')]

###########################################################
# Puzzle 1
def compare(a, b):
  return -1 if (a, b) in orders else 1 if (b, a) in orders else 0

total = 0
for u in updates:
  new = sorted(u, key=functools.cmp_to_key(compare))
  if (new == u):
    total += int(new[len(new) // 2])

total  # 6041


##########################################################
# Puzzle 2
total = 0
for u in updates:
  new = sorted(u, key=functools.cmp_to_key(compare))
  if (new != u): #  ^ True:
    total += int(new[len(new) // 2])

total  # 4884
