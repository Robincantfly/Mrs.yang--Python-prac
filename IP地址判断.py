x=input().split(".")
if len(x)!=4:
    print("No")
else:
    pin=0
    for i in x:
        if i.isnumeric()==False or int(i) not in range (0,256):
            pin=1
            break
    if pin==0:
        print("Yes")
    else:
        print("No")


