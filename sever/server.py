import socket

def writeListFile(filename,data):
    with open(filename,"w",encoding="utf8") as file:
        file.write(data)

def splitTOList(string,filename):
    name = []
    if (string == ""):
        name.append(filename)
    else:
        name = string.split("\n")
        if (filename not in name):
            name.append(filename)
    #name = name.remove('')
    return name
def changeListString(nameList):
    temp = ""
    for i in nameList:
        if (i == ''):
            continue
        i = i.replace("\n","")
        temp += i + "\n"
        print(temp)
    return temp
def Main():
    host = "127.0.0.1"
    port = 5555

    mySocket = socket.socket()
    mySocket.bind((host, port))

    mySocket.listen(10)
    while True:
        conn, addr = mySocket.accept()
        print("From: " + str(addr))
        message = conn.recv(1024).decode()
        print(message)
        if not message:
            print("Invalid connection")
        if message == "upload":
            filename = conn.recv(1024).decode()
            print("filename : ",filename)
            with open("list.txt","r",encoding="utf8") as file:
                temp = file.read()
                listFilename = splitTOList(temp,filename)
                print(listFilename)
                writeListFile("list.txt",changeListString(listFilename))

            file = open(filename,'wb')  # open in binary
            byte_file = conn.recv(1024)
            while (byte_file):
                file.write(byte_file)
                byte_file = conn.recv(1024)
            file.close()

        elif message == "download":
            filename = conn.recv(1024).decode()
            file = open(filename, "rb")
            byte_file = file.read(1024)
            while (byte_file):
                conn.send(byte_file)
                byte_file = file.read(1024)
            file.close()
        elif message == "lookup":
            print("look up list file")
            file = open("list.txt", "r")
            string_file = file.read()
            conn.send(string_file.encode())
            file.close()
        print("Conn Close")
        conn.close()

if __name__ == '__main__':
    Main()