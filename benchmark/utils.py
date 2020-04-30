from timeit import Timer

def measure(func, x, n_runs=1, n_repeats=1):
    timer = Timer(lambda: func(x))
    times = timer.repeat(n_repeats, n_runs)
    return min(times)

def plot(x, y, args={}):
    import matplotlib.pyplot as plt
    fig = plt.figure()
    plt.scatter(x, y)

    if 'ylabel' in args:
        plt.ylabel(args['ylabel'])

    if 'xlabel' in args:
        plt.xlabel(args['xlabel'])

    if 'path' in args:
        fig.savefig(args['path'])
    else:
        plt.show()
