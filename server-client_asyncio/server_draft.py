import socket
from select import select
import asyncio

tasks = []
to_read = {}
to_write = {}


async def waiting_client(server_socket):
    client_socket, addr = server_socket.accept()
    yield client_socket

async def receive_message(client_socket):
    while True:
        request = client_socket.recv(4096)
        yield request


async def send_message(client_socket, message):
    client_socket.send(message)





async def server():
    server_socket = socket.socket()
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('', 2349))
    server_socket.listen()

    print("Сервер запущен и ожидает подключений...")

    while True:
        client_socket = await waiting_client(server_socket)
        print('Connection')


async def client(client_socket):
    while True:
        request = await receive_message(client_socket)

        if not request:
            break
        else:
            await send_message(client_socket, 'Hi'.encode())

    client_socket.close()




def  event_loop():



    while any([tasks, to_read, to_write]):
        ready_to_read, ready_to_write, _ = select(to_read, to_write, [])

        for sock in ready_to_read:
            tasks.append(to_read.pop(sock))

        for sock in ready_to_write:
            tasks.append(to_write.pop(sock))


    try:

        task = tasks.pop(0)

        reason, sock = next(task)

        if reason == 'read':
            to_read[sock] = task

        if reason == 'write':
            to_write[sock] = task

    except StopIteration:
        print('Done!')

tasks.append(server())
event_loop()