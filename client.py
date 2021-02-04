import socket


class Client:
    HEADER = 64
    PORT = 5050
    FORMAT = 'utf-8'
    DISCONNECT_MESSAGE = "!DISCONNECT"
    SERVER = socket.gethostbyname(socket.gethostname())
    ADDR = (SERVER, PORT)

    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect(Client.ADDR)
        self.name = ""

    def set_name(self, name):
        self.name = name + "@"+ Client.SERVER

    def send(self, msg):
        message = msg.encode(Client.FORMAT)
        msg_length = len(message)
        send_length = str(msg_length).encode(Client.FORMAT)
        send_length += b' ' * (Client.HEADER - len(send_length))
        self.client.send(send_length)
        self.client.send(message)

print("podaj swój nick")
name = input()
c1 = Client()
c1.send(c1.name)

while True:
    msg = input()
    if msg != "Disconect":
        c1.send(msg)
    else:
        c1.send(Client.DISCONNECT_MESSAGE)
        break