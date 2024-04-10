import random

class Ia:

    def __init__(self, nom):
        self.choix = [[50, 50] for _ in range(8)]
        self.historique = {"1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0}
        self.palmares = [0, 0]
        self.nom = nom

    def recompense(self):
        for i, key in enumerate(self.historique): 
            if i < 2:
                if self.historique[key] == 1:
                    self.choix[i][0] += 1
                elif self.historique[key] == 2:
                    self.choix[i][-1] += 1
        self.historique = {"1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0}
        self.palmares[0] += 1
        return self.choix, self.historique, self.palmares
    
    def punition(self):
        for i, key in enumerate(self.historique): 
            if i < 8:
                if self.historique[key] == 1:
                    self.choix[i][0] -= 1
                elif self.historique[key] == 2:
                    self.choisir[i][-1] -= 1
        self.historique = {"1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0}
        self.palmares[-1] += 1
        return self.choix, self.historique, self.palmares

    def choisir(self, batons, choix):
        choix_tour = random.randint(1, sum(choix[batons - 1]))
        if 1 <= choix_tour <= choix[batons - 1][0] or batons == 1: 
            self.historique[f"{batons}"] += 1
            return 1
        if choix[batons - 1][0] <= choix_tour <= choix[batons - 1][0] + choix[batons - 1][1]:
                self.historique[f"{batons}"] += 1
                return 2
        
