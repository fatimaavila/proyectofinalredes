import socket
from _thread import *
import sys
import pickle
from game import ConnectFour
import time

#en el server se pone nuestro IPv4 (por lo menos por ahora que es local)
server = "192.168.5.32"
port = 9090

#TODO revisar que son estos sockets
server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

try:
    server_socket.bind((server, port))
except socket.error as e:
    print(str(e))

conexiones = 0
games = {}
ready = {}


#cantidad de conexiones que vamos a tener
server_socket.listen(100)
print("Esperando conexiones, el servidor ha sido iniciado")


def threaded_client(conn, p , gameId):
    global idCount
    conn.send(str(p).encode("ascii"))
    if p == 0:
        
        connect_four = ConnectFour()
        games[gameId] = connect_four
        ready[gameId] = False
        
    else:
        connect_four = games[gameId]
        connect_four.game.print_board()
        ready[gameId] = True


    while ready[gameId] == False:
        print("Esperando rival...")
        time.sleep(1.5)
        

    reply = ""
    connect_four = games[gameId]
    board_data = pickle.dumps(connect_four.game)  
    conn.send(board_data)
   
    while True:
       

        connect_four = games[gameId]                 
        data = conn.recv(2048).decode("ascii")   
        if gameId not in games:
            break
        if data != "n":
          
        
            col = int(data)
            for row in range(connect_four.game.rows-1, -1, -1):
                if connect_four.game.board[row][col] == ' ':
                    connect_four.game.board[row][col] = '🔴' if connect_four.player == 1 else '🟡'
                    break
            connect_four.game.print_board()
            

            if connect_four.check_win():
                connect_four.game.print_board()
                print(f"¡Jugador {connect_four.player} gana! 🎉")
                connect_four.game.winner = connect_four.player
                board_data = pickle.dumps(connect_four.game)
                conn.send(board_data)
                break
            if connect_four.board_full():
                connect_four.game.print_board()
                print("Tie game!")
                break
            if connect_four.player == 1:
                connect_four.player = 2
                connect_four.game.turn = 2
            else:
                connect_four.player = 1
                connect_four.game.turn = 1
            
            
        board_data = pickle.dumps(connect_four.game)
        conn.send(board_data)

    try:
        del games[gameId]
        del ready[gameId]
        print("Se ha cerrado el servidor")
    except:
        pass
    conn.close()
                

while True:
    conn, addr = server_socket.accept()
    print("conectado a: ", addr)
    conexiones += 1
    p = 0
    gameId = (conexiones - 1)//2
    
    if conexiones % 2 == 1:
        print("Creando nuevo juego....")
        print("Esperando rival...")
    else: 
        p = 1
        
    
    start_new_thread(threaded_client, (conn, p, gameId))
