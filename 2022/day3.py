f = open('/users/natalierobinson/Desktop/github/advent_of_code/2022/input3.txt', 'r')
dat = f.read()

rucksacks = dat.split('\n')

rucksacks = ['vJrwpWtwJgWrhcsFMMfFFhFp', 'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL', 'PmmdzqPrVvPwwTWBwg', 'wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn', 'ttgJtRGJQctTZtZT', 'CrZsJsPPZsGzwwsLwLmpwMDw']

# chr(97) = a; chr(122) = z; chr(65) = 'A'; chr(90) = 'Z'
# lowercase offset = (97 - 1)  # Adjust for 0 indexing
# uppercase offset = (65 - 1) + 26


# Part 1 - sum priorities of shared items in rucksacks
total_priority = 0
for r in rucksacks:
    first_half = r[:int(len(r)/2)]
    second_half = r[int(len(r)/2):]
    shared_item = [i for i in first_half if i in second_half]
    for s in shared_item:
        if s.isupper():
            priority = ord(s) - (65 - 1) + 26
        else:
            priority = ord(s) - (97 - 1)
    total_priority += priority

# Part 2 - find groupd of 3 packs with shared items, calculate total value of shared items
total_priority = 0
for r in range(0,len(rucksacks),3):
    shared_first = list(set([i for i in rucksacks[r] if i in rucksacks[(r+1)]]))
    shared_second = list(set([i for i in shared_first if i in rucksacks[(r+2)]]))
    shared_item = [i for i in shared_first if i in shared_second]
    for s in shared_item:
        if s.isupper():
            priority = ord(s) - (65 - 1) + 26
        else:
            priority = ord(s) - (97 - 1)
    total_priority += priority
    
    
