'''Générateur de nombre de la suite Fibonaci'''


number_tab = [0,1]

print('Saissisez le nombre souhaitez :')

number_request = int(input())


def fibonnaci(last_number, current_number, number_request):
    number_tab.append(last_number + current_number)
    if(len(number_tab) == number_request):
        string_to_print = f'Voici les {number_request} premiers nombres de la suite Fibonnacci : '
        for number in number_tab:
            string_to_print = string_to_print + str(number) + ' '
        print(string_to_print)
    else:
        fibonnaci(number_tab[len(number_tab)-2], number_tab[len(number_tab)-1], number_request)

    
fibonnaci(0,1, number_request)

