#nmap module????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????
import nmap

#call nmap port scanner class
scanner = nmap.PortScanner()

print("Welcome, this is a simple nmap automation tool")
print("<-------------------------------------------->")

ipaddress = input("Type IP address to scan...")
print("Typed address: ", ipaddress)
type(ipaddress)

#next line puts cmd on new line instead of 3
resp = input(""""\nType scan to run...
                1) SYN ACK Scan
                2) UDP Scan
                3) Comprehensive Scan \n""")
print("Currently selected option: ", resp)

if resp == '1':
    print('Nmap Version: ', scanner.nmap_version())
    #ipaddress, port range to scan, verbose output simple synax
    scanner.scan(ipaddress, '1-1024', '-v -sS')
    print(scanner.scaninfo()) #prints info like TCP, services and method
    print("Ip Status: ", scanner[ipaddress].state()) ##ip online or offline
    print(scanner[ipaddress].all_protocols) 
    #keys - returnn active ports in specified range, tcp protocol, keys method
    print("Open Ports: ", scanner[ipaddress]['tcp'].keys())
#C:\Program Files (x86)\Nmap

elif resp == '2':
    print('Nmap Version: ', scanner.nmap_version())
    #ipaddress, port range to scan, verbose output simple synax
    scanner.scan(ipaddress, '1-1024', '-v -sU')
    print(scanner.scaninfo()) #prints info like TCP, services and method
    print("Ip Status: ", scanner[ipaddress].state()) ##ip online or offline
    print(scanner[ipaddress].all_protocols)
    #keys - returnn active ports in specified range, tcp protocol, keys method
    print("Open Ports: ", scanner[ipaddress]['udp'].keys())
elif resp == '3':
    #nmap version scan info status of ip, protocol, open ports
    print('Nmap Version: ', scanner.nmap_version())
    #ipaddress, port range to scan, verbose output simple synax
    scanner.scan(ipaddress, '1-1024', '-v -sS -sV -sC -A -O ') #Syn scan -sV for service fingerprinting -Sc default script -A agressive scan -O operating system detection
    print(scanner.scaninfo()) #prints info like TCP, services and method
    print("Ip Status: ", scanner[ipaddress].state()) ##ip online or offline
    print(scanner[ipaddress].all_protocols)
    #keys - returnn active ports in specified range, tcp protocol, keys method
    print("Open Ports: ", scanner[ipaddress]['tcp'].keys()) #tcp == comprehensive scan
elif resp >= '4':
    print("Please enter a valid option")