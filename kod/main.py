from functions import print_fun
import points_gen as pg
from newton_poly import STinterpol
from newton_poly import EQinterpol
from charts import gen_chart
import numpy as np

# wybierz funkcję
fun_name, fun_ptr = print_fun()

# pobierz dane
a           = float(input("Podaj lewą stronę przedziału: "))
b           = float(input("Podaj prawą stronę przedziału: "))
points_am   = int(input("Podaj ile węzłów wygenerować: "))

# ustaw dobrze początek i koniec przedziału
if a > b: a,b = b,a

# pobierz nazwę pliku
filename = "wykresy/" + input("Podaj nazwę pliku z wykresem: ")

###############################
# generowanie interpolacji z punktami
# równoodległymi
points_eq = []
for x in pg.gen_equidistant(a, b, points_am):
    points_eq.append([x, fun_ptr(x)])
points_eq = np.array(points_eq).transpose()

eqinterpol = EQinterpol(points_eq)
gen_chart(fun_ptr, eqinterpol.getY, points_eq, a, b, filename + "_eq.png")

###############################
# generowanie interpolacji z punktami
# losowymi
points_rand = []
for x in pg.gen_random(a, b, points_am):
    points_rand.append([x, fun_ptr(x)])
points_rand = np.array(points_rand).transpose()

stinterpol = STinterpol(points_rand)
gen_chart(fun_ptr, stinterpol.getY, points_rand, a, b, filename + "_rand.png")

print("funkcja:       {}".format(fun_name))
print("przedział:     {} - {}".format(a, b))
print("liczba węzłów: {}".format(points_am))
print()
print("interpolacja losowa:")
print("    współczynniki:   {}".format(stinterpol.getCoef()))
print("    węzły (x):       {}".format([round(elem, 3) for elem in points_rand[0]]))
print("    węzły (y):       {}".format([round(elem, 3) for elem in points_rand[1]]))
print()
print("interpolacja równoodległa:")
print("    współczynniki:   {}".format(eqinterpol.getCoef()))
print("    węzły (x):       {}".format([round(elem, 3) for elem in points_eq[0]]))
print("    węzły (y):       {}".format([round(elem, 3) for elem in points_eq[1]]))