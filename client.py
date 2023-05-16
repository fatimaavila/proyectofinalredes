from network import Network
from game import game
import time



n = Network()

id = int(n.getPos()) + 1
print("Usted es el jugador ",id)

if id == 2:
    game = game()
    game.print_board()
else:
    print("Esperando rival...")


while True:
    
    try:
        board = n.receive_board()
    except:
        print("Usted a perdido")
        break
    current_turn = board.turn
    if board.winner != None:
        print("FELICIDADES HA GANADO")
        break
    
    if board.turn == id:
        board.print_board()
        move = board.get_player_move()
        
        for row in range(board.rows-1, -1, -1):
                if board.board[row][move] == ' ':
                    board.board[row][move] = '🔴' if board.turn == 1 else '🟡'
                    break
        
        send = str(move)
        board.print_board()
        n.send(send)
    else:
        send = "n"
        n.send(send)
        time.sleep(1.5)
        print("Esperando...")

    
    

    
 
