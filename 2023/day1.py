# Fix the calibration document
import re
f = open('/users/natalierobinson/Desktop/github/advent_of_code/2023/day1.txt', 'r')
dat = f.read()
dat = dat.split("\n")

def sumDigits(dat):
    total = 0
    for d in dat:
        digits = [i for i in d if i.isdigit()]
        if len(digits) > 1:
            num = int(digits[0] + digits[-1])
        else:
            num = int(digits[0] * 2)
        print(num)
        total += num
    return(total)


# 1) For each line, combine the first and last digits. Then add
summed = sumDigits(dat)

# 2) Do the same, but now with some of the numbers spelled
strNums = ["one","two","three","four","five","six","seven","eight","nine"]
conversionDict = {}
for i in range(9):
    conversionDict[strNums[i]] = str(i+1)

# Loop through dict keys and values if one is found, store the position of it's starting index. Get first and last values for each elem
total = 0
for d in dat:
    firstInd = len(d)
    firstNum = None
    lastInd = -1
    lastNum = None
    for k in conversionDict.keys():
        numLocs = [subStr.start() for subStr in re.finditer(k, d)] + [subStr.start() for subStr in re.finditer(conversionDict[k], d)]
        if len(numLocs) > 0:
            if min(numLocs) < firstInd:
                firstInd = min(numLocs)
                firstNum = conversionDict[k]
            if max(numLocs) > lastInd:
                lastInd = max(numLocs)
                lastNum = conversionDict[k]
    num = int("".join([firstNum, lastNum]))
    total += num
    
total
