from math import *
from model.Point import *
import itertools


class ControlPoint:

    def Decroissante(self, liste):
        elementPrecedent = liste[0]
        for element in liste:
            if elementPrecedent < element:
                return False
            elementPrecedent = element
        # liste[0] = 0
        # liste.append(0)   
        return True

    def Pyramide(self, liste, max, taille):
        elementPrecedent = liste[0]
        for i, element in enumerate(liste):
            if element == max:
                for j in reversed(range(0, i - 1)):
                    for k in range(0, j + 1):
                        if liste[k] > liste[k + 1]:
                            return False
                for j in reversed(range(i, taille - 1)):
                    for k in range(i, j + 1):
                        if liste[k] < liste[k + 1]:
                            return False
                # liste[0] = 0
                # liste.append(0)         
                return True
        return False

    def creation_dico(self, N):
        dico = {}
        for i in range(1, N + 1):
            globals()['point{0}'.format(str(i))] = Point()
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
        return dico

    def cas_possible(self, dico, N):
        tab = []
        for key in dico.values():
            tab.append(key)
        tab.sort(reverse=True)
        tab_permute = []
        liste = []
        valmax = tab[0]
        tab_permute.extend(list(itertools.permutations(tab)))

        for index, element in enumerate(tab_permute):
            if (self.Decroissante(element) or not (self.Decroissante(element))) and self.Pyramide(element, valmax, N):
                # if Decroissante(element) or Croissante(element) or Pyramide(element, valmax, N):
                liste.append(element)
        return liste

    def temp_2_point(self, point1, point2):
        return int(sqrt(pow((point1._get_x() - point2._get_x()), 2) + pow((point1._get_y() - point2._get_y()), 2)))

    def parcours_0_0(self, liste):
        for i, element in enumerate(liste):
            tab = list(element)
            tab.insert(0, 0)
            tab.append(0)
            liste[i] = tab
        return liste

    def calcul(self, liste, dico):
        tabObject = []
        point0 = Point()
        for elementlist in liste:
            tab = []
            tab.insert(0, point0)
            for element in elementlist:
                for key, valeur in dico.items():
                    if element == valeur:
                        tab.append(key)
            tab.append(point0)
            tabObject.append(tab)
        tabSomme = []
        tabFinal = []
        for elementObject in tabObject:
            somme = 0
            for i in range(0, len(elementObject) - 1):
                somme += self.temp_2_point(elementObject[i], elementObject[i + 1])
            tabSomme.append([somme, elementObject])

        tempminimalTab = sorted(tabSomme, key=lambda tab: tab[0])

        return tempminimalTab[0]

    def itineraire(self, tabtemp,N):
        message = "Veuillez suivre l'itinéraire suivant  "
        for i,element in enumerate(tabtemp[1]):
            x = ","
            if i == N+1:
                x = "."
            message += "{}{} ".format(element._get_z(),x)
        return message + "\nTemps du parcours: {} min".format(tabtemp[0])
