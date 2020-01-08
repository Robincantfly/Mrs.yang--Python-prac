#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# 请注意空格这样的细节问题，否则会返回sorry哦
from socket import *

HOST ='localhost'

PORT = 12345

BUFFSIZE=2048

ADDR = (HOST,PORT)

tctimeClient = socket(AF_INET,SOCK_STREAM)

tctimeClient.connect(ADDR)

while True:
    data = input(">")
    if not data:
        break
    tctimeClient.send(data.encode('utf-8'))
    data = tctimeClient.recv(BUFFSIZE).decode()
    if data=="Bye":
        break
    print(data)
tctimeClient.close()