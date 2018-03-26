import socket
import os
import threading


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

message = ""
while message != 'quit':
    print('Type to send message, "quit" to quit.')
    message = input('> ')
    output = "<" + nickname + ">: " + message
    bytern = output.encode()
    s.sendall(bytern)
    data = s.recv(2048)
    StringData = data.decode()
    os.system('cls')
    print(StringData)
s.close()