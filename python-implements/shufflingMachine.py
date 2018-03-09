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


def main():
    l = getNewPokerSuit()
    print(l)

if __name__ == '__main__':
    main()