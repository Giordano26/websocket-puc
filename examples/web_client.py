import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #create a socket
mysock.connect(('data.pr4e.org',80)) #host(domain name)/port
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode() # .encode() converts from unicode internally to UTF-8
mysock.send(cmd) #send request to the server

while True:
    data = mysock.recv(512)#rcv = recieve, up to 512 chars
    if(len(data)< 1): #the end of the data will quit, seeing if the length is less than 1
        break
    print(data.decode()) #decode from bytes to unicode
mysock.close() #close the socket 
