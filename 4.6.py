b=input().split(' ')
a=[]
for i in b:
    temp1=list(i)
    temp1[1:-1]=[k.lower() for k in temp1[1:-1]]
    a.append("".join(temp1))
print(" ".join(a))
