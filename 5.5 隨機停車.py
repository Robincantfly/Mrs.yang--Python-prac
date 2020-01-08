import random
low,high=0,10
L=1
def parking(f1,f2):
    if f2-f1<L:
        return 0
    else:
        x=low+random.uniform(f1,f2-1)
        return parking(f1,x)+1+parking(x+1,f2)

print(parking(low,high))