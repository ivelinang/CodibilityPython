__author__ = 'Ivelin'

def divideBy2(decNumber):
    remstack = []

    while decNumber > 0:
        rem = decNumber % 2
        remstack.append(rem)
        decNumber = decNumber // 2

    binString = []
    while remstack:
        binString.append(remstack.pop())

    return binString

def findBinaryGap(n):
    binary=divideBy2(n)
    nmax=0
    ntemp=0
    for num in binary:
        if num==0:
            ntemp+=1
        else:
            if ntemp>nmax:
                nmax=ntemp
            ntemp=0

    return nmax


def Main():
    print (divideBy2(529))
    print (findBinaryGap(20))

'Run the Main function if the module is open(vs. imported)'
if __name__ == "__main__":
    Main()