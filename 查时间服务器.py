#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 客戶端程序接受一个输入的字符串就会退出，如有需要就再次运行即可
# 服务器端程序会一直运行监听下去，直到收到“QUIT”
import socket
from time import ctime

phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
phone.bind(('127.0.0.1', 5000))
phone.listen(5)  # 开机  5的作用是最大挂起连接数   #backlog连接池（也叫半链接）
print('------------->')
conn ,addr= phone.accept()
msg = conn.recv(1024).decode('utf-8')  # 收消息
print(msg)
while(int(msg)==1):
    conn.send(ctime().encode())
    conn, addr = phone.accept()

phone.close()

