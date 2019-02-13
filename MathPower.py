__author__ = 'Ivelin'

def looppower(x,a):
    if a==1:
        return x
    else:
        return x*looppower(x,a-1)

def Main():
    pass

'Run the Main function if the module is open(vs. imported)'
if __name__ == "__main__":
    Main()