import socket   
import time
import sys
    
SERVER_IP = "10.1.1.180"
SERVER_PORT = 7654
print("Starting socket: TCP...")
socket_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
print("Connecting to server @ %s:%d..." %(SERVER_IP, SERVER_PORT))
server_addr = (SERVER_IP, SERVER_PORT)
socket_tcp.connect(server_addr)  
 
data = socket_tcp.recv(512)
print("Server: %s" %data)
 
socket_tcp.close()
