import tkinter as tk
import sched, time
from server import Server
from client import Client

class GUI:
    def __init__(self, root):
        self.users = ""
        self.root = root
        self.root.geometry("1000x670")
        self.root.title("Messenger")

        self.name = tk.Entry(self.root, font=14)
        self.name.place(x=10, y=620, width=800, height=40)
        self.name.pack(padx= 10, pady= 10, ipadx = 10, ipady= 10)

        self.name_button = tk.Button(self.root, text="Put name", command= lambda: self.create_conversation())
        self.name_button.place(x=820, y=620, width=170, height=40)
        self.name_button.pack(padx= 10, pady= 10, ipadx = 10, ipady= 10)



    def all(self):
        self.users = tk.Text(root, font=14).place(x= 680, y=10, width=300, heigh=600)
        self.conversation = tk.Text(root, font= 14).place(x= 10, y= 10, width= 660, heigh= 600)

    def message(self):
        self.message_box = tk.Entry(self.root, font= 14)
        self.message_box.place(x= 10, y= 620, width= 800, height= 40)
        self.msg_button = tk.Button(root, text= "Send message")
        self.msg_button.place(x= 820, y= 620, width= 170, height= 40)

    def create_conversation(self):
        self.name.pack_forget()
        self.name_button.pack_forget()
        self.message()
        self.all()
        c1 = Client(self.name.get())
        self.users += self.name.get() + "\n"
        s = sched.scheduler(time.time, time.sleep)
        s.enter(60, 1, self.check_message())

    def check_message(self):





root = tk.Tk()
gui = GUI(root)
root.mainloop()
