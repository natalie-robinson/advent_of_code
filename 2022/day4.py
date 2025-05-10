f = open('/users/natalierobinson/Desktop/github/advent_of_code/2022/input4.txt', 'r')
dat = f.read()
dat = dat.split('\n')

# dat = ['2-4,6-8', '2-3,4-5', '5-7,7-9', '2-8,3-7', '6-6,4-6', '2-6,4-8']

# Part 1 - find pairs where one range is entirely within the other
total_overlap = []
for d in dat:
    r1 = d.split(',')[0]
    r2 = d.split(',')[1]
    test1 = int(r1.split('-')[0]) >= int(r2.split('-')[0]) and int(r1.split('-')[1]) <= int(r2.split('-')[1])
    test2 = int(r2.split('-')[0]) >= int(r1.split('-')[0]) and int(r2.split('-')[1]) <= int(r1.split('-')[1])
    if test1 or test2:
        total_overlap.append(d)

# Part 2 - find pairs where the ranges overlap at all
overlap = []
for d in dat:
    r1 = d.split(',')[0]
    r2 = d.split(',')[1]
    test1 = int(r1.split('-')[0]) <= int(r2.split('-')[1]) and int(r1.split('-')[0]) >= int(r2.split('-')[0]) 
    test2 = int(r2.split('-')[0]) <= int(r1.split('-')[1]) and int(r2.split('-')[0]) >= int(r1.split('-')[0]) 
    if test1 or test2:
        overlap.append(d)