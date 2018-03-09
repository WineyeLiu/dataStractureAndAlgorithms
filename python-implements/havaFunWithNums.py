"""
@author liuwenai

Notice that the number 123456789 is a 9-digit number consisting exactly the numbers from 1 to 9, 
with no duplication. Double it we will obtain 246913578, which happens to be another 9-digit number 
consisting exactly the numbers from 1 to 9, only in a different permutation. 
Check to see the result if we double it again!

Now you are suppose to check if there are more numbers with this property. 
That is, double a given number with k digits, you are to tell if the resulting 
number consists of only a permutation of the digits in the original number.
"""

def num2DigitList(num):
    snum = str(num)
    l = []
    for s in snum:
        l.append(s)
    return l

def isPermutativeSame(num1, num2):
    l1 = num2DigitList(num1)
    l2 = num2DigitList(num2)

    if len(l1) != len(l2):
        return False
    else:
        flag = True
        l1.sort()
        l2.sort()
        i = 0
        while i < len(l1):
            if(l1[i] != l2[i]):
                flag = False
                break
            i += 1
        return flag

def main():
    inum = int(input().split(' ')[0])
    if isPermutativeSame(inum, inum*2):
        print('Yes')
    else:
        print('No')
    print(inum*2, end="")

if __name__ == '__main__':
    main() 

