# dat = "0 3 6 9 12 15\n1 3 6 10 15 21\n10 13 16 21 30 45"
f = open('/users/natalierobinson/Desktop/github/advent_of_code/2023/day9.txt', 'r')
dat = f.read()
sequs = dat.split("\n")

def findSeq(sequs, rev = False):
    allSummed = 0
    for s in sequs:
        # Initiate
        s = s.split(" ")
        updateList = []
        # Evaluate
        idx = 0 if rev else -1
        while len(set(s)) != 1:
            updateList.append(int(s[idx]))
            diffs = [int(s[(i+1)]) - int(s[i]) for i in range(len(s)) if i < len(s)-1]
            s = diffs
        # Sum
        addThis = diffs[-1]
        for ln in list(range(len(updateList)-1,-1,-1)):
            newNum = updateList[ln] - addThis if rev else updateList[ln] + addThis
            addThis = newNum
        allSummed += newNum
    return(allSummed)


# Part 1 - get the next number in the sequence        
answer = findSeq(sequs) # 1974913025

# Part 2 - get the first number from each sequence
answer = findSeq(sequs, rev=True)  # 884
    