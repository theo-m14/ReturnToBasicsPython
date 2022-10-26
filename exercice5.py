'''Jeu du morpion'''

game_board = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]


def is_game_finished(game_board):
    '''Premier ligne'''
    if(game_board[0][0] == game_board[0][1] and game_board[0][1] == game_board[0][2] and game_board[0][0] != ' '):
        return game_board[0][1]
    elif(game_board[1][0] == game_board[1][1] and game_board[1][1] == game_board[1][2] and game_board[1][0] != ' '):
        return game_board[1][0]
    elif(game_board[2][0] == game_board[2][1] and game_board[2][1] == game_board[2][2] and game_board[2][0] != ' '):
        return game_board[2][0]
    elif(game_board[0][0] == game_board[1][0] and game_board[1][0] == game_board[2][0] and game_board[0][0] != ' '):
        return game_board[0][0]
    elif(game_board[0][1] == game_board[1][1] and game_board[1][1] == game_board[2][1] and game_board[0][1] != ' '):
        return game_board[0][1]
    elif(game_board[0][2] == game_board[1][2] and game_board[1][2] == game_board[2][2] and game_board[0][2] != ' '):
        return game_board[0][2]
    elif(game_board[0][0] == game_board[1][1] and game_board[1][1] == game_board[2][2] and game_board[0][0] != ' '):
        return game_board[0][0]
    elif(game_board[0][2] == game_board[1][1] and game_board[1][1] == game_board[2][0] and game_board[0][2] != ' '):
        return game_board[0][2]
    else:
        return -1

    
def display_game_board(game_board):
    for line in game_board:
        print(line)
    
    
player = 2
round = 1    

display_game_board(game_board)

while is_game_finished(game_board) == -1 and round != 9:

    '''On change le joueur en cours au debut pour ensuite retrouver le gagnant plus facilement'''
    if player == 1:
        player = 2
    else:
        player = 1    

    print(f"Joueur {player} choisis la colonne où jouer: (Entre 1 et 3)")
    column = int(input())
    while column < 1 or column > 3:
        print("Seulement entre 1 et 3 : resaisis ta colonne :")
        column = int(input())
    print(f"Joueur {player} choisis maintenant la ligne :")
    line = int(input())
    while line < 1 or line > 3:
        print("Seulement entre 1 et 3 : resaisis ta line :")
        line = int(input())
    
    '''On inscrit le choix du joueur dans le jeu'''
    
    if player == 1:
        game_board[line-1][column-1] = 'O'
    else:
        game_board[line-1][column-1] = 'X'

    display_game_board(game_board)
    round += 1


if round == 9:
    print('Egalité !')
else:
    print(f'Le joueur {player} a gagné ')    