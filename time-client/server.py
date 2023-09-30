import socket
import time
from base64 import b64encode as enc
import sys

server_socket = socket.socket()
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_socket.bind(('', 2348))

server_socket.listen(1)
print("Сервер запущен и ожидает подключений...")

client_socket, client_address = server_socket.accept()
print(f"Клиент подключился: {client_address}")

num = client_socket.recv(3000)
print(f"Клиент отправил данные: {num}, {type(num)}")
num = int(num.decode())

for i in range(num):
    client_socket.send((time.ctime(time.time())).encode())
    time.sleep(5)

pict = 'photo3.jpg'
with open(pict, 'rb') as f:
    by_pict = enc(f.read())
    print(sys.getsizeof(by_pict))
    client_socket.send(by_pict)

client_socket.close()
