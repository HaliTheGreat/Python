import socket

from Tools.scripts.treesync import *


def Main():
    host = "127.0.0.1"
    port = 12345

    s = socket.socket()
    s.connect((host, port))

    marsuge = raw_input("Enter your data or type 'quit' to quit: ")
    bytern = marsuge.encode()
    while marsuge != 'quit':
        s.sendall(bytern)
        data = s.recv(1024)
        StringData = data.decode()
        print("Server said: " + StringData)
        marsuge = raw_input("Send another one: ")
        bytern = marsuge.encode()
    s.close()

if __name__ == '__main__':
    Main()
