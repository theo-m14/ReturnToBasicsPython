'''Algorithme de recherche dichotomique'''

tableau = [ 1, 1, 2, 3, 5, 8, 13, 21, 34 ]


def search_index(array, x):
    start = 0
    end = len(array) - 1

    while start <= end:
        middle = (end + start) // 2

        if(array[middle] == x):
            return middle
        elif(array[middle] < x ):
            start = middle + 1
        else:
            end = middle - 1

    return -1


print(f"Le chiffre recherché (21) se trouve à l'index {search_index(tableau,21)}")