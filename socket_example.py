import socket

## Setup the target
PORT = 9990
HOST = "192.168.0.150"

##setup the client
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server = (str(HOST), PORT)

sock.connect(server)

## Send a command
sock.sendall("PUT COMMAND HERE \n")

## receive 1024 bytes in return
print sock.recv(1024)
