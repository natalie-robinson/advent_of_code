import re
f = open('/users/natalierobinson/Desktop/github/advent_of_code/2023/day4.txt', 'r')
dat = f.read()
dat = dat.split("\n")


# 1. For each card, find the #'s on the left of the | that match those on the right. 
# The first match is worth 1, each subsequent doubles the score. Sum all points
pattern = ['\d+', '\-\d+']
regex = re.compile(r'(' + '|'.join(pattern) + ')')

allCards = []
allPoints = 0
for d in dat:
    matches = []
    points = []
    winningNums = [m.group(0) for m in regex.finditer(d.split(" | ")[0].split(": ")[1])]
    yourNums = [m.group(0) for m in regex.finditer(d.split(" | ")[1])]
    matches = [n for n in yourNums if n in winningNums]
    if len(matches) > 0:
        for m in range(len(matches)):
            points.append(1 if m == 0 else 2*points[-1]) 
        allCards.append(matches)
        allPoints += points[-1]

# 2. Each winning number gives you an additional copy of the nth subsequent card. How many cards are there in the end
cardDict={}
for i in range(len(dat)):
    # Initiate card counts with self
    cardDict["Card " + str(i+1)] = 1
    
for d in range(len(dat)):
    # Process matches
    matches = []
    points = []
    winningNums = [m.group(0) for m in regex.finditer(dat[d].split(" | ")[0].split(": ")[1])]
    yourNums = [m.group(0) for m in regex.finditer(dat[d].split(" | ")[1])]
    matches = [n for n in yourNums if n in winningNums]
    if len(matches) > 0:
        for m in range(len(matches)):
            if d+m+2 < len(dat)+1:
                cardDict["Card " + str(d+m+2)] += cardDict["Card " + str(d+1)]
        
sum(cardDict.values()) # 8054116 is too low
