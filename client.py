import socket


class Client:
    HEADER = 64
    PORT = 5051
    FORMAT = 'utf-8'
    DISCONNECT_MESSAGE = "!DISCONNECT"
    SERVER = socket.gethostbyname(socket.gethostname())
    ADDR = (SERVER, PORT)

    def __init__(self, name):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect(Client.ADDR)
        self.name = name + "@"+ Client.SERVER
        self.send(self.name)

    def send(self, msg):
        msg = f"[{self.name}] {msg}"
        message = msg.encode(Client.FORMAT)
        msg_length = len(message)
        send_length = str(msg_length).encode(Client.FORMAT)
        send_length += b' ' * (Client.HEADER - len(send_length))
        self.client.send(send_length)
        self.client.send(message)


c1 = Client("Kappa")

while True:
    msg = input()
    if msg != "disconnect":
        c1.send(msg)
    else:
        c1.send(Client.DISCONNECT_MESSAGE)