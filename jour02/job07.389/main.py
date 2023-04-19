class Board:
    def __init__(self, i, j):
        self.board = [['O' for _ in range(j)] for _ in range(i)]
        self.i = i
        self.j = j
    
    def play(self, column, color):
        row = self.i - 1
        while row >= 0 and self.board[row][column-1] != 'O':
            row -= 1
        if row >= 0:
            self.board[row][column-1] = color
        else:
            print("La colonne est pleine.")
    
    def print_board(self):
        for row in range(self.i):
            for column in range(self.j):
                print(self.board[row][column], end=' ')
            print()
        print()
        

def play_game():
    i = int(input("Entrez le nombre de rangées : "))
    j = int(input("Entrez le nombre de colonnes : "))
    board = Board(i, j)
    player1 = "J"
    player2 = "R"
    turn = 1
    while True:
        board.print_board()
        if turn % 2 == 1:
            print("C'est au tour du joueur 1 (jaune) :")
            column = int(input("Entrez le numéro de la colonne où vous voulez placer votre jeton : "))
            board.play(column, player1)
            if check_win(board.board, player1):
                print("Le joueur 1 (jaune) a gagné !")
                break
        else:
            print("C'est au tour du joueur 2 (rouge) :")
            column = int(input("Entrez le numéro de la colonne où vous voulez placer votre jeton : "))
            board.play(column, player2)
            if check_win(board.board, player2):
                print("Le joueur 2 (rouge) a gagné !")
                break
        turn += 1


def check_win(board, color):
    # Vérification des lignes
    for row in range(len(board)):
        for column in range(len(board[row])-3):
            if board[row][column] == color and board[row][column+1] == color and board[row][column+2] == color and board[row][column+3] == color:
                return True
    
    # Vérification des colonnes
    for row in range(len(board)-3):
        for column in range(len(board[row])):
            if board[row][column] == color and board[row+1][column] == color and board[row+2][column] == color and board[row+3][column] == color:
                return True
    
    # Vérification des diagonales haut-gauche vers bas-droite
    for row in range(len(board)-3):
        for column in range(len(board[row])-3):
            if board[row][column] == color and board[row+1][column+1] == color and board[row+2][column+2] == color and board[row+3][column+3] == color:
                return True
    
    # Vérification des diagonales bas-gauche vers haut-droite
    for row in range(3, len(board)):
        for column in range(len(board[row])-3):
            if board[row][column] == color and board[row-1][column+1] == color and board[row-2][column+2] == color and board[row-3][column+3] == color:
                return True
    
    return False


game = Board(4,5)
game.play(1,'J')
game.print_board()
