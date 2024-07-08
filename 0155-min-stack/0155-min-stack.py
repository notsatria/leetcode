class MinStack:

    def __init__(self):
        self.items = []
        self.min_items = []
        
    def push(self, val: int) -> None:
        self.items.append(val)
        if self.min_items:
            val = min(self.min_items[-1], val)
        self.min_items.append(val)
        
    def pop(self) -> None:
        self.items.pop()
        self.min_items.pop()

    def top(self) -> int:
        return self.items[-1]

    def getMin(self) -> int:
        return self.min_items[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()