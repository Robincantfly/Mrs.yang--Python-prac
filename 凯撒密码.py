# 65-90 97-122
x=input()
b=""
for i in x:
    if ord(i) in range(65,91):
        b+=chr((ord(i)-62)%26+65)
    elif ord(i) in range(97,123):
        b+= chr((ord(i) - 94) % 26 + 97)
    else:
        b+=i
print(b)




