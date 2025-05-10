f = open('/users/natalierobinson/Desktop/github/advent_of_code/2022/input5.txt', 'r')
dat = f.read()

stacks =  {key: [] for key in ['s' + str(i) for i in range(1,10)]}

for i in range(7, -1, -1):
      crate = dat.split('\n')[i].replace(' ','-').replace('---','[-]')
      crate = [crate[j] for j in range(1,len(crate),4)]

      for c in range(0,len(crate)):
          if crate[c] not in ['-','[',']']:
              stacks['s' + str(c + 1)].append(crate[c])

numMoved = []
moveFrom = []
moveTo = []

for i in range(10,len(dat.split('\n'))):
    digits = [int(myStr) for myStr in dat.split('\n')[i].split() if myStr.isdigit()]
    numMoved.append(digits[0])
    moveFrom.append(digits[1])
    moveTo.append(digits[2])
    

# stacks = {
#     's1': ['Z', 'N'],
#     's2': ['M', 'C', 'D'],
#     's3': ['P']
#     }

# numMoved = [1, 3, 2, 1]
# moveFrom = [2, 1 ,2, 1]
# moveTo = [1, 3, 1, 2]

# Part 1 - find top crate in each stack
for n in range(len(numMoved)):
    miniStack = stacks['s' + str(moveFrom[n])][-numMoved[n]:]
    miniStack.reverse()
    stacks['s' + str(moveFrom[n])] = stacks['s' + str(moveFrom[n])][:(len(stacks['s' + str(moveFrom[n])]) - numMoved[n])]
    stacks['s' + str(moveTo[n])] = stacks['s' + str(moveTo[n])] + miniStack

print(''.join([stacks[k][-1] for k in stacks.keys()]))
    
    
# Part 2 - as in part 1, but crates are not reordered
for n in range(len(numMoved)):
    miniStack = stacks['s' + str(moveFrom[n])][-numMoved[n]:]
    stacks['s' + str(moveFrom[n])] = stacks['s' + str(moveFrom[n])][:(len(stacks['s' + str(moveFrom[n])]) - numMoved[n])]
    stacks['s' + str(moveTo[n])] = stacks['s' + str(moveTo[n])] + miniStack

print(''.join([stacks[k][-1] for k in stacks.keys()]))