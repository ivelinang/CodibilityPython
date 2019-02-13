__author__ = 'Ivelin'

def solution(A, K):
    if len(A) == 0:
        return A

    return A[len(A)-(K%len(A)):] + A[:len(A)-(K%len(A))]

def Main():
    a=[3, 8, 9, 7, 6]
    print (solution(a,3))
    print(7%5)

'Run the Main function if the module is open(vs. imported)'
if __name__ == "__main__":
    Main()
