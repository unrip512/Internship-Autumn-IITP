import socket
import time
import asyncio

server_socket = socket.socket()
server_socket.bind(('', 2349))
server_socket.listen(1)
print("Сервер запущен и ожидает подключений...")


client_socket, client_address = server_socket.accept()
print(f"Клиент подключился: {client_address}")

pict = 'photo2.jpg'
f = open(pict, mode='rb')

while True:
    data1 = f.read(2048)
    if data1:
        client_socket.send(data1)
    else:
        break


f.close()
client_socket.close()
