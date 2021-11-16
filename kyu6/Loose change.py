#https://www.codewars.com/kata/loose-change
def loose_change(cents):
    PENNIES = 1 
    NICKLES = 5
    DIMES = 10
    QUARTES = 25
    valores_monedas = [QUARTES, DIMES, NICKLES, PENNIES]
    monedero = {'Quarters': 0,  'Dimes': 0, 'Nickels': 0, 'Pennies': 0}
    #monedero.key en este caso el bucle hace que pase por las key que hay en el monedero.
    for (index, moneda) in enumerate(monedero.keys()):
        #por cada nombre de moneda en el monedero cogemos el nombre de moneda como moneda y el index  commo index
        #Le resta a al dinero los valores que estan en una lista.
        while cents - valores_monedas[index] >= 0:
            monedero[moneda] += 1
            #Sumamos al diccionario 1 por cada moneda usada 
            cents -= valores_monedas[index]
            #restamos a cents el valor para saber cuando hay que dejar de restar.
    return dict(reversed(list(monedero.items())))
# devuelve al revés el diccionario, que en este caso da igual.

if __name__ == '__main__':
    assert loose_change(29) == {'Nickels': 0, 'Pennies': 4, 'Dimes': 0, 'Quarters': 1}
    assert (loose_change(91),  {'Nickels': 1, 'Pennies': 1, 'Dimes': 1, 'Quarters': 3})
    assert (loose_change(0),   {'Nickels': 0, 'Pennies': 0, 'Dimes': 0, 'Quarters': 0})
    assert (loose_change(-2),  {'Nickels': 0, 'Pennies': 0, 'Dimes': 0, 'Quarters': 0})
    assert (loose_change(3.9), {'Nickels': 0, 'Pennies': 3, 'Dimes': 0, 'Quarters': 0})