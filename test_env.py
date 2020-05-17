class TestEnv:

    def __init__(self, arbre, test_set):
        self.arbre = arbre
        self.test_set=test_set
        self.precision,self.target, self.predictions = self.evaluate(self.arbre,self.test_set)



    def evaluate(self,arbre, test_set):
        compteur = 0
        target = []
        predictions = []

        for d in test_set:
            classe = d[0]
            pred = arbre.classifie(d[1])[-1]
            predictions.append(pred)
            target.append(classe)
            if classe != pred:
                compteur += 1
        return 1-compteur/len(test_set) , target , predictions

    def __repr__(self):
        return "Pecision de l'arbre="+str(self.precision) +'\n'+ "La cible était :" + str(self.target)+'\n'+ "La prédiction était :" + str(self.predictions)