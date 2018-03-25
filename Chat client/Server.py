import socket
import os


def Main():
    os.system('cls')

    print('Settings:')

    host = '127.0.0.1'
    print('Host: ' + host)
    port = input("Port (default 8675): ")
    if port != "":
        port = int()
    if port == 0:
        print('Invalid port')
        port()
    if port == "":
        port = 8675

    s = socket.socket()
    s.bind((host, port))
    s.listen(1)

    hostname = socket.gethostbyname(socket.gethostname())

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
    c.close
Main()

if __name__ == '__main__':
    Main()
