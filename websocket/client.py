import socket


#Port that the server is connect to
PORT = 8765

#get the host from the server start
HOST = "127.0.1.1"

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


def send(msg):
    #when sending messages, its crucial to enconde them to bytes objects
    #then send them to socket
    message = msg.encode(FORMAT)

    #we need to format and pad the 64 bytes header for the message length
    #so the server can handle properly the size of the message we are sending
    msg_length = len (message)
    send_length = str(msg_length).encode(FORMAT)

    #calculation for the padd -> byte size of space * (64 bytes header - len of the msg)
    #making sure that the first 64 bytes are just the header
    send_length += b' ' * (HEADER - len(send_length))

    #send first the header then the actual message
    client.send(send_length)
    client.send(message)

def start():
    username = input("Who are you?: ")
    send(username)
    connected = True

    while connected:
        client_msg = input("> ")
        send(client_msg)
        if client_msg == DISCONNECT_MESSAGE:
            print("Now Disconnecting...")
            connected = False
            
start()
exit()
