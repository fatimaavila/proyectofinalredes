from network import Network
from game import game



n = Network()
print("cliente")
id = int(n.getPos()) + 1




while True:
   
    board = n.receive_board()
    print("loop")
    current_turn = board.turn
    print("turn = ", current_turn)
    print("id = ", id)
    if board.turn == id:
        board.print_board()
        move = board.get_player_move()
        """
        for row in range(board.rows-1, -1, -1):
                if board.board[row][move] == ' ':
                    board.board[row][move] = '🔴' if board.turn == 1 else '🟡'
                    break
        """
        send = str(move)
        #print("second board")
        #board.print_board()
        n.send(send)
    else:
        send = "n"
        n.send(send)

    
    

    
 
