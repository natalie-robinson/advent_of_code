f = open('/users/natalierobinson/Desktop/github/advent_of_code/2022/input6.txt', 'r')
code = f.read()

# code = 'bvwbjplbgvbhsrlpgdmjqwftvncz'

# Part 1 - find the index of the character after a starting sequence of 4 unique characters has been hit
st = 0
while st < (len(code)-4):
    chunk = code[st:(st+4)]
    if len(set(chunk)) == 4:
        print(st+4)
        break
    st +=1


# Part 2 - find the number of characters preceding a message marker, sequence of 14 unique characters
st = 0
while st < (len(code)-14):
    chunk = code[st:(st+14)]
    if len(set(chunk)) == 14:
        print(st+14)
        break
    st +=1