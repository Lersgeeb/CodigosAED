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

