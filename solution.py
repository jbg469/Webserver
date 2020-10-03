#John Guevara
#This is a simple Python socket web server
from socket import *
import sys 
def webServer():
    port=13331
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind(("localhost", port))
    serverSocket.listen(1)#ready

    while True:
        print("Ready to serve on port:", port)
        connectionSocket, addr = serverSocket.accept()
        try:
            mess = connectionSocket.recv(1024)
            print("HTTP MESSAGE: ", mess)
            file = mess.split()[1] #HTTP path 
            buffer = open(file[1:])
            output =buffer.read()
           #Send one HTTP header line into socket
            connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n".encode())
            #Send the content of the requested file to the client
            for j in range(0, len(output)):
                connectionSocket.send(output[j].encode())
            connectionSocket.send("\r\n".encode())
            connectionSocket.close()
        except IOError:
            connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n".encode())
            connectionSocket.send("<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n".encode())
            #Close client socket
            connectionSocket.close()

    serverSocket.close()
    sys.exit()  # Terminate the program after sending the corresponding data

if __name__ == "__main__":
    webServer()
