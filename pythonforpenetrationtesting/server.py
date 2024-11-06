import socket

#Creating the socket object
serversocketObject = socket.socket(
    socket.AF_INET,socket.SOCK_STREAM
)

#host = host IP address
host = socket.gethostbyname()
port = 444


#Binding to socket
serversocketObject.bind((host,port))#Host will be replaced with IP , if changed and not running on host 

#Starting TCP listener
serversocketObject.listen(3)

while True:
    #Starting the connection
    clientsocketObject, address = serversocketObject.accept()
    print("recieved connection from " % str(address))

    message = 'hello! thank you for connectin to the server' + "\r\n"
    clientsocketObject.send(message.encode('ascii'))

    clientsocketObject.close()

