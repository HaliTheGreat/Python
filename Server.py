import socket


def Main():
    host = '127.0.0.1'
    port = 8675

    s = socket.socket()
    s.bind((host, port))
    s.listen(1)
    while True:
        c, addr = s.accept()
        print("Connection incoming: " + str(addr))
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


if __name__ == '__main__':
    Main()
