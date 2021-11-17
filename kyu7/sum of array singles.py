#https://www.codewars.com/kata/59f11118a5e129e591000134

def repeats(arr):
    repeat = 0
    for number in arr:
        if arr.count(number) == 1:
            repeat += number
    return repeat