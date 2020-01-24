import socket


def Main():
    host = '127.0.0.1'
    port = 5555
    message = input("MODE : ")

    while message != "exit":
        if message == "upload":
            mySocket = socket.socket()
            mySocket.connect((host, port))
            mySocket.send(message.encode())
            print("upload : ")
            filename = input("File Name : ")
            mySocket.send(filename.encode())

            file = open(filename, "rb")
            byte_file = file.read(1024)
            while (byte_file):
                mySocket.send(byte_file)
                byte_file = file.read(1024)
            mySocket.close()
            #combine = filename + "$$" + data
            #mySocket.send(combine.encode())

            #recrive
            #data = mySocket.recv(1024).decode()
        elif message == "download":
            print("download : ")
            mySocket = socket.socket()
            mySocket.connect((host, port))
            mySocket.send(message.encode())
            filename = input("File Name : ")
            # send file name
            mySocket.send(filename.encode())

            file = open(filename, "wb")
            byte_file = mySocket.recv(1024)
            while (byte_file):
                file.write(byte_file)
                byte_file = mySocket.recv(1024)
            file.close()
            mySocket.close()
        elif message == "lookup":
            mySocket = socket.socket()
            mySocket.connect((host, port))
            mySocket.send(message.encode())

            listFile = mySocket.recv(1024)
            print(listFile.decode())

            mySocket.close()
        else:
            print("Invalid input ")

        message = input("MODE : ")

    print("close")


if __name__ == '__main__':
    Main()