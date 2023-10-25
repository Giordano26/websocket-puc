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

def start():
    server.listen()
    while True:
        #starts listening and waits a conn and addr from client
        #conn will allow to communicate back to the client 
        #addr -> info about ip and port is connect to the server
        conn, addr = server.accept() 

        #create a thread for handle client requisitions
        thread = threading.Thread(target=client_handle, args= (conn,addr))
        thread.start()

        #shows actual connections
        print(f"[NEW CONECCTION] New connection from {conn}/{addr}")
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")

def client_handle(conn, addr):
    pass



print(f"[STARTING] Server is starting on {HOST} at port {PORT}...")
start()