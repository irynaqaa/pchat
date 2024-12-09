import threading
import socket

client = socket.socket()
client.connect(('localhost', 12451))

def recv():
    while True:
        data_get = client.recv(1024)
        if data_get:
            print(data_get.decode('utf-8'))

def send():
    while True:
        text = input(">>")
        try:
            client.send(text.encode('utf-8'))
        except TypeError:
            pass

threading.Thread(target=send).start()
threading.Thread(target=recv).start()