import socket

#specify ip protocol version handshake TCP
clientsocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#host = '10.0.0.90'
host = socket.gethostname() #preferred

port = 4444

clientsocket.connect(('10.0.0.90', port))

#??? buffer size ???
message = clientsocket.recv(1024)

clientsocket.close()

print(message.decode('ascii'))

#cmd python3 TCPClient.py