#!/usr/bin/env python3
#-*- coding:utf-8 -*-

from socket import *
from time import ctime

mydict={
'How are you?' :                'Fine,thank you.',
"How old are you? " :              "21",
"What is your name?":           "陈田瀚",
"What's your name?" :           "陈田瀚",
"What time is it? ":               ctime(),
"Please tell me a secret about you." : "I don't think so.",
"Are you happy? ":               "Better than previous",
"Where do you work?":          "CAU",
}
host = ''
port = 12345
buffsize = 2048
ADDR = (host,port)

tctime = socket(AF_INET,SOCK_STREAM)
tctime.bind(ADDR)
tctime.listen(3)

while True:
    print('Wait for connection ...')
    tctimeClient,addr = tctime.accept()
    print("Connection from :",addr)

    while True:
        data = tctimeClient.recv(buffsize).decode('utf-8')
        print(data=="Bye")
        if data in mydict:
            tctimeClient.send(('%s' % (mydict[data])).encode())
        elif data=="Bye":
            tctimeClient.send('Bye'.encode())
            break
        else:
            tctimeClient.send('Sorry'.encode())
tctimeClient.close()