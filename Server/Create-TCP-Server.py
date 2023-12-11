#socket module
import socket

#serversocket object calls socket function, specify socket type, socket family, type of TCP conn SOCK_STREAM
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#give value to host, gets host name, gets ip address/ID of server, might be wrong on windows
# host = socket.gethostbyname()
#alt cmd > ipconfig > ipv6 address, host = 2601:1c0:c701:2d50::945b


#specify port number, accept admin privelages for file permissions
port = 4444

#use server socket object and bind address which is host, port to socket 
serversocket.bind(('10.0.0.90', port))
#alt: '2601:1c0:c701:2d50::945b'

#set up TCP listener, listens for connections, max 3 in this example. change for more.
serversocket.listen(3)

#two variables created to equal serversocket.accept(), info accepted from client, accepts TCP info coming from client
while True:
    clientsocket, address = serversocket.accept()

#message with address converted to string
print("recieved connection from " % str(address))

#\r\n next line, sent to client once connected to server
#% convert to different data types. inside a string "%s" "%r" means more than one data type
message = 'thanks for connecting to server' + "\r\n"



#encoding type ascii
clientsocket.send(message.encode('ascii'))

#send function for sending information
clientsocket.send(message)

#close socket
clientsocket.close()

