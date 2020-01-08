print("Beautiful is better than ugly.")
x=input()
temp="Beautiful is better than ugly."
L=min(len(x),len(temp))
sum=0
for i in range(0,L):
    if x[i]==temp[i]:
        sum+=1
print(sum/len(temp))
