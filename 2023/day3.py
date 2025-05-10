import re
f = open('/users/natalierobinson/Desktop/github/advent_of_code/2023/day3.txt', 'r')
dat = f.read()
dat = dat.split("\n")


# 1) Sum of all numbers that are adjacent (including diagonal) to a symbol
# For each line, create a dictionary of the locations and values of the numbers
numDict = {}
for d in range(len(dat)):
    numDict[d] = [(m.start(0),m.end(0)-1,int(m.group(0))) for m in re.finditer("\d+", dat[d])]
    
rowSums = []
for k in numDict.keys():
    rowSum = 0 
    if len(numDict[k]) > 0:
        for elem in numDict[k]:
            # Determine index range to check for symbols
            isFirstCol = True if elem[0] == 0 else False
            isLastCol = True if elem[1] == len(dat[k]) - 1 else False
            isTopRow = True if k == 0 else False
            isBottomRow = True if k == len(numDict) - 1 else False
            if isFirstCol:
                indStart = elem[0]
            else:
                indStart = elem[0] - 1
            if isLastCol:     
                indEnd = elem[1]
            else: 
                indEnd = elem[1] + 2
            if isTopRow:
                rowStart = k
            else:
                rowStart = k - 1
            if isBottomRow:
                rowEnd = k
            else:
                rowEnd = k+1
            # Get symbols in window around number and if any are special characters then add to row sum
            if isTopRow or isBottomRow:
                checkForSymbols = dat[rowStart][indStart:indEnd] + dat[rowEnd][indStart:indEnd]
            else:
                checkForSymbols = dat[rowStart][indStart:indEnd] + dat[k][indStart:indEnd] + dat[rowEnd][indStart:indEnd]
            if any((not y.isdigit() and y != ".") for y in checkForSymbols):
                rowSum += elem[2]
    rowSums += [rowSum]
           
sum(rowSums)     # 546312
                
 
# 2) Multiply the numbers near a gear (two numbers adjacent to *)
## I give up - cannot see why the below code fails
    
pattern = ['\d+', '\-\d+']
regex = re.compile(r'(' + '|'.join(pattern) + ')')
numDict = {}
for d in range(len(dat)):
    numDict[d] = [(m.start(0),m.end(0)-1,int(m.group(0))) for m in regex.finditer(dat[d])]

out = []
for d in range(len(dat)):
    isTopRow = True if d == 0 else False
    isBottomRow = True if d == len(dat) - 1 else False
    if isTopRow:
        rowRange = range(0,d+2)
    elif isBottomRow:
        rowRange = range(d-1,d+1)
    else:
        rowRange = range(d-1,d+2)
    for i in range(len(dat[d])):
        qualifyingNums = []
        if dat[d][i] == "*":
            isFirstCol = True if i == 0 else False
            isLastCol = True if i == (len(dat[d])-1) else False
            if isFirstCol:
                checkThese = [0,i+1]
            elif isLastCol:
                checkThese = [i-1,i]
            else:
                checkThese = [i-1,i,i+1]
            for r in rowRange:
                if len(numDict[r]) > 0:
                    for e in numDict[r]:
                        if checkThese[0] in range(e[0],e[1]+1):
                            qualifyingNums.append(e[2])
                        elif checkThese[-1] in range(e[0],e[1]):
                            qualifyingNums.append(e[2])
                        else:
                            if len(checkThese) == 3 and checkThese[1] in range(e[0],e[1]+1):
                                qualifyingNums.append(e[2])
        if len(qualifyingNums) == 2:
            mult = qualifyingNums[0] * qualifyingNums[1]
            out.append([d, i, qualifyingNums, mult])
    

# sum(out)   # 5653838; 87014456 are too low. 80702188; 87441793 are wrong (not sure how)
sum([i[3] for i in out])  
            
    