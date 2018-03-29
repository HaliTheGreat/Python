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
clients = set()
def clientAccepted(c, addr):
    clients.add(c)
    global history
    global lastRec
    lastRec = ""
    while True:
        rec = c.recv(20480)
        rec = rec.decode('utf-8')
        if rec != lastRec:
            history = history + "\n" + str(rec)
            lastRec = rec
            threading._start_new_thread(updateClients, (c, addr, history) )

def updateClients(c, addr, history):
    sentMessage = history.encode()
    c.send(sentMessage)

while True:
    c, addr = s.accept()
    print('Connection incoming from ' + str(addr) )
    print(str(clients))
    threading._start_new_thread(clientAccepted, (c, addr) )