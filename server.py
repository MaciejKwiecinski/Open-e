import socket
import threading

def check(string):
    x = string.split("]")
    x[0] = x[0][1:]
    x[1] = x[1][1:]
    if x[0] == x[1]:
        return True
    else:
        return False

class Server:
    HEADER = 64
    PORT = 5051
    SERVER = socket.gethostbyname(socket.gethostname())
    ADDR = (SERVER, PORT)
    FORMAT = 'utf-8'
    DISCONNECT_MESSAGE = "!DISCONNECT"

    def __init__(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.messages = ""

    def handleClient(self, conn, addr):
        print(f"[NEW CONNECTION] {addr} connected.")

        connected = True
        while connected:
            msg_length = conn.recv(Server.HEADER).decode(Server.FORMAT)
            if msg_length:
                msg_length = int(msg_length)
                msg = conn.recv(msg_length).decode(Server.FORMAT)
                if msg == Server.DISCONNECT_MESSAGE:
                    connected = False
                elif check(msg) != True:
                    print(f"{msg}")
                    self.messages += msg + "\n"
                conn.send("Msg received".encode(Server.FORMAT))

        conn.close()


    def start(self):
        self.server.bind(Server.ADDR)
        self.server.listen()
        print(f"[LISTENING] Server is listening on {Server.SERVER}")
        while True:
            conn, addr = self.server.accept()
            thread = threading.Thread(target=self.handleClient, args=(conn, addr))
            thread.start()
            print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")
            print(chr(27) + '[2j')
            print(self.messages)

s1 = Server()
s1.start()


