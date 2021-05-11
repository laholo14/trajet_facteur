from math import *
from model.Point import *
import itertools


def temp_2_point(point1, point2):
    return int(sqrt(pow((point1._get_x() - point2._get_x()), 2) + pow((point1._get_y() - point2._get_y()), 2)))

def Croissante(L):
    elementPrecedent = L[0]
    for element in L:
        if elementPrecedent > element:
            return False
        elementPrecedent = element
    return True


def Decroissante(L):
    elementPrecedent = L[0]
    for element in L:
        if elementPrecedent < element:
            return False
        elementPrecedent = element
    return True
    

def Pyramide(L, max, n):
    elementPrecedent = L[0]
    for i, element in enumerate(L):
        if element == max:
            for j in reversed(range(0, i - 1)):
                for k in range(0, j + 1):
                    if L[k] > L[k + 1]:
                        return False
            for j in reversed(range(i, n - 1)):
                for k in range(i, j + 1):
                    if L[k] < L[k + 1]:
                        return False
            return True
    return False


def cas_possible(dico, N):
    tab = []
    for key in dico.values():
        tab.append(key)

    tab_permute = []
    tabfin = []
    valmax = tab[0]

    tab_permute.extend(list(itertools.permutations(tab)))

    for index, element in enumerate(tab_permute):
        if Decroissante(element) or Croissante(element) or Pyramide(element, valmax, N):
            tabfin.append(element)
    return tabfin



def calcul(N):
    dico = {}
    for i in range(1, N + 1):
        globals()['point{0}'.format(str(i))] = Point()
        globals()['point{0}'.format(str(i))]._set_id(i)
        if str(i) == "1":
            terme = "ère"
        else:
            terme = "ème"

        globals()['x{0}'.format(str(i))] = int(input("Coordonne x de la " + str(i) + terme + " destination: "))
        globals()['point{0}'.format(str(i))]._set_x(globals()['x{0}'.format(str(i))])

        globals()['y{0}'.format(str(i))] = int(input("Coordonne y de la " + str(i) + terme + " destination: "))
        globals()['point{0}'.format(str(i))]._set_y(globals()['y{0}'.format(str(i))])

        globals()['z{0}'.format(str(i))] = -1
        while globals()['z{0}'.format(str(i))] <= 0:
            globals()['z{0}'.format(str(i))] = int(input("Altitude de la " + str(i) + terme + " destination: "))
            globals()['point{0}'.format(str(i))]._set_z(globals()['z{0}'.format(str(i))])

        dico[globals()['point{0}'.format(str(i))]] = globals()['point{0}'.format(str(i))]._get_z()

    tableau = cas_possible(dico,N)
    return tableau

