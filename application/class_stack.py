class Stack:

    def __init__(self):
        self.stack = []

    def is_empty(self):
        if not self.stack:
            return True
        return False

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)
