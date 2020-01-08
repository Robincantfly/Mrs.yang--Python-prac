N1=4
string="This is a test case"
N2=len(string)//4+1
a=[]
b=[a]*N1
for i in range(0,N1):
    for j in range(0,N2):
        if N1*j+i<len(string):
            b[i].append(string[N1*j+i])


print(b)


