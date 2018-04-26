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

history = " "
update = "0"
def clientAccepted(c, addr):
    threading._start_new_thread(recieveMessages, (c, addr))
    threading._start_new_thread(updateClients, (c, addr))

def recieveMessages(c, addr):
    global history
    global update
    while True:
        history = c.recv(2048)
        print(history)
        update = 1

def updateClients(c, addr):
    global update
    global history
    print("Update clients")
    while True:
        if update != 0:
            sentMessage = history.encode("utf-8")
            c.send(sentMessage)
            update = 0
            print("Sent!")

def debug():
    while True:
        print(update)

threading._start_new_thread(debug, ())

while True:
    c, addr = s.accept()
    print('Connection incoming from ' + str(addr) )
    threading._start_new_thread(clientAccepted, (c, addr) )
