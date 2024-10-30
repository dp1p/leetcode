class Solution:
    def isValid(self, s: str) -> bool:
        #this is a stack problem because we care about the order and placement
        #we will store the brackets in a separate arr
        #stacks are last in, first out

        stack = []

        #then we will make a hashmap so we know which bracket goes to which
        brackets = {
            '}' : '{',
            ')' : '(',
            ']' : '['
        }
        #we make the closing bracket the key because we only care when it is closed to check the value of it
        for i in range(len(s)):
            if s[i] not in brackets: #if the bracket is open
                stack.append(s[i]) #simply append it to the stack
            else: #if the bracket is closed
                if stack == []: #if the bracket is closed and the stack is empty
                    return False
                elif brackets[s[i]] == stack[-1]: #if the value of (closed bracket) is the last of the stack
                    stack.pop() #pop the bracket in the stack
                else:
                    return False

        return stack == []