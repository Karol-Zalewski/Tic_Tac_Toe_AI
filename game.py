from player import HumanPlayer, RandomComputerPlayer, GeniusComputerPlayer

class Tic_Tac_Toe:
    """"""
    def __init__(self):
        self.board = [" " for _ in range(9)] # We will use a single list to rep 3x3 board
        self.current_winner = None # Keep track of the winner

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range (3)]:
            print('| ' + ' | '.join(row)+ ' |')

    @staticmethod
    def print_board_nums():
        # 0 | 1 | 2 etc (tells us what number corresponds to what box)
        number_board = [[str(i) for i in range(j*3,(j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row)+ ' |')
    
    def available_moves(self):
        # return [i for i, spot in enumerate(self.board) if spot == ' ']
        moves = []
        for (i, spot) in enumerate(self.board):
            # ['x', 'x', 'o']-->[(0, 'x'), (1, 'x'), (2, 'o')]
            if spot == ' ':
                moves.append(i)
        return moves
    
    def empty_squares(self):
        return " " in self.board
    
    def num_empty_squares(self):
        return len(self.available_moves())
    
    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        # Winner if 3 in a row
        # First let's check the row
        row_ind = square // 3
        row = self.board[row_ind*3 : (row_ind+1)*3]
        if all([spot == letter for spot in row]):
            return True
        
        # Check the column
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True
        

        # Check diagonals 
        if square % 2 == 0:
            diagonal1 = [self.board[i*4] for i in range(3)]
            diagonal2 = [self.board[2+2*i] for i in range(3)] 
            if all([spot == letter for spot in diagonal1]):
                return True
            if all([spot == letter for spot in diagonal2]):
                return True
        
        return False
        


def play(game, x_player, o_player, print_game = True):
    """Returns the winner of the game if there is one. If there isn't return None
    """
    if print_game:
        game.print_board_nums()
    
    letter = "X" # starting letter
    # Iterate while the game still has empty squared
    # (we don't have to worry about the winner because we'll just return that
    # which breaks the loop)
    while game.empty_squares():
        # Get the move from the appropriate player
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)
        
        # Function to make a move
        if game.make_move(square, letter):
            if print_game:
                print(letter + f' makes a move to square: {square}')
                game.print_board()
                print('') # just an empty line

            if game.current_winner:

                if print_game:
                    print(letter + ' wins')
                return letter        
            # After we made our move, we need to alternate letters
        # letter = 'O' if letter == 'X' else 'X'
        if letter == 'X':
            letter = 'O'
        else:
            letter = 'X'
    if print_game:
        print("It's a tie ")

if __name__ == "__main__":
    x_player = GeniusComputerPlayer('X')
    o_player = HumanPlayer('O')
    game = Tic_Tac_Toe()
    play(game, x_player, o_player, print_game= True)


