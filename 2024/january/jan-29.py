class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    # need to keep the LAST element in the stack here 
    def push(self, x: int) -> None:
        while self.stack1: 
            self.stack2 = [self.stack1.pop(0)] + self.stack2

        self.stack1.append(x)
        while self.stack2: 
            self.stack1 = [self.stack2.pop(0)] + self.stack1

    def pop(self) -> int:
        return self.stack1.pop(0)

    def peek(self) -> int:
        return self.stack1[0]

    def empty(self) -> bool:
        return self.stack1 == []


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()