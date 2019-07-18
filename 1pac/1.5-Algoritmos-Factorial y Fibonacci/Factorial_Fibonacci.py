def factorialAsc(n):
    n=int(n)
    factorial=1
    for i in range(1,n+1,1):
        factorial *= i

    return factorial

def factorialDesc(n):
    n=int(n)
    factorial=1
    for i in range(n,0,-1):
        factorial *= i

    return factorial

def fibonacci(n):
    n = int(n)
    if(n==1 or n==0):
        return n
    elif(n>1):
        return fibonacci(n-1) + fibonacci(n-2)
    else:
        return False