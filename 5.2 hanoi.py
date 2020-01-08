def move(n, a='A', b='B', c='C'):
    if n==1:
        print (a,'-->',c,sep='',end=' ')
        return
    else:
        move(n-1,a,c,b)  #首先需要把 (N-1) 个圆盘移动到 b
        move(1,a,b,c)    #将a的最后一个圆盘移动到c
        move(n-1,b,a,c)  #再将b的(N-1)个圆盘移动到c

move(eval(input()))

# 我每次看到这个方法都有种很奇妙的感觉