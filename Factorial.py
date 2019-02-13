__author__ = 'Ivelin'

def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)


def Main():
    pass

'Run the Main function if the module is open(vs. imported)'
if __name__ == "__main__":
    Main()