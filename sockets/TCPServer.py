#! /usr/local/bin/python
import socket
import threading

bindIP = "0.0.0.0"
bindPort = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((bindIP,bindPort))

server.listen(5)

print "[*] Linstening on %s:%d" %(bindIP, bindPort)

# Client handling thread
def handleClient(clientSocket):
    # Print out what the client sends
    request = clientSocket.recv(1024)
    print "[*] Received: %s" %request
    # Send back a packet
    clientSocket.send("ACK!")
    clientSocket.close()

while True:
    client,addr = server.accept()
    print "[*] Accepted connection from %s:%d" %(addr[0], addr[1])
    # Spin up our client thread to handle incoming data
    clientHandler = threading.Thread(target=handleClient, args=(client,))
    clientHandler.start()
