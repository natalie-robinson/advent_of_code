f = open('/users/natalierobinson/Desktop/github/advent_of_code/2022/input2.txt', 'r')
dat = f.read()

player1 = [dat[x] for x in range(0,len(dat),4)]
player2 = [dat[x] for x in range(2,len(dat),4)]

options = {'rock': ['A','X',1],
           'paper': ['B','Y',2],
           'scissors': ['C','Z',3]}
outcome = {'lost': 0,
           'draw': 3,
           'won': 6}

# Part 1 - total score
total_score = 0
for r in range(len(player1)):
    player_1_score = [options[k][2] for k in options.keys() if player1[r] in options[k]][0]
    player_2_score = [options[k][2] for k in options.keys() if player2[r] in options[k]][0]
    diff = player_2_score - player_1_score
    if diff in [1, -2]:
        total_score += player_2_score + outcome['won']
    elif diff in [-1, 2]:
        total_score += player_2_score + outcome['lost']
    else:
        total_score += player_2_score + outcome['draw']

print(total_score)

# Part 2 - 
# player1 = ['A', 'B', 'C'] 
# player2 = ['Y', 'X', 'Z']

options = {'rock': ['A',1],
           'paper': ['B',2],
           'scissors': ['C',3]}
outcome = {'lost': ['X',0],
           'draw': ['Y',3],
           'won': ['Z',6]}

total_score = 0
for r in range(len(player1)):
    player_1_score = [options[k][1] for k in options.keys() if player1[r] in options[k]][0]
    if player2[r] in outcome['draw']:
        player_2_choice = player1[r]
    elif player2[r] in outcome['won']:
        player_2_choice = 'B' if player1[r] == 'A' else 'C' if player1[r] == 'B' else 'A'
    else:
        player_2_choice = 'A' if player1[r] == 'B' else 'B' if player1[r] == 'C' else 'C'
    player_2_score = [options[k][1] for k in options.keys() if player_2_choice in options[k]][0]
    diff = player_2_score - player_1_score
    if diff in [1, -2]:
        total_score += player_2_score + outcome['won'][1]
    elif diff in [-1, 2]:
        total_score += player_2_score + outcome['lost'][1]
    else:
        total_score += player_2_score + outcome['draw'][1]
    
print(total_score)