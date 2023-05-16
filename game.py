import numpy as np
import wcwidth
from tabulate import tabulate

class game:
    def __init__(self, rows = 6, cols = 7):
        self.rows = rows
        self.cols = cols
        self.board = np.full((rows, cols), ' ')
        
        self.ended = False

    def print_board(self):
        headers = [str(i) for i in range(1, self.cols+1)]
        max_col_widths = [max([wcwidth.wcwidth(cell) for cell in col]) for col in zip(*self.board)]
        formatted_board = [[cell.ljust(width) for cell, width in zip(row, max_col_widths)] for row in self.board]
        print(tabulate(formatted_board, headers=headers, tablefmt="fancy_grid"))
        


class ConnectFour:

    def __init__(self):
        self.player = 1
        self.game = game()
        

    def get_player_move(self):
        valid_move = False
        
        while not valid_move:
            col = int(input(f"Jugador {self.player}, elige donde colocar tu pieza! (1-{self.game.cols}) "))
            if col < 1 or col > self.game.cols:
                print(f"Columna invalida, elija entre (1-{self.game.cols})")
            elif self.game.board[0][col-1] != ' ':
                print("Esa columna ya está llena. 🧐")
            else:
                valid_move = True
        return col-1

    def check_win(self):
        # check para ganar horizontal
        for row in self.game.board:
            for col in range(len(row)-3):
                if row[col] == row[col+1] == row[col+2] == row[col+3] != ' ':
                    return True
        # check para verti
        for col in range(len(self.game.board[0])):
            for row in range(len(self.game.board)-3):
                if self.game.board[row][col] == self.game.board[row+1][col] == self.game.board[row+2][col] == self.game.board[row+3][col] != ' ':
                    return True
        # diagonal de arriba para abajo
        for row in range(len(self.game.board)-3):
            for col in range(len(self.game.board[0])-3):
                if self.game.board[row][col] == self.game.board[row+1][col+1] == self.game.board[row+2][col+2] == self.game.board[row+3][col+3] != ' ':
                    return True
        # abajo para arriba
        for row in range(3, len(self.game.board)):
            for col in range(len(self.game.board[0])-3):
                if self.game.board[row][col] == self.game.board[row-1][col+1] == self.game.board[row-2][col+2] == self.game.board[row-3][col+3] != ' ':
                    return True
        return False

    def board_full(self):
        for row in self.game.board:
            if ' ' in row:
                return False
        return True

    def jugar(self):
        while True:
            self.game.print_board()
            col = self.get_player_move()
            for row in range(self.game.rows-1, -1, -1):
                if self.game.board[row][col] == ' ':
                    self.game.board[row][col] = '🔴' if self.player == 1 else '🟡'
                    break
            if self.check_win():
                self.game.print_board()
                print(f"¡Jugador {self.player} gana! 🎉")
                break
            if self.board_full():
                self.game.print_board()
                print("Tie game!")
                break
            if self.player == 1:
                self.player = 2
            else:
                self.player = 1
    
    def connected(self):
        return self.ready


if __name__ == "__main__":
    connect_four = ConnectFour()
    connect_four.jugar()
