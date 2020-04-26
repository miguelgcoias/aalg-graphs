import numpy as np


class PQueue:

    def __init__(self, source, vertices):
        '''Priority queue using a binary heap. Designed specifically for 
        Dijkstra's algorithm and not adequate for other uses.'''
        self.vertices = np.arange(vertices, dtype='u4')
        self.weights = np.empty(self.vertices.size, dtype='f8')
        self.weights.fill(np.inf)
        self.preds = np.empty(self.vertices.size, dtype='O')
        # Think of a better solution for this
        self.loc = {v: pos for pos, v in enumerate(self.vertices)}
        self.update(source, 0, None)
    
    def _swap(self, indv, indw):
        self.vertices[indv], self.vertices[indw] = self.vertices[indw], \
            self.vertices[indv]
        self.weights[indv], self.weights[indw] = self.weights[indw], \
            self.weights[indv]
        self.loc[self.vertices[indv]], self.loc[self.vertices[indw]] = \
            self.loc[self.vertices[indw]], self.loc[self.vertices[indv]]
        self.preds[indv], self.preds[indw] = self.preds[indw], self.preds[indv]
    
    def _hasleft(self, ind):
        return ind * 2 + 1 < self.vertices.size

    def _hasright(self, ind):
        return ind * 2 + 2 < self.vertices.size
    
    def _downheapify(self, ind = 0):
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
        return self.vertices.size == 0
    
    def pop(self):
        minimum = (self.vertices[0], self.weights[0], self.preds[0])
        self._swap(0, self.vertices.size - 1)
        self.loc.pop(minimum[0])
        self.vertices, self.weights = self.vertices[:-1], self.weights[:-1] 
        self.preds = self.preds[:-1]
        self._downheapify()
        return minimum

    def update(self, vertex, weight, pred):
        pos = self.loc[vertex]
        if weight < self.weights[pos]:
            self.weights[pos] = weight
            if pred is not None:
                self.preds[pos] = [pred]
        else:
            self.preds[pos].append(pred)
        self._upheapify(pos)
    
    def get(self, vertex):
        pos = self.loc[vertex]
        return (self.vertices[pos], self.weights[pos], self.preds[pos])
    
    def exists(self, vertex):
        return vertex in self.loc
