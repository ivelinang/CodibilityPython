__author__ = 'Ivelin'

def solution(A):
    sum_two=sum(A)
    min_diff=None
    sum_one=0
    for i in range(1, len(A)):
        sum_one+=A[i-1]
        sum_two-=A[i-1]
        diff=abs(sum_one-sum_two)

        if min_diff==None:
            min_diff=diff
        else:
            min_diff=min(min_diff,diff)
    return min_diff

def Main():
    pass

'Run the Main function if the module is open(vs. imported)'
if __name__ == "__main__":
    Main()
