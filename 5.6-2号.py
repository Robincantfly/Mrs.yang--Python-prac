class Vecter3:
    def __init__(self, x_=0, y_=0, z_=0):  # 构造函数
        self.x = x_
        self.y = y_
        self.z = z_
    def __add__(self, obj):  # 重载+作为加号
        return Vecter3(self.x + obj.x, self.y + obj.y, self.z + obj.z)
    def __sub__(self, obj):  # 重载-作为减号
        return Vecter3(self.x - obj.x, self.y - obj.y, self.z - obj.z)
    def __mul__(self, k):  # 重载*作为点乘
        return Vecter3(self.x * k, self.y * k, self.z * k)
    def __truediv__(self, k):
        return Vecter3(self.x / k, self.y / k, self.z / k)

    def show(self):
        print("({},{},{})".format(self.x,self.y,self.z))
# m=eval(input())
#
# n=eval(input())
#
# k=eval(input())
#
# v1 = Vecter3(m[0],m[1],m[2])
# v2 = Vecter3(n[0],n[1],n[2])
# v3 = v1+v2
# v3.show()
# v4 = v1-v2
# v4.show()
# v5 = v1*k
# v5.show()
# v6 = v1/k
# v6.show()





