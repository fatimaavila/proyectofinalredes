import socket
import pickle

class Network:
    def __init__(self) -> None:
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        #Cambiar a mi propia IPv4
        self.server = "192.168.1.238"
        self.port = 9090
        self.addr = (self.server, self.port)
        self.pos = self.connect()

    def getPos(self):
        return self.pos
        
    #SE CONECTA AL SERVER
    def connect(self):
        self.client.connect(self.addr)
        return self.client.recv(2048).decode("ascii")
        
    #ENVIA UN STR
    def send(self,data):         
        self.client.send(data.encode("ascii"))
        
    #RECIBE OBJETO BOARD COMO BINARIO Y LO CONVIERTE EN OBJETO
    def receive_board(self):
        data = self.client.recv(2048*8) 
        board = pickle.loads(data) 
       
        return board
       
    


    


