import time
import socket

num = 5

time.sleep(1)
client_socket = socket.socket()
client_socket.connect(('127.0.0.1', 2348))

client_socket.send((str(num)).encode())

for i in range(num):
    data = client_socket.recv(1024)
    print(f'cl2: Получено: {data.decode()}')

client_socket.close()
