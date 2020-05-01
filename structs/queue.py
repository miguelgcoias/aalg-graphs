class Queue:

    def __init__(self):
        self.contents = list()
    
    def enqueue(self, v):
        self.contents.append(v)
    
    def dequeue(self):
        return self.contents.pop(0)
    
    def first(self):
        return self.contents[0]

    def isempty(self):
        return len(self.contents) == 0