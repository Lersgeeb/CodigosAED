def NFibonacci(n):
    n1 = 0
    n2 = 1

    if(n<2):
        return n
    
    for i in range(2,n+1,1):
        
        nEsimo = n1 + n2 
        n1 = n2
        n2 = nEsimo
        if(n==i):
            return nEsimo

    
print(NFibonacci(1))
print(NFibonacci(2))
print(NFibonacci(3))
print(NFibonacci(4))
print(NFibonacci(5))
print(NFibonacci(6))
print(NFibonacci(7))