import collections
import copy
import re
# dat = "32T3K 765\nT55J5 684\nKK677 28\nKTJJT 220\nQQQJA 483"
f = open('/users/natalierobinson/Desktop/github/advent_of_code/2023/day7.txt', 'r')
dat = f.read()
hands = dat.split("\n")

def sortHands(inputDict, cardRanks, finalList):
    ''' Iterate through cards in hands, checking for highest value card by card'''
    k = 0      
    while k < len(inputDict.keys()):
        hands = inputDict[list(cardRanks.keys())[k]]
        while len(hands) > 0:
            card = 1  # Initiate the card to check
            # Get ranks of hands by 2nd card (first cards are all identical for key)
            temp = [cardRanks[h[card]] for h in hands]
            topHands = [hands[h] for h in range(len(temp)) if temp[h] == min(temp)]
            if len(topHands) == 1:
                finalList += topHands
                hands = [h for h in hands if h not in topHands]
            else:
                while len(list(set(temp))) != len(temp):
                    card += 1
                    temp = [cardRanks[th[card]] for th in topHands]
                    stash = [x for _, x in sorted(zip(temp, topHands))]
                    topHands = [topHands[h] for h in range(len(temp)) if temp[h] == min(temp)]
                finalList += stash
                hands = [h for h in hands if h not in stash]
        k += 1
    return(finalList)


# 1. Multiply each hand's bid by its rank (out of the 5 hands) and sum
cardVals = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
cardDict = {i: [] for i in cardVals}

# Sort the hands into dictionaries by hand "type"
fiveOfAKind = copy.deepcopy(cardDict)
fourOfAKind = copy.deepcopy(cardDict)
fullHouse = copy.deepcopy(cardDict)
threeOfAKind = copy.deepcopy(cardDict)
twoPair = copy.deepcopy(cardDict)
onePair = copy.deepcopy(cardDict)
highCard = copy.deepcopy(cardDict)

for h in hands:
    cards = h.split(" ")[0]
    if len(set(cards)) == 1:
        fiveOfAKind[cards[0]].append(cards)
    elif len(set(cards)) == 2:
        if (sorted(cards)[0] != sorted(cards)[1]) or (sorted(cards)[3] != sorted(cards)[4]):
            fourOfAKind[cards[0]].append(cards)
        else:
            fullHouse[cards[0]].append(cards)
    elif len(set(cards)) == 3:
        if len(re.findall(cards[0],cards)) == 3 or len(re.findall(cards[1],cards)) == 3 or len(re.findall(cards[2],cards)) == 3:
            threeOfAKind[cards[0]].append(cards)
        else:
            twoPair[cards[0]].append(cards)
    elif len(set(cards)) == 4:
        onePair[cards[0]].append(cards)
    else:
        highCard[cards[0]].append(cards)

# Fully process cards in each dictionary
cardRanks = {cardVals[i]: i for i in range(len(cardVals))}
        
# Calculate final scores
final = []
final = sortHands(fiveOfAKind, cardRanks, final)
final = sortHands(fourOfAKind, cardRanks, final)
final = sortHands(fullHouse, cardRanks, final)
final = sortHands(threeOfAKind, cardRanks, final)
final = sortHands(twoPair, cardRanks, final)
final = sortHands(onePair, cardRanks, final)
final = sortHands(highCard, cardRanks, final)

# Reverse the list and multiply the ranks by the bids
total = sum([(len(final) - i) * int(dat.split(final[i] + " ")[1].split("\n")[0]) for i in range(len(final))])
total


# 2. J == Joker, and assumes value that will make the hand strongest. It is the weakest card during scoring, though
cardVals = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]
cardDict = {i: [] for i in cardVals}

# Sort the hands into dictionaries by hand "type"
fiveOfAKind = copy.deepcopy(cardDict)
fourOfAKind = copy.deepcopy(cardDict)
fullHouse = copy.deepcopy(cardDict)
threeOfAKind = copy.deepcopy(cardDict)
twoPair = copy.deepcopy(cardDict)
onePair = copy.deepcopy(cardDict)
highCard = copy.deepcopy(cardDict)

for h in hands:
    cards = h.split(" ")[0]
    if len(set(cards)) == 1 or ("J" in cards and len(set(cards)) == 2):
        fiveOfAKind[cards[0]].append(cards)
    else:
        if "J" not in cards:
            if len(set(cards)) == 2:
                if (sorted(cards)[0] != sorted(cards)[1]) or (sorted(cards)[3] != sorted(cards)[4]):
                    fourOfAKind[cards[0]].append(cards)
                else:
                    fullHouse[cards[0]].append(cards)
            elif len(set(cards)) == 3:
                if len(re.findall(cards[0],cards)) == 3 or len(re.findall(cards[1],cards)) == 3 or len(re.findall(cards[2],cards)) == 3:
                    threeOfAKind[cards[0]].append(cards)
                else:
                    twoPair[cards[0]].append(cards)
            elif len(set(cards)) == 4:
                onePair[cards[0]].append(cards)
            else:
                highCard[cards[0]].append(cards)
        else:
            if len(set(cards)) == 3:
                if collections.Counter(cards).most_common(1)[0][1] == 3 or len(re.findall("J",cards)) == 2:
                    fourOfAKind[cards[0]].append(cards)
                else:
                    fullHouse[cards[0]].append(cards)
            elif len(set(cards)) == 4:
                threeOfAKind[cards[0]].append(cards)
            else:
                onePair[cards[0]].append(cards)
        
# Fully process cards in each dictionary 
cardRanks = {cardVals[i]: i for i in range(len(cardVals))}
        
# Calculate final scores
final = []
final = sortHands(fiveOfAKind, cardRanks, final)
final = sortHands(fourOfAKind, cardRanks, final)
final = sortHands(fullHouse, cardRanks, final)
final = sortHands(threeOfAKind, cardRanks, final)
final = sortHands(twoPair, cardRanks, final)
final = sortHands(onePair, cardRanks, final)
final = sortHands(highCard, cardRanks, final)

# Reverse the list and multiply the ranks by the bids
total = sum([(len(final) - i) * int(dat.split(final[i] + " ")[1].split("\n")[0]) for i in range(len(final))])
total
         


# Part b = 249781879
