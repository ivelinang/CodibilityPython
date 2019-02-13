__author__ = 'Ivelin'

def fibonacci(n):
    curr=1
    prev=1
    for i in range(n-2):
        curr, prev= curr+prev, curr
    return curr


def fibonacci2(n):
    if n<3:
        return 1
    else:
        return fibonacci2(n-1)+fibonacci2(n-2)


# Generator fibonacci

def fibonacci_v3(limit):
    a, b, c = 0, 1, 0
    while c < limit:
        yield a
        a, b, c = b, a+b, c+1

#from interview
def fibonacci_v4(n):
    def fib(cnter, curr, prev):
        if n<3:
            return 1
        if cnter==n:
            return curr
        else:
            curr, prev = curr+prev, curr
            #prev = curr
            cnter+=1
            return fib(cnter, curr, prev)
    return fib(1,1,0)


def Main():
    print (fibonacci(5))
    print (fibonacci2(5))
    print (fibonacci_v4(5))


'Run the Main function if the module is open(vs. imported)'
if __name__ == "__main__":
    Main()