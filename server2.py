import socket
import socketserver
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

def clientAccepted(c, addr):
    threading._start_new_thread(updateClients, (c, addr))
    threading._start_new_thread(recieveMessages, (c, addr))

def recieveMessages(c, addr):
    global history
    while True:
        history = c.recv(2048)

def updateClients(c, addr):
    while True:
        sentMessage = history.encode("utf-8")
        c.send(sentMessage)

while True:
    c, addr = s.accept()
    print('Connection incoming from ' + str(addr) )
    threading._start_new_thread(clientAccepted, (c, addr) )


