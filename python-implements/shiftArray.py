"""平移数组算法
"""

"""
交换数组list中下标为idx1和idx2两个元素的位置
"""
def swap(l, idx1, idx2):
    tmp = l[idx1]
    l[idx1] = l[idx2]
    l[idx2] = tmp
    tmp = None

def floatUp(l, startIdx, endIdx):
    idx = startIdx
    while idx < endIdx:
        swap(l, idx, idx+1)
        idx += 1

def sinkDown(l, startIdx, endIdx):
    idx = endIdx
    while idx > startIdx:
        swap(l, idx, idx-1)
        idx -= 1

def shift(l, offset, startIdx, endIdx):
    if offset == len(l)-1:
        floatUp(l, startIdx, endIdx)
    elif offset == 1:
        sinkDown(l, startIdx, endIdx)
    else:
        halfSize = (endIdx - startIdx + 1)/2
        if offset < halfSize :
            # 如果右移的位数n小于需要位移数组大小的一半，则交换前n个元素和后n个元素的位置后，前n个已经排列好
            # 后len-2n 和 n 需要再交换
            i = 0
            while i < offset:
                swap(l, startIdx + i, endIdx - offset + 1 + i)
                i += 1
                
            shift(l, offset, startIdx + offset, endIdx)
        elif offset == halfSize:
            i = 0
            while i < offset:
                swap(l, startIdx + i, endIdx - offset + 1 + i)
                i += 1
        else:
            # 如果右移的位数n大于于需要位移数组大小的一半，则交换 len(数组)-n 个...， 后n个已经排好...
            # 前n个和中间len - 2n个要再交换
            i = 0
            while i < endIdx - startIdx + 1 -offset:
                swap(l, startIdx + i, endIdx - (endIdx - startIdx + 1 -offset) + 1 + i)
                i += 1
            shift(l, (endIdx - startIdx + 1) - 2*((endIdx - startIdx + 1)-offset), startIdx, endIdx - (endIdx - startIdx + 1 - offset))

def listRightShift(l, offset):
    if offset < len(l):
        shift(l, offset, 0, len(l) - 1)
    else: 
        if offset%len(l) == 0:
            None
        else:
            offset = offset%len(l)
            shift(l, offset, 0, len(l) - 1)
    
      

def main():

    #l = [1, 2, 3, 4]
    #l = [1, 2, 3, 4, 5, 6, 7]
    ipt = input()
    iptList = ipt.split(' ')
    lSize = iptList[0]
    offset = int(iptList[1])

    lStr = input()
    lArr = lStr.split(' ')
    l = []
    for i in lArr:
        l.append(int(i))

    listRightShift(l, offset)
    
    
    print(*l, sep=" ", end="")
    

if __name__ == '__main__':
    main()
    