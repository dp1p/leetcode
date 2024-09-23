class MinStack:

    def __init__(self):
        self.stack = [] #even though we instaniated the class, we need to create a new variable

    def push(self, val: int) -> None:
        self.stack.append(val) #we want to push to our stack, so we do class name

    def pop(self) -> None:
        self.stack.pop() #we want to pop 

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return min(self.stack)

    def __repr__(self) -> str: 
        return f"Arr Stack {self.stack}"

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()