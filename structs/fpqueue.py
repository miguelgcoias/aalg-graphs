import numpy as np


class FPQueue:

    def __init__(self, source):
        self.vertices = [source]
        self.weights = [0]
        self.preds = [None]
        # Don't know what I want to do about this yet
        self.locators = []
    
    def _hasleft(self, ind):
        return ind * 2 + 1 < len(self.vertices)

    def _hasright(self, ind):
        return ind * 2 + 2 < len(self.vertices)
    
    def _downheapify(self, ind = 0):
        if self._hasleft(ind):
            left = ind * 2 + 1
            minchild = left
            if self._hasright(ind):
                right = ind * 2 + 2
                if self.weights[left] > self.weights[right]:
                    minchild = right
            if self.weights[minchild] < self.weights[ind]:
                # Swap vertices and their weights
                # To do: use locators
                self.vertices[ind], self.vertices[minchild] = self.vertices[minchild], self.vertices[ind]
                self.weights[ind], self.vertices[minchild] = self.weights[minchild], self.weights[ind]
                # Run heapify() on subtree
                self._downheapify(minchild)
    
    def _upheapify(self, ind):
        parent = np.floor((ind - 1) / 2).astype('i4')
        if ind > 0 and self.weights[parent] > self.weights[ind]:
            self.vertices[parent], self.vertices[ind] = self.vertices[ind], self.vertices[parent]
            self.weights[parent], self.weights[ind] = self.weights[ind], self.weights[parent]
            self._upheapify(parent)
    
    def isempty(self):
        return len(self.vertices) == 0

    def insert(self, vertex, weight):
        # To do: implement "bottom-up" construction. Not trivial to do in linear time, but theoretically possible.
        raise NotImplementedError

    def min(self):
        '''Return vertex with minimum weight and its predecessor.'''
        return (self.vertices[0], self.weights[0], self.preds[0])
    
    def pop(self):
        '''Extract and return vertex with minimum weight and its predecessor.'''
        popped = (self.vertices[0], self.weights[0], self.preds[0])
        # To do: implement and use locators
        # Swap last element into root
        self.vertices[0], self.weights[0], self.preds[0] = self.vertices[-1], self.weights[-1], self.preds[-1]
        # Decrease size of all arrays
        self.vertices, self.weights, self.preds = self.vertices[:-1], self.weights[:-1], self.preds[:-1]
        # Run heapify with default argument
        self._downheapify()
        return popped

    def update(self, vertex, weight, pred):
        '''Decrease weight and change predecessor of a vertex.'''
        # To do: implement locators to do this in constant time
        pass
