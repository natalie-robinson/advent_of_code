#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 16:21:50 2024
@author: natalierobinson
"""

###########################################################
day = 2

dir_path = '/users/natalierobinson/Desktop/github/advent_of_code/2024/'
puzzle_path = dir_path + 'day' + str(day) + '.txt'
    
with open(puzzle_path, 'r') as f:
    puzzle_input = f.read().strip().split('\n')
    
###########################################################

puzzle_input = ['7 6 4 2 1', '1 2 7 8 9', '9 7 6 2 1', '1 3 2 4 5',
                '8 6 4 4 1', '1 3 6 7 9']


###########################################################
def test_lvl(l):
    is_safe = 'fail'
    deltas = list(map(lambda x: int(l[x]) - int(l[x-1]), range(1,len(l))))
    if set(deltas) <= {1, 2, 3} or set(deltas) <= {-1, -2, -3}:
        is_safe = 'pass'
    
    return(is_safe)

###########################################################
# Puzzle 1
            
safe_lvls = []
for lvl in puzzle_input:
    l = lvl.split()
    is_safe = test_lvl(l)
    if is_safe == 'pass':
        safe_lvls += [lvl]

len(safe_lvls) # 411

###########################################################
# Puzzle 2

safe_lvls = []
for lvl in puzzle_input:
    l = lvl.split()
    # Test
    is_safe = test_lvl(l)
    if is_safe == 'pass':
        safe_lvls += [lvl]
    else:
        dirs = ['i' if int(l[i+1]) - int(l[i]) > 0 else 'd' if int(l[i+1]) - int(l[i]) < 0 else 's' for i in range(len(l)-1)]
        if 's' in dirs:
            remove = [x for x in range(len(dirs)) if dirs[x] == 's'][0]
            l = [l[i] for i in range(len(l)) if not i == remove]
            is_safe = test_lvl(l)
            if is_safe == 'pass':
                safe_lvls += [lvl]
        else:
            if 'i' in dirs and 'd' in dirs:
                problem_dir = 'i' if dirs.count('i') < dirs.count('d') else 'd'           
                remove = [x for x in range(len(dirs)) if dirs[x] == problem_dir][0]
                l = [l[i] for i in range(len(l)) if not i == remove+1]
                is_safe = test_lvl(l)
                if is_safe == 'pass':
                    safe_lvls += [lvl]
            else:
                remove = [i for i in range(len(l)-1) if int(l[i+1]) - int(l[i]) < -3 or int(l[i+1]) - int(l[i]) > 3][0]
                if remove == 0:
                    l = [l[i] for i in range(len(l)) if not i == remove]
                else:
                    l = [l[i] for i in range(len(l)) if not i == remove+1]    
                is_safe = test_lvl(l)
                if is_safe == 'pass':
                    safe_lvls += [lvl]

len(safe_lvls) # 455 is off by 10 (answer is 465)

########################################################
# Stolen from subreddit after not being able to get the correct answer for puzzle 2

def is_safe(row):
    inc = [row[i + 1] - row[i] for i in range(len(row) - 1)]
    if set(inc) <= {1, 2, 3} or set(inc) <= {-1, -2, -3}:
        return True
    return False

data = [[int(y) for y in x.split(' ')] for x in puzzle_input]

safe_count = sum([is_safe(row) for row in data])
print(safe_count)

safe_count = sum([any([is_safe(row[:i] + row[i + 1:]) for i in range(len(row))]) for row in data])
print(safe_count)


