"""
@author liuwenai

Shuffling Machine
"""

def getNewPokerSuit():
    l = []
    for x in 'SHCD':
        i = 0
        while i < 13:
            l.append(x + str(i+1))
            i += 1
    l.append('J1')
    l.append('J2')
    return l

def shuffling(cardList, ruleList):
    l = [x for x in range(len(cardList))]
    i = 0
    for x in ruleList:
        l[x-1] = cardList[i]
        i += 1
    return l

def shufflingRepeat(cardList, ruleList, times):
    l = cardList
    i = times
    while i > 0:
        l = shuffling(l, ruleList)
        i -= 1
    return l

def main():
    # l = getNewPokerSuit()
    # print(l)
    #s ='36 52 37 38 3 39 40 53 54 41 11 12 13 42 43 44 2 4 23 24 25 26 27 6 7 8 48 49 50 51 9 10 14 15 16 5 17 18 19 1 20 21 22 28 29 30 31 32 33 34 35 45 46 47'
    times = int(input().split(' ')[0])
    s = input()
    ls = s.split(' ')
    rl = list(map(lambda x: int(x), ls))
    print(rl)
    cl = getNewPokerSuit()
    # rl = [4, 2, 5, 3, 1]
    l = shufflingRepeat(cl, rl, times)
    print(*l, sep=' ', end="")

if __name__ == '__main__':
    main()