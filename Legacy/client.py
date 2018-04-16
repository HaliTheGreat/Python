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

def updateChat():
    global prevData
    prevData = ""
    while True:
        global s
        data = s.recv(2048)
        if prevData != "":
            if data != prevData:
                StringData = data.decode()
                os.system('cls')
                print(StringData)
        prevData = data

threading._start_new_thread(updateChat, () )

message = ""
while message != 'quit':
    print('Type to send message, "quit" to quit.')
    message = input('> ')
    output = "<" + nickname + ">: " + message
    bytern = output.encode()
    s.sendall(bytern)
s.close()