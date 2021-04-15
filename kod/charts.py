import matplotlib.pyplot as plt
import numpy as np

def gen_chart(fun_og, fun_inter, node, a, b, filename):
    # wczyczyść figurę
    plt.clf()

    # narysuj oś x
    plt.axhline(0, color='black')

    # start i end wykraczają o 10% poza max min node'a
    length = 0 #abs(b-a) * 0.2 # 1e4
    start = a - length
    end = b + length


    x = np.arange(start, end, 0.01)
    # narysuj funkcje
    plt.plot(x, fun_og(x), "b-", label="funkcja oryginalna")
    plt.plot(x, fun_inter(x), "g-", label="funkcja interpolowa")

    # narysuj węzły
    plt.plot(node[0], node[1], "ro", label="węzły")
    
    # narysuj legendę
    plt.legend(loc="upper right")

    # zapisz
    plt.savefig(filename)