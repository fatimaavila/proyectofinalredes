import socket

class Network:
    def __init__(self) -> None:
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        #Cambiar a mi propia IPv4
        self.server = "192.168.5.32"
        self.port = 5555
        self.addr = (self.server, self.port)
        self.pos = self.connect()

    def getPos(self):
        return self.pos
        

    def connect(self):
        
        self.client.connect(self.addr)
        return self.client.recv(2048).decode("ascii")
        

    def send (self,data):
         
        self.client.send(data.encode("ascii"))
        return self.client.recv(2048).decode("ascii")
    
n = Network()


    


