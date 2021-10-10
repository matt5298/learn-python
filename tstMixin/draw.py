import tkinter as tk

class mixinMessages(object):
    def setMessageHello(self):
        message = tk.Label(self.root, text="Hello, World!")
        message.pack()

    def setMessageLater(self):
        message = tk.Label(self.root, text="Later Aligator!!!!")
        message.pack()

class BaseTkApp:
    def __init__(self):
        self.root = tk.Tk()

    def runApp(self):
        self.root.mainloop()



class NewApp(mixinMessages, BaseTkApp):
    def __init__(self):
        super().__init__()
        self.setMessageHello() 
        self.setMessageLater()
        self.runApp()


if __name__=='__main__':
    app = NewApp()