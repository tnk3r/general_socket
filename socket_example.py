import socket
import time

## Setup the target
PORT = 9900
HOST = "VIDEO_HUB_IP_ADDRESS"

##setup the server
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server = (str(HOST), PORT)

sock.connect(server)

## Send a command
sock.sendall("PUT COMMAND HERE \n")

## receive 1024 bytes in return
print sock.recv(1024)
