from timeit import Timer

def measure(func, x, n_runs=1, n_repeats=1):
    timer = Timer(lambda: func(x))
    times = timer.repeat(n_repeats, n_runs)
    return min(times)

def plot(x, y, path=None):
    import matplotlib.pyplot as plt
    fig = plt.figure()
    plt.scatter(x, y)

    if path:
        fig.savefig(path)
    else:
        plt.show()
