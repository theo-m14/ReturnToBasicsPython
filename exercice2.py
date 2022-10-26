from random import randint

bot_points = 0
user_points = 0
choice_tab = ['Pierre', 'Feuille', 'Ciseaux']

print('Bienvenue dans le jeu du pierre feuille ciseau')

print('Choissisez le nombre de point gagnant :')

'''On demande le nombre de point gagant'''
win_point = 0
win_point = int(input())

while win_point <= 0:
    print('Veuillez choisir un nombre de points positif :')
    win_point = int(input())

    '''On définit les conditions de victoire d'une manche'''
def who_win(user_choice : int, bot_choice : int):
    if user_choice == bot_choice :
        return 'Equality'
    elif user_choice == 1 and bot_choice == 2:
        return 'BotWin'
    elif user_choice == 1 and bot_choice == 3:
        return 'UserWin'
    elif user_choice == 2 and bot_choice == 1:
        return 'UserWin'
    elif user_choice == 2 and bot_choice == 3:
        return 'BotWin'
    elif user_choice == 3 and bot_choice == 1:
        return 'BotWin'
    elif user_choice == 3 and bot_choice == 2:
        return 'UserWin'

'''On boucle tant que on a pas atteinds le nombre de point gagnant'''
while bot_points != win_point and user_points != win_point:
    print('Veuillez choisir votre coup :')
    print('Pierre = 1 / Feuille = 2 / Ciseaux = 3')

    user_choice = int(input())

    while user_choice < 1 and user_choice > 3:
        print('Veuillez saisir un nombre de coup valide :')
        print('Pierre = 1 / Feuille = 2 / Ciseaux = 3')
        user_choice = int(input())

    bot_choice = randint(1,3)
    print(f"L'ordinateur choisis {choice_tab[bot_choice-1]}")

    if who_win(user_choice,bot_choice) == 'UserWin':
        user_points += 1
        print('Gagnant de cette manche : Vous')
    elif who_win(user_choice,bot_choice) == 'BotWin':
        bot_points += 1
        print('Gagnant de cette manche : Ordinateur')

    print(f'Score -> Vous : {user_points} Ordinateur : {bot_points}')

print('Fin de Partie !')

if user_points == win_point:
    winner = 'Vous'
else:
    winner = "L'ordinateur"

print(f'Le gagnant est {winner}')
print(f'Score -> Vous : {user_points} Ordinateur : {bot_points}')