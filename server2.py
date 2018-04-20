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

history = ""

def clientRecieve(c, addr):
    history = c.recv(2048)

def clientAccepted(c, addr, chat):
    threading._start_new_thread(clientRecieve, (c, addr) )
    while True:

def updateClients(c, addr, history):
    while True:
        sentMessage = history.encode()
        c.send(sentMessage)

while True:
    c, addr = s.accept()
    print('Connection incoming from ' + str(addr) )
    threading._start_new_thread(clientAccepted, (c, addr) )


