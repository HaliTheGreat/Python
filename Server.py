import socket
import os
import threading
import time

os.system('cls')

print('Settings:')

host = socket.gethostname()
port = input("Port (default 8675): ")
if port != "":
    port = int(port)
elif port == "":
    port = 8675
s = socket.socket()
s.bind((host, port))
s.listen(1)

hostname = socket.gethostbyname(socket.gethostname())

global chat
chat = ""
def clientConnect(c, addr):
    while True:
        global StrData
        global chat
        data = c.recv(2048)
        data = data.decode('utf-8')
        StrData = str(data)
        chat = chat + "\n" + StrData
        

def clientChatUpdate(c, addr):
    while True:
        global chat
        data = chat
        byter = data.encode()
        os.system('cls')
        print(chat)
        c.sendall(byter)



print('Server started on ' + hostname + ":" + str(port))

while True:
    c, addr = s.accept()     # Establish connection with client.
    threading._start_new_thread(clientConnect, (c, addr))
    time.sleep(1)
    threading._start_new_thread(clientChatUpdate, (c, addr))
    print("Connection incoming: " + str(addr))