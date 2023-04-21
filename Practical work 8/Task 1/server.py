import socket
import pickle
import threading

chat = ""

def newClient(conn, clients):
    work = True
    name = ""
    global chat
    while work:
        data = pickle.loads(conn.recv(4096))
        name = data[0]
        chat += data[0] + ": " + data[1] + '\n'
        for i in range(len(clients)):
            try:
                clients[i].send(chat.encode())
            except ConnectionResetError:
                del clients[i]
                chat += "Користувач " + name + " вийшов з чату.\n"
                for i in clients:
                    i.send(chat.encode())

sock = socket.socket()
sock.bind(('', 7070))
sock.listen(2)

clientName = []
clients = []

while True:
        conn, _ = sock.accept()
        if conn:
            clients.append(conn)
            thr = threading.Thread(target=newClient, args=(conn, clients))
            thr.start()