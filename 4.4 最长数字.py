import re
inp = input()
mln = 0
num = re.findall(r'[0-9]+', inp)
for n in num:
    len = len(n)
    if len > mln:
        ml = len
        mln = n
print(mln)
