import re
# (?=.*[0-9])
def check_password(passwd):
    mark=0
    myset=["error","weak","below middle" ,"above middle","strong"]
    if len(passwd)<6:
        return "not suitable for password"
    else:
        if  re.match(r'^(?=.*[A-Z])\w.*$',passwd):
            mark+=1
        if re.match(r'^(?=.*[a-z]).*$',passwd):
            mark+=1
        if re.match(r'^(?=.*[0-9]).*$',passwd):
            mark+=1
        if re.match(r'^(?=.*[,.;!?<>]).*$',passwd):
            mark+=1
    return myset[mark]

Pword=input()
print(check_password(Pword))
