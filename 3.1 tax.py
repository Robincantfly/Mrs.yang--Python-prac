n=int(input())
tax=0
if(n<=3500):
    tax=0
elif(n <5000):
    tax+=(n-3500)*0.03
elif(n <8000):
    tax=(n-3500)*0.1
elif(n <12500):
    tax =(n-3500)*0.2
elif(n < 38500):
    tax =(n-3500)*0.25
elif(n < 58500):
    tax = (n-3500)*0.3
else:
    tax = (n-3500)*0.35
print(int(tax))



