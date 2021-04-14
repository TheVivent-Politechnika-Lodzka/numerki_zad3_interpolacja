import numpy as np

class STinterpol:

    coef = []
    node_x = []
    node_y = []

    def __init__(self, node):
        self.node_x = node[0]
        self.node_y = node[1]
        self.coef = self.__calc_coefficients()


    def __calc_coefficients(self):
        
        x = self.node_x
        y = self.node_y
        n = len(y)

        coef = np.zeros([n,n])
        # pierwsza kolumna, to y
        coef[:, 0] = y

        for j in range(1,n):
            for i in range(n-j):
                coef[i][j] = (coef[i+1][j-1] - coef[i][j-1]) / (x[i+j] - x[i])            

        # zwróć pierwszy wiersz
        # (właściwe współczynniki)
        return coef[0]

    def getCoef(self):
        result = ""
        for coef in self.coef:
            result += "{}, ".format(round(coef, 3))
        return result

    def getY(self, x):

        i = len(self.node_x)
        result = self.coef[i-1]
        
        for j in range(1, i):
            result = self.coef[i-j-1] + (x - self.node_x[i-j-1]) * result
        
        return result


import numpy as np


class EQinterpol:

    coef = []
    node_x = []
    node_y = []
    h = 0

    def __init__(self, node):
        self.node_x = node[0]
        self.node_y = node[1]
        self.h      = abs(self.node_x[1] - self.node_x[0])
        self.coef   = self.__calc_coefficients()


    def __getT(self, x):
        return (x - self.node_x[0])/self.h


    def __calc_coefficients(self):
        
        x = self.node_x
        y = self.node_y
        n = len(y)

        pascal_triangle = np.zeros([n,n])
        pascal_triangle[:, 0] = 1
        np.fill_diagonal(pascal_triangle, 1)
        
        # tworzenie trójkąta Pascala
        for i in range(2, n):
            for j in range(1, i+1):
                pascal_triangle[i][j] = pascal_triangle[i-1][j-1] + pascal_triangle[i-1][j]

        # obliczenie współczynników
        coef = []
        coef.append(y[0])
        strong = 1
        for k in range(1, n):
            total = 0
            for i in range(k+1):
                tmp = y[i]*pascal_triangle[k][i]
                if (k-i) % 2 == 1: tmp*=-1
                total += tmp
            coef.append(total/strong)
            strong *= k+1

        return coef

    def getCoef(self):
        result = ""
        for coef in self.coef:
            result += "{}, ".format(round(coef, 3))
        return result

    def getY(self, x):

        result = 0
        for i in range(len(self.node_x)):
            tmp = self.coef[i]
            for j in range(i):
                tmp *= self.__getT(x) - j
            result += tmp
        
        return result