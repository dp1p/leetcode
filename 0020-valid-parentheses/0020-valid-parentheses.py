class Solution:
    def isValid(self, s: str) -> bool:
        #STACKING! LIFO (last in, first out)
        #we will make a empty arr called stack
        #we will iterate thru s till the very end, and append the char from s in it
        #if char is open
            #stack.append(s)
        #if char is closed (matches in our dict)
            #if stack[-1] = closeToOpen[char] #we check if stack[-1] is open, and find if it is equal to the value of the closing bracket, which is why we make the opening as a value, and closing bracket as a key
                #stack.pop()
                #NOTE WE NEVER APPEND THE CLOSING BRACKET, IT WILL ALWAYS BE OPEN BRACKETS IN THE STACK

        closeToOpen = {
            ')' : '(',   
            '}' : '{',
            ']' : '['
        }
        stack = [] #LAST IN, FIRST OUT 
        for char in s:
            if char in closeToOpen: #if the character is a closing bracket
                if closeToOpen[char] == stack[-1]: #if the value of ']' is equal to the first char of the stack (which should be an open)
                    stack.pop()
                else:
                    return False
            else: #if character is a open bracket
                stack.append(char)

        return len(stack) == 0 







        #each bracket must be closed
        #if there is '(' there must be a ')', else false, vice versa
        #IMPORTANT
        #left brackets must always be first '(', else false
        
        #convert s to a list
        #store our chars in a hashmap, so if there is our value in there, skip
        #else do stuff

        #1. determine if a bracket has a closing
        #two pointer method
        #pointer1 = 0
        
        #for pointer1 in s
            #for pointer2 in range(pointer1, len(s)):
                #if char = '('
                    #find ')'
                        #if found
                        #s.pop(char)
                #elif char = ')'
                    #return false
                #elif char = '['
                    #find ')'
                        #if found
                        #s.pop(char)
                        #...
        # s = list(s) #will make mutable
        # print(s)
        # for pointer1 in range(len(s)):
        #     print(f'CHARACTER IS {pointer1}, find the closing bracket ---------')
        #     for pointer2 in range(pointer1, len(s)):
        #         print(f'character: {s[pointer2]}')
        #         if s[pointer1] == '(':
        #             if s.index(')') == True:
        #                 s.pop(pointer1)
        #                 s.pop(s.index(')'))
        #             else:
        #                 return False
        # if s == []:
        #     return True
        # else:
        #     return False



