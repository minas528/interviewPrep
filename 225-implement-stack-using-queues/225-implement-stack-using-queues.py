class MyStack:

    def __init__(self):
        self.poped = []
        self.pushed = []       

    def push(self, x: int) -> None:
        self.pushed.append(x)
        

    def pop(self) -> int:
        if not self.poped:
            while self.pushed:
                self.poped.insert(0,self.pushed.pop())
        val = self.poped.pop()
        self.pushed = self.poped
        self.poped = []
        return val
        
    def top(self) -> int:
        if not self.poped:
            while self.pushed:
                self.poped.insert(0,self.pushed.pop())
        val = self.poped[-1]
        self.pushed = self.poped
        self.poped = []
        return val
        

    def empty(self) -> bool:
        return not self.pushed and not self.poped
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()