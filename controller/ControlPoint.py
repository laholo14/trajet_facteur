from math import sqrt,pow
from model.Point import *
import itertools


class ControlPoint:

    def Decroissante(self, liste):
        elementPrecedent = liste[0]
        for element in liste:
            if elementPrecedent < element:
                return False
            elementPrecedent = element
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
                return True
        return False

    def creation_dico(self, fichier):
        dico = {}
        for i,element in enumerate(fichier):
            globals()['point{}'.format(str(i+1))] = Point()
            Listsplit = element.split(" ")
            globals()['point{}'.format(str(i+1))]._set_x(int(Listsplit[0]))
            globals()['point{}'.format(str(i+1))]._set_y(int(Listsplit[1]))
            globals()['point{}'.format(str(i+1))]._set_z(int(Listsplit[2]))
            dico[globals()['point{}'.format(str(i+1))]] = globals()['point{}'.format(str(i+1))]._get_z()
        return dico

    def cas_possible(self, dico, N):
        tab = []
        liste = []
        tab_permute = []
        for key in dico.values():
            tab.append(key)
        tab.sort(reverse=True)
        valmax = tab[0]
        tab_permute.extend(list(itertools.permutations(tab)))
        for element in tab_permute:
            if (self.Decroissante(element) or not(self.Decroissante(element))) and self.Pyramide(element, valmax, N):
                liste.append(element)
        return liste
   
    def parcours_0_0(self, liste):
        for i, element in enumerate(liste):
            tab = list(element)
            tab.insert(0, 0)
            tab.append(0)
            liste[i] = tab
        return liste
    
    def temp_2_point(self, point1, point2):
        return int(sqrt(pow((point1._get_x() - point2._get_x()), 2) + pow((point1._get_y() - point2._get_y()), 2)))
    
    
    def calcul(self, liste, dico):
        tabObject = []
        tabSomme = []
        tabFinal = []
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
        for elementObject in tabObject:
            somme = 0
            for i in range(0, len(elementObject) - 1):
                somme += self.temp_2_point(elementObject[i], elementObject[i + 1])
            tabSomme.append([somme, elementObject])
        tempminimalTab = sorted(tabSomme, key=lambda index: index[0])
        return tempminimalTab[0]

    def itineraire(self, tabtemp,N):
        message = "Veuillez suivre l'itinéraire suivant  "
        for i,element in enumerate(tabtemp[1]):
            x = ","
            if i == N+1:
                x = "."
            message += "{}{} ".format(element._get_z(),x)
        return message + "\nTemps du parcours: {} min".format(tabtemp[0])
