def quicksort(xs):
    if xs:
        pivot = xs[0]
        below = [i for i in xs[1:] if i < pivot]
        above = [i for i in xs[1:] if i >= pivot]
        return quicksort(below) + [pivot] + quicksort(above)
    else:
        return xs
