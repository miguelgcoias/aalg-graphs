from json import dump


def konect(path, n, dump_path=None):
    '''Quick and dirty script to parse unweighted edge lists from KONECT. 
    Every vertex v from the graph is mapped to v - 1 on the returned 
    dictionary, since in our implementation vertex numbering starts at 0.
    
    Keyword arguments:
    path -- path to file downloaded from KONECT
    n -- number of vertices
    dump_path -- optional parameter; if a valid path is provided, the function  
    will write the contents of the dictionary to a JSON file.'''
    graph_dict = {v: [] for v in range(n)}

    with open(path) as data:
        for line in data:
            if line[0] == '%':
                continue
            else:
                start, end = line.split()
                graph_dict[int(start) - 1].append(int(end) - 1)
                graph_dict[int(end) - 1].append(int(start) - 1)
    
    if dump_path is not None:
        with open(dump_path, 'w') as json_file:
            dump(graph_dict, json_file, indent=2)
    
    return graph_dict
