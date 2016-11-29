"""A simple TCP client.  Doesn't use an application protocol and just sends a text message."""
import random
import socket

__author__ = 'Julian Chukwu.'
 
print('Starting TCP Client.py')

server_name = 'localhost'
server_port = 8814 


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.bind(("",random.randint(3000,4000)))
client_socket.connect((server_name,server_port))
#client_socket.getsockname()

while 1:
  message = raw_input("HalloSwitchStationTCPClient >> ")

  client_socket.send(message)
  data = client_socket.recv(4000)
  if data:
    print data

client_socket.close()


