import socket





def Main():
    host = '127.0.0.1'
    port = 12345

    s = socket.socket()
    s.bind((host, port))

    s.listen(1)
    c, addr = s.accept()
    print("Connection incoming: " + str(addr))
    while True:
        data = c.recv(2048)
        data = data.decode('utf-8')
        StrData = str(data)
        if not data:
            break
        print("from user: " + StrData)
        data = "To the renfair: " + StrData
        print("Sending user data: " + StrData)
        byter = data.encode()
        c.sendall(byter)
    c.close()

if __name__ == '__main__':

    Main()