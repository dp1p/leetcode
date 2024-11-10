class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        answer = 0
        if len(tokens) == 1:
            return int(tokens[0])
        for value in tokens:
            if len(value) > 1 or value.isdigit(): #len(value) > 2 bc if it is a negative number it will skip
                #print(f"{value} its a number")
                stack.append(int(value))
                #print(stack)
            else:
                #print(f"{value} is not a digit, we will go straight to divison")
                if value == "+":
                    num1 = stack.pop()
                    num2 = stack.pop()
                    answer = (num1) + (num2)
                    #print(f"{num1} + {num2} = {answer}")
                    stack.append(int(answer)) #to prevent decimals
                elif value == "*":
                    num1 = stack.pop()
                    num2 = stack.pop()
                    answer = (num1) * (num2)
                    stack.append(int(answer))
                    #print(f"{num2} * {num1} = {answer}")
                elif value == "/":
                    num1 = stack.pop()
                    num2 = stack.pop()
                    answer = (num2) / (num1)
                    stack.append(int(answer))
                    #print(f"{num2} / {num1} = {answer}")
                elif value == "-":
                    num1 = stack.pop()
                    num2 = stack.pop()
                    answer = (num2) - (num1)
                    stack.append(int(answer))
                    #print(f"{num2} - {num1} = {answer}")
                    
        return int(answer)