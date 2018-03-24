import socket
import os


def Main():
    os.system('clear')

    print('Settings:')

    host = '127.0.0.1'
    print('Host: ' + host)
    port = input("Port (default 8675): ")

    if port == "":
        port = 8675

    s = socket.socket()
    s.bind((host, port))
    s.listen(1)

    hostname = socket.gethostbyname(socket.gethostname())

    print('Server started! Tell your friends to connect with ' + hostname + ":" + str(port))

    while True:
        c, addr = s.accept()
        print("Connection incoming: " + str(addr))
        c.send('Connected!')
        while True:
            data = c.recv(2048)
            data = data.decode('utf-8')
            StrData = str(data)
            if not data:
                break
            print("Sent message: " + StrData)
            data = StrData
            print("Sending user data: " + StrData)
            byter = data.encode()
            c.sendall(byter)
        c.close()
    c.close
Main()

if __name__ == '__main__':
    Main()
