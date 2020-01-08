n=eval(input())
mark=0
for num in range(int(n/2)+1,0,-1):
    temp=num*(num+1)/2
    if n-temp>0 and (n-temp)%(num+1)==0:
        mark+=1
        initial=(n-temp)/(num+1)
        for i2 in range(0,num+1):
            print(int(initial),end=' ')
            initial+=1
        print('')
if mark==0:
    print('no')
