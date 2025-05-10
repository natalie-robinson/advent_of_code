import re
f = open('/users/natalierobinson/Desktop/github/advent_of_code/2023/day2.txt', 'r')
dat = f.read()
dat = dat.split("\n")

# 1) Sum of the game numbers that would be possible if there were x dice of each color available in the bag 
# Dice in bag
red = 12
green = 13
blue = 14

gameNumsSummed = 0
for d in dat:
    gameNum = int(d.split("Game ")[1].split(":")[0])
    r = [0]; g = [0]; b = [0]
    if "red" in d:
        r = [int(i) for i in re.findall(r" (\d+) red", d)]
    if "green" in d:
        g = [int(i) for i in re.findall(r" (\d+) green", d)]
    if "blue" in d:
        b = [int(i) for i in re.findall(r" (\d+) blue", d)]
    if not any(e > red for e in r) and not any(e > green for e in g) and not any(e > blue for e in b):
        gameNumsSummed += gameNum
        
# 2) What is the summed of the product of the fewest number of cubes of each color 
#     that could have been in the bag to make each game possible?
productsSummed = 0
for d in dat:
    r = 0; g = 0; b = 0
    if "red" in d:
        r = max([int(i) for i in re.findall(r" (\d+) red", d)])
    if "green" in d:
        g = max([int(i) for i in re.findall(r" (\d+) green", d)])
    if "blue" in d:
        b = max([int(i) for i in re.findall(r" (\d+) blue", d)])
    # Final list in order red, green, blue
    finalDice = [r,g,b]
    product = 1
    for num in finalDice:
        if num > 0:
            product *= num
    productsSummed += product
    
