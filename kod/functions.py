from numpy import sin, cos

def cot(x):
    return 1/tan(x)

def csc(x):
    return 1/sin(x)

#####
def f0(x):
    # policzenie schematem hornera
    # 3*x^5 - 5*x^4 + 1.2*x^3 + 5x^2 + 10x - 1
    coefficients = [3, -5, 1.2, 5, 10, -1]
    result = coefficients[0]
    for i in range(1, 6):
        result = result*x + coefficients[i]
    return result
#####

#---#
def f1(x):
    result = 2 * x + 5
    return result
#---#

#####
def f2(x):
    result = abs(x)
    return result
#####

#---#
def f3(x):
    result = sin(x)
    return result
#---#

#####
def f4(x):
    result = sin(2 * x + 5)
    return result
#####

#---#
def f5(x): 
    result = abs((x - cos(x)) * (x + cos(x)))
    return result
#---#

'''
0. wielomian (horner)
1. liniowa
2. |x|
3. trygonometryczna
4. złożenie
5. złożenie
'''

functions = [
    # 0:
    ["3*x⁵ - 5*x⁴ + 1.2*x³ + 5x² + 10x - 1", f0],
    # 1:
    ["2x + 5", f1],
    # 2:
    ["|x|", f2],
    # 3:
    ["sin(x)", f3],
    # 4:
    ["sin(2x + 5)", f4],
    # 5:
    ["|x²-cos²(x)|", f5]
]

def print_fun():
    for i in range(len(functions)):
        print(str(i) + ". " + functions[i][0])
    i = int(input("Wybierz funkcję: "))
    return functions[i][0],functions[i][1]