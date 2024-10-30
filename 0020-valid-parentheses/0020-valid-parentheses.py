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
        for char in s:
            if char not in brackets: #if the bracket is open
                stack.append(char) #simply append it to the stack
            else: #if the bracket is closed
                if stack == [] or brackets[char] != stack[-1]: #if brack is closed but the stack is empty or doesnt equal the last value in the stack
                    return False
                stack.pop() #pop the bracket in the stack

        return stack == []