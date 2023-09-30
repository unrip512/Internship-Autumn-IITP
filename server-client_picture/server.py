import socket
import time

server_socket = socket.socket()

server_socket.bind(('', 2349))

server_socket.listen(1)
print("Сервер запущен и ожидает подключений...")

client_socket, client_address = server_socket.accept()
print(f"Клиент подключился: {client_address}")

pict = 'photo.jpg'

f = open(pict, mode='rb')
data1 = f.read(2048)

while data1:
    client_socket.send(data1)
    data1 = f.read(2048)

f.close()
client_socket.close()
