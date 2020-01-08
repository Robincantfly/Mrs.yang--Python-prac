i=eval(input())
def myfun(x):
    ar=[50,10,5,1]
    for i in ar:
        p1=x//i
        x=x%i
        yield p1

for i in myfun(i):
    print(i)


