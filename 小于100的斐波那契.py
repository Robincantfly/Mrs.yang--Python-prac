def fibo(n):
    n1,n2=0,1
    while n1 <= n:
        yield n1
        n1,n2=n2,n1+n2

for i in fibo(100):
    print(i,";",sep="",end="")