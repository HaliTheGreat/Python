import socket
import os
import threading
import time


os.system('cls')

print('Settings:')

host = str(input('Host (default localhost): '))
if host == "":
    host = socket.gethostname()

port = input("Port (default 8675): ")
if port != "":
    port = int()
if port == 0:
    print('Invalid port')
    port()
if port == "":
    port = 8675


s = socket.socket()
s.connect((host, port))
print('Connected to ' + host + ':' + str(port))
nickname = input('Unique Identifier: ')

def sendMessage():
    message = ""
    while True:
        message = input('Type to send message, "quit" to quit. \n >: ')
        if message != 'quit':
            outbox = "<" + nickname + ">: " + message
            send = outbox.encode()
            s.send(send)
        else:
            exit()

def updateChat():
    lastRec = ""
    while True:
        rec = s.recv(20480)
        if lastRec != rec:
            lastRec = rec
            rec = rec.decode()
            os.system('cls')
            print(rec)

threading._start_new_thread(updateChat, () )
sendMessage()
