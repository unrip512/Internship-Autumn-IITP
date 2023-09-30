import time
import socket
sock = socket.socket()

time.sleep(5)
print("I am here 3")


client_socket = socket.socket()
client_socket.connect(('10.0.111.233', 2025))

client_socket.send(b"5")

data = client_socket.recv(1024)
print(f'Получено: {data.decode()}')

data = client_socket.recv(1024)
print(f'Получено: {data.decode()}')

client_socket.close()