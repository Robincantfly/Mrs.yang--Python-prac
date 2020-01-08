ID=input()
if len(ID)!=18:
    print("No")#初步判断（根据长度）
else:
    ID_add=ID[0:6]
    ID_sex=ID[14:17]
    ID_brith=ID[6:14]
    ID_check=ID[17]
    #ID_add是身份证中的区域代码，如果有行政区划代码字典
    #就可以获取大致地址
    W = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
    ID_num = [18, 17, 16, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2]
    ID_CHECK = ['1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2']
    ID_aXw = 0
    for i in range(len(W)):
        ID_aXw = ID_aXw + int(ID[i]) * W[i]
    ID_Check = ID_aXw % 11
    if ID_check != ID_CHECK[ID_Check]:
        print('No')
    else:
        print('Yes')
        year=ID_brith[0:4]
        moon=ID_brith[4:6]
        day=ID_brith[6:8]
        print("出生日期:"+year+'年'+moon+'月'+day+'日')
        if int(ID_sex)%2==0:
            print("性别:女")
        else:
            print("性别:男")

