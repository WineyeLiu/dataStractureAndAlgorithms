'''
打印沙漏算法
'''
def sandgalssSizeGen(arg1):
    size = 1
    halfH = 1
    while size + ((halfH+1)*2 -1)*2 < arg1:
        size += ((halfH+1)*2 -1)*2
        halfH += 1
    return (size, arg1 - size, halfH)

def printBp(bNums, pNums, pattern):
    for i in range(bNums):
        print(' ', end='')
    for i in range(pNums):
        if(i == pNums-1):
            print(pattern)
        else:
            print(pattern, end='')


def printSandGlass(halfH, pattern):
    cursor = halfH
    while cursor > 0:
        printBp(halfH-cursor, cursor*2 - 1, pattern)
        cursor -= 1

    if halfH > 1:
        cursor = 2
        while cursor <= halfH:
            printBp(halfH-cursor, cursor*2 - 1, pattern)
            cursor += 1


def main():
    ipt = input()
    size = int(ipt.split(" ")[0])
    pattern = ipt.split(" ")[1]

    t = sandgalssSizeGen(size)
    printSandGlass(t[2], pattern)
    print(t[1], end="")

if __name__ == '__main__':
    main()
