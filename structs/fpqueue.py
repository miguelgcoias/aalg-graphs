import numpy as np


class FPQueue:

    def __init__(self, source, neighbours, weights):
        '''Initialize FPQueue with source vertex and its neighbours.
        
        Keyword arguments:
        source - source vertex
        neighbours - list of'''
        self.vertices = [source] + neighbours
        self.weights = [0] + weights
        self.preds = [None] + [source for v in neighbours]
        self.locators = {v: pos for pos, v in enumerate(self.vertices)}
        self._insheapify()
    
    def _swap(self, v, w):
        '''Swap positions of two vertices.'''
        self.vertices[v], self.vertices[w] = self.vertices[w], self.vertices[v]
        self.weights[v], self.weights[w] = self.weights[w], self.weights[v]
        self.locators[self.vertices[v]], self.locators[self.vertices[w]] = self.locators[self.vertices[w]], self.locators[self.vertices[v]]
        self.preds[v], self.preds[w] = self.preds[w], self.preds[v]
    
    def _hasleft(self, ind):
        return ind * 2 + 1 < len(self.vertices)

    def _hasright(self, ind):
        return ind * 2 + 2 < len(self.vertices)

    def _insheapify(self):
        '''Heapify from a provided initial list of vertices.'''
        start = np.floor((len(self.vertices) - 1) / 2).astype('i4')
        for v in range(start, -1, -1):
            self._downheapify(v)
    
    def _downheapify(self, ind = 0):
        '''Heapify downwards, starting from ind.'''
        if self._hasleft(ind):
            left = ind * 2 + 1
            minchild = left
            if self._hasright(ind):
                right = ind * 2 + 2
                if self.weights[left] > self.weights[right]:
                    minchild = right
            if self.weights[ind] > self.weights[minchild]:
                self._swap(ind, minchild)
                self._downheapify(minchild)
    
    def _upheapify(self, ind):
        parent = np.floor((ind - 1) / 2).astype('i4')
        if ind > 0 and self.weights[parent] > self.weights[ind]:
            self._swap(ind, parent)
            self._upheapify(parent)
    
    def isempty(self):
        return len(self.vertices) == 0

    def insert(self, vertices, weights, pred):
        for k in range(len(vertices)):
            self.vertices.append(vertices[k])
            self.weights.append(weights[k])
            self.preds.append(pred)
            self.locators[vertices[k]] = len(self.vertices) - 1
            self._upheapify(len(self.vertices) - 1)        

    def min(self):
        '''Return vertex with minimum weight and its predecessor.'''
        return (self.vertices[0], self.weights[0], self.preds[0])
    
    def pop(self):
        '''Extract and return vertex with minimum weight and its predecessor.'''
        minimum = (self.vertices[0], self.weights[0], self.preds[0])
        self._swap(0, len(self.vertices) - 1)
        self.locators.pop(minimum[0])
        self.vertices, self.weights, self.preds = self.vertices[:-1], self.weights[:-1], self.preds[:-1]
        self._downheapify()
        return minimum

    def update(self, vertex, weight, pred):
        '''Decrease weight and change predecessor of a vertex.'''
        pos = self.locators[vertex]
        self.weights[pos], self.preds[pos] = weight, pred
        self._downheapify(pos)
