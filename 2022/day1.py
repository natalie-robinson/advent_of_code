# Which elf has the most calories in it's pack

f = open('/users/natalierobinson/Desktop/github/advent_of_code/2022/input_1a.txt', 'r')
dat = f.read()

# 1 - find the hightest number of calories being carried by an elf
highestCals = 0
for elf in range(len(dat.split('\n\n'))):
    calories = sum([int(i) for i in dat.split('\n\n')[elf].split('\n') if i != ''])
    if calories > highestCals:
        highestCals = calories


# 2 - find the top three calorie carriers and sum theiry total calories

highestCals = []
for elf in range(len(dat.split('\n\n'))):
    calories = sum([int(i) for i in dat.split('\n\n')[elf].split('\n') if i != ''])
    highestCals.append(calories)
        
highestCals.sort()
sum(highestCals[-3:])
