class Stack:

    def __init__(self):
        self.contents = list()
    
    def push(self, v):
        self.contents.append(v)

    def pop(self):
        return self.contents.pop(-1)
    
    def isempty(self):
        return len(self.contents) == 0
