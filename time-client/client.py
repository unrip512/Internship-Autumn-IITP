import time
import socket
from base64 import b64decode as dec
from base64 import b64encode as enc
from io import BytesIO
from PIL import Image

from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

num = 1

time.sleep(5)
client_socket = socket.socket()
client_socket.connect(('10.0.111.233', 2348))

client_socket.send((str(num)).encode())

for i in range(num):
    data = client_socket.recv(1024)
    print(f'Получено: {data.decode()}')

by_pic = client_socket.recv(30000)
pic = BytesIO(dec(by_pic))
pillow = Image.open(pic)
y = Image._show(pillow)

client_socket.close()
