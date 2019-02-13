__author__ = 'Ivelin'

def solution(nList):
    sortList=sorted(nList)
    print (sortList)
    cnter=0
    for i in range(len(sortList)-1):
        if sortList[i]!=sortList[i+1]:
            if cnter==0:
                return sortList[i]
            else:
                cnter=0
        else:
            cnter=1
    #return false

def solution2(nList):
    myDict={}
    for num in nList:
        myDict[num]=myDict.get(num,0)+1
    for key, value in myDict.items():
        if value==1:
            return key

def solution3(A):
    i=0
    for x in A:
        i=i^x
    return i

def solution4(A):
    iSet=set()
    for num in A:
        if num not in iSet:
            iSet.add(num)
        else:
            iSet.remove(num)
    return iSet.pop()


def Main():
    v= [9, 3, 9, 3, 9, 7, 9]
    print(solution( v))
    print(solution2( v))
    print(solution3(v))
    print(solution4(v))


'Run the Main function if the module is open(vs. imported)'
if __name__ == "__main__":
    Main()
