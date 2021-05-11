from model.Point import *
from controller.ControlPoint import *
import itertools

N = 0
while N <= 0 or N > 500:
    N = int(input("Nombre de destinations à desservir(1 à 500): "))



print(calcul(N))

