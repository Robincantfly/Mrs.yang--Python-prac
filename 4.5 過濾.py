import re

def check_filter(keywords, text,filterword):
     return re.sub("|".join(keywords), filterword, text)
keywords = input().split(" ")
text = input()
Fword=input()
print(check_filter(keywords, text,Fword))

