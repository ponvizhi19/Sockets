import socket
import sys
import time
s=socket.socket()
s.bind(('localhost',1234))
print('successfully bounded')
s.listen(1)
conn,addr=s.accept()
print(addr,"has connected")
while 1:
   message=input(str("You:>>"))
   message=message.encode()
   conn.send(message)
   incoming_message=conn.recv(1025)
   incoming_message=incoming_message.decode()
   print("client:>>",incoming_message)
