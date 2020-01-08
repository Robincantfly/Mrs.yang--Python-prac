def fibo(n):
    n1,n2=0,1
    while n1 <= n:
        yield n1
        n1,n2=n2,n1+n2

L=0
n=eval(input())
for i in fibo(n):
    print(i,end=", ")
    L+=1

print(sum(fibo(n)),round(sum(fibo(n))/L),sep=", ")


