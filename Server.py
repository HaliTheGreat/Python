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

    while True:
        data = c.recv(2048)
        data = data.decode('utf-8')
        StrData = str(data)
        if not data:
            break
        data = StrData
        byter = data.encode()
        print(StrData)
        c.send(byter)
