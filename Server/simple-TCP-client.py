import socket  
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
sock.connect(('10.0.0.90', 4444))  
#sock.send('Test\n')  
sock.send(("Please input : "))  
message = sock.recv(1024)

sock.close()

print(message.decode('ascii'))
sock.close()