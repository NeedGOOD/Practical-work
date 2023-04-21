import socket
import pickle
import threading
import os

def printChat():
    chat = ""
    while True:
        try:
            chat = sock.recv(1024)
        except ConnectionAbortedError:
            print("Клієнт зупинив роботу.")
            return
        if chat:
            os.system("cls")
            print(chat.decode())
            print(name + ": ", end="")
        else:
            return

name = input("Введіть ім'я: ")

sock = socket.socket()
sock.connect(('localhost', 7070))

print("Щоб вийти введіть - \"Вийти з чату\".")
print(name + ": ", end="")

thr = threading.Thread(target=printChat)
thr.start()

while True:
    text = input()
    info = [name, text]
    sock.send(pickle.dumps(info))
    if text in ("end", "кінець", "Вийти з чату", "вийти з чату"):
        break

sock.close()