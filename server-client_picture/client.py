import time
import socket

time.sleep(5)
client_socket = socket.socket()
client_socket.connect(('10.0.111.233', 2349))

f = open('got_image.jpg', mode='wb')
data = client_socket.recv(2048)

while data:
    f.write(data)
    data = client_socket.recv(2048)

f.close()
client_socket.close()
