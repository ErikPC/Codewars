#https://www.codewars.com/kata/54b42f9314d9229fd6000d9c

# Primera solución 
def duplicate_encode(word):
    word = word.lower()
    Complete_string = ''
    for character in word:
        if word.count(character) != 1:
            Complete_string += ")"
        else:
            Complete_string += "("
    print(Complete_string)
    return Complete_string
# Segunda solución usando diccionarios
# def duplicate_encode(word):
#     word_lower=word.lower()
#     texto=''
#     diccionario_letras={}
#     for letra in word_lower:
#         diccionario_letras[letra] = word.count(letra)
#         if diccionario_letras[letra] != 1:
#             texto += ')'
#         else:
#             texto += '('
#     return texto


    
# Casos test
if __name__=='__main__':
    assert duplicate_encode("din") == "((("
    assert duplicate_encode("recede") == "()()()"
    assert duplicate_encode("Success") == ")())())","should ignore case"
    assert duplicate_encode("(( @") == "))(("