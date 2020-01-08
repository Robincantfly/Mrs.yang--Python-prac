x=input()
sum=0
for i in x:
    sum+=pow(int(i),3)
if sum==int(x):
    print("YES")
else:
    print("NO")
