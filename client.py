from network import Network
from game import game
import time


#SE ESTABLECE LA CONEXIÓN
n = Network()

#SE BUSCA EL ID DEL JUGADOR
id = int(n.getPos()) + 1
print("Usted es el jugador ",id)

#IMPRIME EL BOARD O ESPERA HASTA QUE SE CONECTE JUGADOR 2
if id == 2:
    game = game()
    game.print_board()
else:
    print("Esperando rival...")

#LOOP DE CUANDO ESTÁ ESPERANDO A QUE SEA SU TURNO
while True:
    
    #CUANDO SE ACABE EL JUEGO ESTO DA ERROR Y YA SE SALE DEL WHILE
    try:
        board = n.receive_board()
    except:
        print("Usted ha perdido")
        break
    current_turn = board.turn
    if board.winner != None:
        print("FELICIDADES HA GANADO")
        break
    #SI ES TURNO ESCOGER LA JUGADA
    if board.turn == id:
        board.print_board()
        move = board.get_player_move()
        
        for row in range(board.rows-1, -1, -1):
                if board.board[row][move] == ' ':
                    board.board[row][move] = 'X' if board.turn == 1 else '0'
                    break
        
        send = str(move)
        board.print_board()
        n.send(send)
        
    #SI NO ES TURNO, ESPERAR
    else:
        send = "n"
        n.send(send)
        time.sleep(1.5)
        print("Esperando...")

    
    

    
 
