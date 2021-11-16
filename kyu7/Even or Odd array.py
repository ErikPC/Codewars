#https://www.codewars.com/kata/5949481f86420f59480000e7
#Given a list of integers, determine whether the sum of its elements is odd or even.
# Give your answer as a string matching "odd" or "even".

def odd_or_even(arr):
    total = sum(arr)
    if total % 2 ==0:
        return "even"
    return "odd"