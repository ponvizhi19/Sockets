import socket
import sys
import time
c =socket.socket()
c.connect(('localhost',1234))
print("connected to server")
while 1:
    incoming_message = c.recv(1024)
    incoming_message = incoming_message.decode()
    print("server:>>",imcoming_message)
    message = input(str("You:>>"))
    message = message.encode()
    s.send(message)
    
