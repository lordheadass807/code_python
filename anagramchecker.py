
def isAnagram(word1, word2):

    if len(word1) != len(word2):
        return False
    else:
        for character in word1:
            if word1.count(character) != word2.count(character):
                return False

        return True

anagram = isAnagram("anagram", "nagrama")
print(anagram)
