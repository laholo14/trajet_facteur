from controller.ControlPoint import *
import time

entrer = open("in/1.in","r")
N = int(entrer.readline())
control = ControlPoint()
dico = control.creation_dico(entrer)
entrer.close()  
start_time = time.time() 
itineraire_possible = control.cas_possible(dico,N)
print(itineraire_possible)  
print("--- %s secondes ---" % (time.time() - start_time))
depart_arrive = control.parcours_0_0(itineraire_possible)
minimal = control.calcul(depart_arrive,dico)

sortie = open("out/1.out","w")
sortie.write(control.itineraire(minimal,N))
sortie.close()

  
