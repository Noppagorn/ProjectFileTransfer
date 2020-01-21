import socket


def Main():
    host = '127.0.0.1'
    port = 5555
    mySocket = socket.socket()
    mySocket.connect((host, port))

    message = input("MODE : ")

    while message != "exit":
        if message == "upload":
            mySocket.send(message.encode())
            print("upload : ")
            filename = input("File Name : ")
            file = open(filename, "r", encoding="utf8")
            data = file.read()
            file.close()

            combine = filename + "$$" + data
            mySocket.send(combine.encode())

            #recrive
            #data = mySocket.recv(1024).decode()
        elif message == "download":
            print("download : ")
        else:
            print("Invalid input ")

        message = input("MODE : ")

    mySocket.close()


if __name__ == '__main__':
    Main()