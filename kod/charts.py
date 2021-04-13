import matplotlib.pyplot as plt
import numpy as np

def gen_chart(fun_og, fun_inter, node):

    plt.axhline(0, color='black')

    plt.plot(node[0], node[1], "ro", label="węzły")

    x = np.arange(node[0][0]-1, node[0][len(node[0])-1]+1, 0.01)
    plt.plot(x, fun_og(x), "b-", label="funkcja oryginalna")
    plt.plot(x, fun_inter(x), "g-", label="funkcja interpolowa")

    plt.legend(loc="upper right")

    plt.show()