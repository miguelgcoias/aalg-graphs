class Stack:

    def __init__(self):
        self.contents = list()
    
    def push(self, v):
        self.contents.append(v)

    def pop(self):
        head = self.contents[-1]
        self.contents = self.contents[:-1]
        return head
    
    def isempty(self):
        return len(self.contents) == 0
