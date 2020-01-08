def fac(n):
    if(n>0):
        return n*fac(n-1)
    else:
        return 1
a=b=int(input())
result= divmod(a, 10)[0]
sum=0
while a>=10:
    result, remainder = divmod(a, 10)
    a = result
    sum += fac(remainder)
sum+=fac(result)
print(sum)
if sum==b:
    print("YES")
else:
    print("NO")

