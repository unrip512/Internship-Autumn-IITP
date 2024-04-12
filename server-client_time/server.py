import socket
import time
server_socket = socket.socket()
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_socket.bind(('', 2348))

for i in range(3):
    server_socket.listen(1)
    print("Сервер запущен и ожидает подключений...")

    client_socket, client_address = server_socket.accept()
    print(f"Клиент подключился: {client_address}")

    num = client_socket.recv(1024)
    print(f"Клиент отправил данные: {num}, {type(num)}")
    num = int(num.decode())

    for i in range(num):
        client_socket.send((time.ctime(time.time())).encode())
        time.sleep(5)

    client_socket.close()
