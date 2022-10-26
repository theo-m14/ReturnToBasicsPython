'''Jeu du juste prix'''

from random import randint, random

random_number = randint(1, 20)
user_number = 0
number_of_try = 0

print("Veuillez saisir un nombre entre 0 et 20:")

while random_number != user_number:
    user_number = int(input())
    number_of_try = number_of_try + 1
    if user_number < random_number:
        print("C'est plus ! Entrez un nouveau nombre :")
    elif user_number > random_number:
        print("C'est moins ! Entrez un nouveau nombre :")

print(f'Vous avez réussi ! En {number_of_try} tentatives')