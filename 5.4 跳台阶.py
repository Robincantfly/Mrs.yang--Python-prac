def jump(target):
    temp=[0,1,2]
    if (target<3) :
        return temp[target]
    s1 = 1
    s2 = 2
    s3 = 1
    for i in range(3,target+1):
        # 一级台阶易得，二级台阶易得，那我从第三级台阶开始就用
        # 前两级相加，然后修改s1 s2
        # 递归的反面就是用数组通通存下来，或“磁头”不断移位扫描
        s3 = s1 + s2
        s1 = s2
        s2 = s3
    return s3
print(jump(eval(input())))


