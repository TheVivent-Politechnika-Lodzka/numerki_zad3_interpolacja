import matplotlib.pyplot as plt
import numpy as np

def gen_chart(fun_og, fun_inter, node, filename):
    plt.clf()

    plt.axhline(0, color='black')


    length = abs(node[0][len(node[0])-1] - node[0][0]) * 0.1
    start = node[0][0] - length
    end = node[0][len(node[0])-1] + length


    x = np.arange(start, end, 0.01)
    plt.plot(x, fun_og(x), "b-", label="funkcja oryginalna")
    plt.plot(x, fun_inter(x), "g-", label="funkcja interpolowa")



    plt.plot(node[0], node[1], "ro", label="węzły")
    plt.legend(loc="upper right")

    plt.savefig(filename)