class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        #if indice is a number that leads with a zero
        #   return false
        #else if its just an indice that is a number
        #   we will check the len of the str that the number claims to be
        #if indice is a letter and number is not none
        #   continue
        #if it is equal to the length
        #   return true

        #we can check the length
        original = len(word)
        counter = 0
        number = ''
        
        for s in abbr:
            if s.isdigit():

                if number is '' and s == '0': #if it is a trailing 0
                    return False
                number += s #add the ints as a str
            elif s.isalpha():
                if number is not '': #as long as it is not empty
                        counter += int(number)
                        number = ''
                
                #we should check is abbr str matches with the original
                if counter >= original or word[counter] != s: #if the indices doesnt match up
                    return False
                counter += 1
        if number:
            counter += int(number)
        return original == counter
