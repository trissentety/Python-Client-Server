import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(5)

# host = "10.0.0.90"
# port = 21
#So you don't have to change this every time:
host = input("Please enter the IP you want to scan: ")
port = int(input("Please enter the port you want to scan: "))


#local 443 port is open, FTP 21 is closed, 80 is closed, 4444 is closed, 4445 is closed
#(hackthissite) 22 is closed, 443 is open, 80 is open, FTP open or closed 21

def portScanner(port):
    if s.connect_ex((host, port)):
        print("The port is closed")
    else:
        print("The port is open")
portScanner(port)


#ping hackthissite.org