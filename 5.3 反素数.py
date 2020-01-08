import math
def isprime(n):
    mark=0
    if not n>1:
        return 1
    else:
        for i in range(2,int(math.sqrt(n))+1):
            if n%i==0:
                mark=1
        if mark==0:
            return 0
        else:
            return 1
# 0 is prime,1 not prime

def numRus(a):
    b=int(str(a)[::-1])
    return b
# 0 yes,1 no



a=int(input())
pin=0
i=0
while pin<a:
    if isprime(i)==0 and isprime(numRus(i))==0:
        print(i,end=" ")
        pin+=1
    i+=1





