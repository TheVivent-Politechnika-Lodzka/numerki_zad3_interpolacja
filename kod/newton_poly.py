import numpy as np

class standard_interpolation:

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


    def getY(self, x):

        i = len(self.node_x)
        result = self.coef[i-1]
        
        for j in range(1, i):
            result = self.coef[i-j-1] + (x - self.node_x[i-j-1]) * result
        
        return result


import numpy as np

class equidistant_interpolation:

    coef = []
    node_x = []
    node_y = []
    h = 0

    def __init__(self, node, h):
        self.h      = h
        self.node_x = node[0]
        self.node_y = node[1]
        self.coef   = self.__calc_coefficients()


    def __calc_coefficients(self):
        
        x = self.node_x
        y = self.node_y
        n = len(y)

        facs = np.zeros([n,n])
        facs[0][0] = 1


                        # coef = np.zeros([n,n])
                        # # pierwsza kolumna, to y
                        # coef[:, 0] = y

                        # for j in range(1,n):
                        #     for i in range(n-j):
                        #         coef[i][j] = (coef[i+1][j-1] - coef[i][j-1]) / self.h * i

        # zwróć pierwszy wiersz
        # (właściwe współczynniki)
        return coef[0]


    def getY(self, x):

        i = len(self.node_x)
        result = self.coef[i-1]
        
        for j in range(1, i):
            result = self.coef[i-j-1] + (x - self.node_x[i-j-1]) * result
        
        return result