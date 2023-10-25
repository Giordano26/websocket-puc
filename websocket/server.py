import socket
import threading

#any port that doesn't belong to a crucial app
PORT = 8765

#gethostname -> machine name 
#gethostby name -> get ip by machine name 
HOST = socket.gethostbyname(socket.gethostname())

#tuple for host and port
ADDR = (HOST, PORT)

#Create a new socket
#socket.AF_INET -> socket family IPV4
#socket.SOCK_STREAM -> streaming data on the socket
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#anything that hits the address -> addr(HOST + PORT), will be on this socket
server.bind(ADDR)

