__author__ = 'Ivelin'

def solution(A):
    n=len(A)
    sumN=sum(x for x in range(n+2))
    return sumN-sum(A)


def Main():
    v=[1,2,3,5]
    print(solution(v))

'Run the Main function if the module is open(vs. imported)'
if __name__ == "__main__":
    Main()
