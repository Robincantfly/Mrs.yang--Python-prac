#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 客戶端程序接受一个输入的字符串就会退出，如有需要就再次运行即可
# 服务器端程序会一直运行监听下去，直到收到“QUIT”
import socket

phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

phone.connect(('127.0.0.1', 5000))
msg=input("press 1 to get current time:").encode('utf-8')
phone.send(msg)  # 发消息
data = phone.recv(1024).decode()
print('现在的时间是: ', data)
phone.close()