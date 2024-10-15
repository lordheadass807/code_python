
def is_palindrome(text):
    '''
    Checks if a text is a palindrome

    Arg: text is a string

    returns a boolean value, true if palindrome fasle if otherwise

    '''

    #splices the text, checks if the text is equal to it backwards
    
    return text == text[::-1]

print(is_palindrome('tacocat'))