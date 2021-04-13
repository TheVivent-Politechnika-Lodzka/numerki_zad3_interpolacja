from functions import print_fun
import points_gen as pg
from newton_poly import standard_interpolation
from newton_poly import equidistant_interpolation
from charts import gen_chart
import numpy as np

fun_name, fun_ptr = print_fun()

a = int(input("Podaj lewą stronę przedziału: "))
b = int(input("Podaj prawą stronę przedziału: "))

if a > b: a,b = b,a

points = []
for x in pg.gen_random(a, b, 8):
    points.append([x, fun_ptr(x)])
points = np.array(points).transpose()

interpol = equidistant_interpolation(points, (b-a)/8)

gen_chart(fun_ptr, interpol.getY, points)