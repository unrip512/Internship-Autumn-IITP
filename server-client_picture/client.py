import time
import socket

time.sleep(5)
client_socket = socket.socket()
client_socket.connect(('10.0.111.233', 2349))

f = open('got_image.jpg', mode='wb')

while True:
    data = client_socket.recv(2048)
    if data:
        f.write(data)
    else:
        break

f.close()
client_socket.close()
