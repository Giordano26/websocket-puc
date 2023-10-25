import socket
import threading

#any port that doesn't belong to a crucial app
PORT = 8765

#gethostname -> machine name 
#gethostby name -> get ip by machine name 
SERVER = socket.gethostbyname(socket.gethostname())

print(SERVER)