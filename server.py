import socket
import _thread
import sys
import pickle

#en el server se pone nuestro IPv4 (por lo menos por ahora que es local)
server = "192.168.5.32"
port = 5555

#TODO revisar que son estos sockets
server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

try:
    server_socket.bind((server, port))
except socket.error as e:
    print(str(e))

conexiones = 0

#cantidad de conexiones que vamos a tener
server_socket.listen(2)
print("Esperando conexiones, el servidor ha sido iniciado")


def client_checkup(conn):

    conn.send(str.encode("conectado"))

    respuesta = ""
    while True:
    
        #2048 son los bits
        data = conn.recv(2048)
        #ascii o utf-8 para codificar
        respuesta = data.decode("ascii")

        if not data:
            print("Desconectado")
            break
        
        else:
            print("Recieved: ", respuesta)
            print("enviando: ", respuesta)
        
        conn.sendall(str.encode(respuesta))
        
    print("conexión perdida")
    conn.close

while True:
    conn, addr = server_socket.accept()
    print("conectado a: ", addr)
    conexiones += 1
    client_checkup(conn)

