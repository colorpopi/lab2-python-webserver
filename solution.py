# import socket module
from socket import *
# In order to terminate the program
import sys


def webServer(port=13331):
    serverSocket = socket(AF_INET, SOCK_STREAM)
    # Prepare a server socket
    serverSocket.bind(("", port))

    serverSocket.listen(1)

    while True:
        # Establish the connection
        # print('Ready to serve...')
        print("Connection open..")
        connectionSocket, addr = serverSocket.accept()
        try:

            try:
                # can receive up to 1024 bytes
                message = serverSocket.recv(1024)
                filename = message.split()[1]
                f = open(filename[1:])
                outputdata = f.read()

                # Send one HTTP header line into socket.
                connectionSocket.send("200 OK".encode("utf-8"))

                # Send the content of the requested file to the client
                for i in range(0, len(outputdata)):
                    connectionSocket.send(outputdata[i].encode())

                connectionSocket.send("\r\n".encode())
                connectionSocket.close()
            except IOError:
                # Send response message for file not found (404)
                connectionSocket.send("404 Not Found".encode("utf-8"))
                # Close client socket
                connectionSocket.close()

        except (ConnectionResetError, BrokenPipeError):
            pass

    serverSocket.close()
    sys.exit()  # Terminate the program after sending the corresponding data


if __name__ == "__main__":
    webServer(13331)
