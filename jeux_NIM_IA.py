from IA import Ia
import random

def definir_j1(liste_ia):
    j1 = random.randint(1, 2)
    if j1 == 1:
        return liste_ia[0], liste_ia[-1]
    else:
        return liste_ia[-1], liste_ia[0]

def fin_jeu(vainqueur, perdant):
    vainqueur.recompense()
    perdant.punition()
    print(vainqueur.nom, "a gagné:")
    print("    palmarès: ", vainqueur.palmares[0], "-", vainqueur.palmares[-1])
    print("Options1:", vainqueur.choix)
    print(perdant.nom, "a perdu:")
    print("    palmarès: ", perdant.palmares[0], "-", perdant.palmares[-1])
    print("Options2:", perdant.choix)

def main():
    ia1, ia2 = Ia("ia1"), Ia("ia2")
    entrainement = int(input("Entrer le nombre de simulations: "))
    for _ in range(entrainement):
        nb_batons = 8
        j1, j2 = definir_j1([ia1, ia2])
        while nb_batons > 0:
            nb_batons -= j1.choisir(nb_batons, j1.choix)
            if nb_batons <= 0:
                fin_jeu(j1, j2)
                break
            nb_batons -= j2.choisir(nb_batons, j2.choix)
            if nb_batons <= 0:
                fin_jeu(j2, j1)
                break


main()
