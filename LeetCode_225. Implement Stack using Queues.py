class MyStack:

    def __init__(self):
        self.stack = []
        
    def push(self, x: int) -> None:
        self.stack.append(x)
        
    def pop(self) -> int:
        if len(self.stack) == 0:
            return -1
        else:
            self.end_val = self.stack[len(self.stack) - 1]
            self.stack.remove(self.end_val)
            return self.end_val
        
    def top(self) -> int:
        if len(self.stack) == 0:
            return -1
        else:
            return self.stack[len(self.stack) - 1]
        
    def empty(self) -> bool:
        if len(self.stack) == 0:
            return True
        else:
            return False
