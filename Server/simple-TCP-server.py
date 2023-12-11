import socket,os
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
sock.bind(('10.0.0.90', 4444))  
sock.listen(4)  
while True:  
    connection,address = sock.accept()  
    buf = connection.recv(1024)  
    print(buf)
    connection.send(buf)    		
    connection.close()