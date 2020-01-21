import socket

def writeListFile(filename,data):
    temp = ""
    for i in data:
        temp = temp + i + "\n"
    with open(filename,"w",encoding="utf8") as file:
        file.write(temp)

def Main():
    host = "127.0.0.1"
    port = 5555

    mySocket = socket.socket()
    mySocket.bind((host, port))

    mySocket.listen(1)
    while True:
        conn, addr = mySocket.accept()
        print("From: " + str(addr))
        data = conn.recv(1024).decode()
        if not data:
            print("not data")
        if data == "upload":
            print("USER : " + str(data))
            data = conn.recv(1024).decode()
            print("data",data)
            filename = data.split("$$")[0]
            data = data.split("$$")[1]
            try:
                #list = []
                with open("list.txt","r",encoding="utf8") as file:
                    list = file.read().split("\n")
                    print(list)
                    list.append(filename)
                    print(list)
                    writeListFile("list.txt",list)

            except:
                break
            try:
                file = open(filename,"w+", encoding="utf8")
                file.write(data)
            except:
                break
            finally:
                file.close()

        #print("USER : " + str(data))
        #data = str(data).upper()
        #file = open("testDown.txt", "r", encoding="utf8")
        #data = file.read()
        #file.close()
        #print("sending : " + str(data))

        #conn.send(data.encode())

    conn.close()


if __name__ == '__main__':
    Main()