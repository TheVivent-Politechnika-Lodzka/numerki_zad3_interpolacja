import random
import numpy as np

def gen_random(a, b, amount):
    # generowanie nierównych odstepów argumentów
    nodes = []
    while len(nodes) != amount:
        # dopóki ilość punktów wygenerowanych jest różna
        # od żądanej wartości losuj kolejne punkty
        x = round(random.uniform(a, b), 2)
        if not x in nodes:
            nodes.append(x)
    nodes.sort()
    return np.array(nodes)

def gen_equidistant(a, b, amount):
    # generowanie węzłów równoodległych
    return np.linspace(a, b, amount)