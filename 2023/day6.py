import re
# dat = "Time:      7  15   30\nDistance:  9  40  200"
f = open('/users/natalierobinson/Desktop/github/advent_of_code/2023/day6.txt', 'r')
dat = f.read()

times = re.findall("\d+",dat.split("\n")[0])
distances = re.findall("\d+",dat.split("\n")[1])

# 1. Find the number of ways the previous distance record can be broken
waysToBeatRecord = []
product = 1
for r in range(len(times)):
    distToBeat = int(distances[r])
    iWin = 0
    for t in range(1,int(times[r])):
        newDist = (int(times[r]) - t) * t
        if newDist > distToBeat:
            iWin += 1
    # Add to record keeping
    waysToBeatRecord.append(iWin)
    product *= iWin
            
product     # 128700
        
# 2. Remove the spaces in each line and figure out how many ways there are to beat the record
def findRngLimit(x, distToBeat, holdTime, totTime, direction, outList):
    multiplier = 0.5 if direction == "down" else 1.5
    incrementer = 1 if direction == "down" else -1
    # Change by halves
    while x > distToBeat:
        holdTime = round(multiplier * holdTime)
        x = holdTime * (totTime - holdTime)
    # Fine tune
    while x < distToBeat:
        holdTime += incrementer
        x = holdTime * (totTime - holdTime)
    outList.append(holdTime if direction == "down" else holdTime+1)
    return(outList)

# Parse data
totTime = int(re.sub(" +", "", dat.split("\n")[0].split(":")[1]))
distToBeat = int(re.sub(" +", "", dat.split("\n")[1].split(":")[1]))

# Initiate hold time at 1/2 range and calc distance traveled
holdTime = round(0.5 * totTime)
x = holdTime * (totTime - holdTime)

# Calculate range within which distance traveled is greater than distance to beat
rng = findRngLimit(x, distToBeat, holdTime, totTime, direction="down", outList=[])
rng = findRngLimit(x, distToBeat, holdTime, totTime, direction="up", outList=rng)

waysToWin = rng[1]-rng[0]
waysToWin
