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
    global prevChat
    prevChat = ""
    while True:
        global StrData
        global chat
        data = c.recv(2048)
        data = data.decode('utf-8')
        StrData = str(data)
        #WORK ON PREV TOMORROW
        if prevChat != "":
            if prevChat != chat:
                chat = chat + "\n" + StrData
                data = chat
                byter = data.encode()
                print(StrData)
                c.sendall(byter)
            else:
                prevChat = chat
        else:
            prevChat = chat
        



print('Server started on ' + hostname + ":" + str(port))

while True:
    c, addr = s.accept()     # Establish connection with client.
    threading._start_new_thread(clientConnect, (c, addr))
    print("Connection incoming: " + str(addr))
