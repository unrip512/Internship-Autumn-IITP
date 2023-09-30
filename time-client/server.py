import socket
server_socket = socket.socket()
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_socket.bind(('', 2025))

server_socket.listen(1)
print("Сервер запущен и ожидает подключений...")

client_socket, client_address = server_socket.accept()
print(f"Клиент подключился: {client_address}")

data = client_socket.recv(1024)
data = int(data.decode())
print(f"Клиент отправил данные: {data}, {type(data)}")

client_socket.send(b"I got you")
client_socket.close()
