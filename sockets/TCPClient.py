#! /usr/local/bin/python
import socket

# targetHost = "www.google.com"
# targetPort = 80
targetHost = "0.0.0.0"
targetPort = 9999

# Create a socket object
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# Connect the client
client.connect((targetHost,targetPort))

# Send some data
client.send("GET HTTP/1.1\r\nHost:google.com\r\n\r\n")

# Receive some data
response = client.recv(4096)

print response
