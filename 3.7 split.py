log=t=eval(input())

temp=[]
i=2
# 从2开始往上遍历
while 1:
    if t==i:
        temp.append(i)
        break
    #     除到只剩自己
    if t%i==0:
        temp.append(i)
        t=t/i
    #     除数合适
    else:
        i+=1
#         除数不合适

print(log," = ",sep='',end='')
if(len(temp)>=1):
    for i in range(0,len(temp)):
        if(i!=len(temp)-1):
            print(temp[i],'*',sep='',end='')
        else:
            print(temp[i])
else:
    print('no')
