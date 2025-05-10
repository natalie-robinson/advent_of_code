import math
import re
from functools import reduce
# dat = "RL\n\nAAA = (BBB, CCC)\nBBB = (DDD, EEE)\nCCC = (ZZZ, GGG)\nDDD = (DDD, DDD)\nEEE = (EEE, EEE)\nGGG = (GGG, GGG)\nZZZ = (ZZZ, ZZZ)"
# dat = "LLR\n\nAAA = (BBB, BBB)\nBBB = (AAA, ZZZ)\nZZZ = (ZZZ, ZZZ)"
# dat = "LR\n\n11A = (11B, XXX)\n11B = (XXX, 11Z)\n11Z = (11B, XXX)\n22A = (22B, XXX)\n22B = (22C, 22C)\n22C = (22Z, 22Z)\n22Z = (22B, 22B)\nXXX = (XXX, XXX)"
f = open('/users/natalierobinson/Desktop/github/advent_of_code/2023/day8.txt', 'r')
dat = f.read()

instructions = dat.split("\n\n")[0]


# 1. How many steps to reach ZZZ?
nodesDict = {re.findall("[a-zA-Z]+",i)[0]: (re.findall("[a-zA-Z]+",i)[1],re.findall("[a-zA-Z]+",i)[2]) for i in dat.split("\n\n")[1].split("\n")}

k = "AAA" 
turn = 0
steps = 0
while k != "ZZZ":
    steps += 1
    k = nodesDict[k][0] if instructions[turn] == "L" else nodesDict[k][1]
    if turn < len(instructions)-1:
        turn += 1
    else:
        turn = 0

steps

# 2. Follow two paths simultaneously until both land on a sequence ending in Z
nodesDict = {re.findall("[a-zA-Z0-9]+",i)[0]: (re.findall("[a-zA-Z0-9]+",i)[1],re.findall("[a-zA-Z0-9]+",i)[2]) for i in dat.split("\n\n")[1].split("\n")}
# Loop through and find when first key has ending Z. Test other keys to see if they do too. If not, keep track
#  of where the loop was to aovid rerunning the loop repetitively

# Above is correct but never finishes. Puzzle was set up to be least common multiple problem: find first ending Z
# for each start node, then LCM for all nodes. LAME
starts = [k for k in nodesDict.keys() if k[-1] == "A"]
distToZ = []
for s in starts:
    # Initiate the node and step
    n = s
    steps = 0
    while n[-1] != "Z":
        turn = instructions[steps] if steps < len(instructions) else instructions[steps - (len(instructions) * math.floor(steps/len(instructions)))]
        n = nodesDict[n][0] if turn == "L" else nodesDict[n][1]
        steps += 1
    distToZ.append(steps)

reduce(math.lcm,distToZ)  # 10668805667831

# Brute force answer that should work, but never finishes
# starts = [[k,0] for k in nodesDict.keys() if k[-1] == "A"]
# steps = 0
# k = starts[0][0]  # Get the first key and remove it from the dictionary
# starts = starts[1:]
# keepGoing = True
# while keepGoing:
#     steps += 1
#     turn = instructions[steps-1] if steps < len(instructions)+1 else instructions[steps - (len(instructions) * math.floor(steps/len(instructions))) - 1]
#     k = nodesDict[k][0] if turn == "L" else nodesDict[k][1]
#     if k[-1] == "Z":
#         for s in range(len(starts)):
#             newKey = starts[s][0]
#             for i in range(starts[s][1],steps):
#                 turn = instructions[i] if i < len(instructions) else instructions[i - (len(instructions) * math.floor(i/len(instructions)))]
#                 newKey = nodesDict[newKey][0] if turn == "L" else nodesDict[newKey][1]
#             # Update the list with where we left off
#             starts[s] = [newKey, steps]
#             if newKey[-1] != "Z":
#                 break
#         if s == len(starts) - 1 and newKey[-1] == "Z":
#             keepGoing = False

