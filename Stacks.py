class Stacks:
    def __init__(self):
        self.item = []

    def push(self, value):
        self.item.append(value)

    def pop(self):
        if len(self.item) != 0:
            return self.item.pop()
        else:
            return("Stack is empty!!")
    def peek(self):
        if len(self.item) != 0:
            return self.item[-1]
        else:
            return("Stack is empty!!")
    def is_empty(self):
        if len(self.item) != 0:
            return False
        else:
            return True
    def size(self):
        return len(self.item)



