import socket

#1024 bytes, strip eliminates b from string
def banner(ip, port):
    s = socket.socket()
    s.connect((ip,int(port)))
    s.settimeout(5)
    print(s.recv(1024))
    print(str(s.recv(1024)).strip('b'))

def main():
    ip = input("Please enter the IP: ")
    port = str(input("Please enter the port: "))
    banner(ip, port)

#calls banner
main()



#broken
# import socket

# #socket module from socket class
# s = socket.socket()

# ip = input("Please enter the IP: ")

# #first converted to string
# port = str(input("Please enter the port: "))

# #connect function, conversion back to integer
# s.connect(ip, int(port)) #broken

# print(s.recv(1024))
