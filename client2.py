import os
import socket
import threading
import time


os.system('cls')

print('Settings:')

host = str(input('Host (default localhost): '))
if host == "":
    host = socket.gethostname()

port = input("Port (default 8675): ")
if port != "":
    port = int(port)
if port == 0:
    print('Invalid port')
    port()
if port == "":
    port = 8675


s = socket.socket()
s.connect((host, port))
print('Connected to ' + host + ':' + str(port))
nickname = input('Unique Identifier: ')

def updateChat():
    lastRec = ""
    rec = ""
    rec = rec.encode()
    chat = ""
    while True:
        rec = s.recv(2048)
        rec = rec.decode()
        print(lastRec)
        print(rec)
        if lastRec != "":
            if lastRec != rec:
                lastRec = rec
                chat = chat + "\n" + rec.decode('utf-8')
                print(chat)
        else:
            print(rec)
        lastRec = rec
        
threading._start_new_thread(updateChat, () )

while True:
        message = input('Type to send message, "quit" to quit. \n >: ')
        if message != 'quit':
            outbox = "<" + nickname + ">: " + message
            send = outbox.encode()
            s.send(send)
        else:
            exit()