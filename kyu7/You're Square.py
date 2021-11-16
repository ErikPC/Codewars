#https://www.codewars.com/kata/54c27a33fb7da0db0100040e
def is_square(n):
    resultado = n**(1/2)
    if n < 0:
        return False
    if resultado.is_integer:
        return True
    return False