import math

'''
素数猜想 算法
'''

def getPrimeNumsList(maxNum):
    pnl = []
    n = 1
    while n <= maxNum:
        divider = 2
        isPrime = True
        while divider <= math.sqrt(n):
            if n % divider == 0:
                isPrime = False
                break
            divider += 1
        
        if isPrime:
            pnl.append(n)
        n += 1
    return pnl

def getCoupleNums(l):
    res = 0
    i = 0
    while i < len(l)-1:
        if l.index(l[i]+2):
            res += 1
        i += 1
    return res


def main():
    N = input().split(' ')[0]
    l = getPrimeNumsList(int(N))
    print(l)
    # print(getCoupleNums(l), end="")

if __name__ == '__main__':
    main()
            
