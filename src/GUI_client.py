import socket
import threading
import time
import tkinter as tk

client = socket.socket()
client.connect(('localhost', 63453))
root = tk.Tk()

def send():
    data_send = get_message.get()
    if data_send != "":
        data_send = str(data_send)
        client.sendall(data_send.encode())
        lbl = tk.Label(root, text=data_send, bg="red", fg="white")
        get_message.delete(0, tk.END)
        lbl.pack(fill=tk.X, side=tk.TOP)

def recv():
    while True:
        data_recv = client.recv(1024)
        if data_recv != b"":
            lbl = tk.Label(root, text=data_recv.decode('utf-8'), bg="blue", fg="white")
            lbl.pack(fill=tk.X, side=tk.TOP)


get_message = tk.Entry(root)
send_message = tk.Button(root, text="Send", command=send)

send_message.pack(fill=tk.X, side=tk.BOTTOM)
get_message.pack(fill=tk.X, side=tk.BOTTOM)

threading.Thread(target=recv).start()

root.title("Chat Client")
root.geometry("500x700")
root.resizable(width=False, height=False)

root.mainloop()