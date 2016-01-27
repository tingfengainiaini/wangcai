#Created by Baoquan Wang.
from wheel import wheel_controller
import time
import socket
import sys
 
HOST_IP = "10.1.1.180"
HOST_PORT = 7654
 
print("Starting socket: TCP...")
socket_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
print("TCP server listen @ %s:%d!" %(HOST_IP, HOST_PORT) )
host_addr = (HOST_IP, HOST_PORT)
socket_tcp.bind(host_addr)
socket_tcp.listen(1)
 
socket_con, (client_ip, client_port) = socket_tcp.accept()
print("Connection accepted from %s." %client_ip)
socket_con.send("Welcome to RPi TCP server!")
socket_tcp.close()
