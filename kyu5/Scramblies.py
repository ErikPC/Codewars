#https://www.codewars.com/kata/55c04b4cc56a697bb0000048
def scramble(s1, s2):
    for letra in set(s2):
        if s1.count(letra) < s2.count(letra):
            return False
    return True