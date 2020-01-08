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
def posev(x):
    x=int(x)
    for i in range(1,int(x/2)+1):
        if isprime(i)==0 and isprime(x-i)==0:
            print("{} + {} = {}".format(i,x-i,x))
