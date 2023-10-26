import socket


#Port that the server is connect to
PORT = 8765

#get the host from the server start
HOST = "192.168.15.114"

#tuple for host and port
ADDR = (HOST, PORT)

#header(first 64 bytes) from requisition -> will tell the size of the msg for sockek recv
HEADER = 64

#defining the format of char is utf-8 enconding 
FORMAT = 'utf-8'


#flag for client disconnection
DISCONNECT_MESSAGE = "!DISCONNECT"

#Create a new socket
#socket.AF_INET -> socket family IPV4
#socket.SOCK_STREAM -> streaming data on the socket
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#connect client to the socket on (HOST, PORT)
client.connect(ADDR)