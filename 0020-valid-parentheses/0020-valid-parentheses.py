class Solution:
    def isValid(self, s: str) -> bool:
        #when it comes to stacking, it uses a last in, first out
        #we push the next value at the end (to insert)
        #we pop the last value at the end (to remove)
        
        #we need to make a separate array
        #so we can PUSH to a new array
        #and if the next value is a closing bracket
        #we will pop the open bracket in the new array
        #we can check if the corresponding closing bracket is equal to the open

        #answer = []
        #for char in s:
            #if char is NOT a closing bracket
                #answer.append(char)
            #if char IS a closing bracket
                #check if opening bracket matches the closing bracket #use dict
                #answer.pop()
            
        #return answer == []
        #this is for checking the closing bracket is matching with the open bracket 
        matchClosingWithOpen = { 
            '}' : '{',
            ']' : '[',
            ')' : '('
        }
        answer = []
        
        # if len(s) == 1:
        #     return False

        for char in s:
            if char not in matchClosingWithOpen.keys():
                answer.append(char)
            else:
                if answer == []: #what if first char is a closing bracket? return False  
                    return False
                if answer[-1] == matchClosingWithOpen[char]: #if last character in answerArr == val of char...
                    answer.pop()
        return answer == []
