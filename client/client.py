import socket


def Main():
    host = '127.0.0.1'
    port = 5555
    mySocket = socket.socket()
    mySocket.connect((host, port))

    message = input("USER : ")

    while message != 'q':
        mySocket.send(message.encode())
        data = mySocket.recv(1024).decode()

        print('server: ' + data)

        message = input("USER : ")

    mySocket.close()


if __name__ == '__main__':
    Main()