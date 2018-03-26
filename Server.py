import socket
import os
import threading

os.system('cls')

print('Settings:')

host = socket.gethostname()
port = input("Port (default 8675): ")
if port != "":
    port = int(port)
elif port == "":
    port = 8675
while True:
    s = socket.socket()
    s.bind((host, port))
    s.listen(1)

    hostname = socket.gethostbyname(socket.gethostname())
    os.system('cls')
    print('Server started on ' + hostname + ":" + str(port))
    c, addr = s.accept()
    print("Connection incoming: " + str(addr))

def clientConnect(c, addr):
        data = c.recv(2048)
        data = data.decode('utf-8')
        StrData = str(data)
        data = StrData
        byter = data.encode()
        print(StrData)
        c.send(byter)

while True:
       c, addr = s.accept()     # Establish connection with client.
       threading._start_new_thread(clientConnect(c,addr))