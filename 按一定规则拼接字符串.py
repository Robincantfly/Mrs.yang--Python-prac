a=input()
b=input()
res=[]
for i in a:
    if b.find(i)>=0:
        res=a[:a.find(i)]+b[b.find(i):]
        break
if res !=[]:
    print(res)
else:
    print("")
