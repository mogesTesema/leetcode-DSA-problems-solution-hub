class MyQueue:

    def __init__(self):
        self.stack_one = []
        self.stack_two = []
        

    def push(self, x: int) -> None:
        while self.stack_two:
            self.stack_one.append(self.stack_two.pop())
        self.stack_one.append(x)

    def pop(self) -> int:

        while self.stack_one:
            self.stack_two.append(self.stack_one.pop())
        return self.stack_two.pop()
        

    def peek(self) -> int:
        while self.stack_one:
            self.stack_two.append(self.stack_one.pop())
        return self.stack_two[-1]
        

    def empty(self) -> bool:
        if self.stack_one or self.stack_two:
            return False
        else:
            return True
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
