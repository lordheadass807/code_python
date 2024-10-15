def stringcleaner(text):
    '''cleans a string, makes everything lowercase and removes non alphabet characters
  
  Args:
  Text is a string

  returns:
  clean string

  '''

 #intiliazes a string 

    result = ' '
    for character in text:
        #is.alpha() checks if character is a letter
        if character.isalpha():
            #if it is a letter, it adds the lowercase version to return
            result += character.lower()

    return result


value = stringcleaner('HELL0 W0RLD')

print(f"{value}")