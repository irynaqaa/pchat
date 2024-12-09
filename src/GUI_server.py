import threading
import socket
import time
from tkinter import *

server = socket.socket()
server.bind(('localhost', 63453)) 
server.listen(2)
con, addr = server.accept()

root = Tk()

def send():
    data_send = edit_Text.get()
    con.send(data_send.encode('utf-8'))
    label = Label(root, text=data_send, bg="red", fg="white")
    label.pack(side='top', fill='x')
    edit_Text.delete(0, 'end')

def recv():
    while True:
        data_recv = con.recv(1024).decode('utf-8')
        if not data_recv:
            break
        label = Label(root, text=data_recv, bg="blue", fg="white")
        label.pack(side='top', fill='x')

button = Button(root, text="Send", command=send)
edit_Text = Entry(root)

button.pack(fill='x', side='bottom')
edit_Text.pack(fill='x', side='bottom')

threading.Thread(target=recv).start()

root.geometry("400x600")
root.title("server")
root.resizable(False, False)

root.mainloop()