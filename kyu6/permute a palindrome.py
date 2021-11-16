#https://www.codewars.com/kata/58ae6ae22c3aaafc58000079
def permute_a_palindrome(word):
    odd_char_counter = 0
    
    for char in word:
        if word.count(char) % 2 == 0:
            continue
        elif word.count(char) % 2 != 0 and word.count(char) == 1:
            odd_char_counter += 1
            if odd_char_counter == 1:
                continue
            else:
                return False
        else:
            return False
        return True

if __name__ == '__main__':
    assert permute_a_palindrome("a") == True
    assert permute_a_palindrome("aa") == True
    assert permute_a_palindrome("baa") == True
    assert permute_a_palindrome("abc") == False
    assert permute_a_palindrome("baaz") == False
    assert permute_a_palindrome("baabcd") == False
    assert permute_a_palindrome("racecars") == False
    assert permute_a_palindrome("abcdefghba") == False
    assert permute_a_palindrome("") == True