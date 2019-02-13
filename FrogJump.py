__author__ = 'Ivelin'

def solution(X, Y, D):
    z=(Y-X)//D
    if (Y-X)%D!=0:
        return z+1
    else:
        return z

def Main():
    print(solution(10,85,30))

'Run the Main function if the module is open(vs. imported)'
if __name__ == "__main__":
    Main()
