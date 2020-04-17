import numpy as np

def dependency(outpaths, sigma, v):
    '''Recursive dependency function, as defined in U. Brandes' paper 'A Faster 
    Algorithm for Betweenness Centrality' (2001).'''
    if outpaths.neighbours(v)[0].size == 0:
        return 0
    else:
        sumdep = 0
        for w in outpaths.neighbours(v)[0]:
            sumdep += sigma[v] / sigma[w] * (1 + dependency(outpaths, sigma, w))
        return sumdep