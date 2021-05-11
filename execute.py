from controller.ControlPoint import *

N = 0
while N <= 1 or N > 500:
    N = int(input("Nombre de destinations à desservir(2 à 500): "))

control = ControlPoint()
dico = control.creation_dico(N)
itineraire_possible = control.cas_possible(dico,N)
depart_arrive = control.parcours_0_0(itineraire_possible)

print(control.itineraire(control.calcul(depart_arrive,dico),N))