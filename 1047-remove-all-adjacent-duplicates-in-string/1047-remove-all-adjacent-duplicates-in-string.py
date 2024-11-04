class Solution:
    def removeDuplicates(self, s: str) -> str:
        #we can loop until there is no duplicates
        #if there is a duplicate, pop it, and, go back to the beginning of s 
        #OR WE CAN USE A STACK, LAST IN, BUT FIRST OUT
        #we have to back track, or go back to check the previous iteration before making a choice
        #we check the FIRST letter, then compare it to the SECOND letter
        #if both letters are equal, pop it
        #return stack
        stack = []
        for i in range(len(s)):
            if stack and stack[-1] == s[i]: #if the last letter of the stack is the same as the next iteration
                stack.pop()
            else: #else if they do not equal
                stack.append(s[i])
        return "".join(stack)