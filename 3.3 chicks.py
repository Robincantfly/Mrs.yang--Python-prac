Roster=0
hen=0
chick=0
# 5Roster+3Hen+chick/3＝100
# Roster+Hen+chick＝100
# 整理得：7Roster+4Hen=100．
# Roster=(100-4*hen)/7
for hen in range(int(100/3),0,-1):
    if  (100-4*hen)%7==0and(100-4*hen)/7>0 :
        Roster = (100 - 4 * hen) / 7
        chick=100-Roster-hen
        print(int(Roster),hen,int(chick))
