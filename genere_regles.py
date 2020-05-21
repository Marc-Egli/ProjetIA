from regle import Regle
import copy
from correcteur import Correcteur

class GenereRegles:
    def __init__(self, arbre, train_set):
        self.arbre = arbre
        self.regles = self.genere_regles_rec(self.arbre, [Regle()])
        self.train_set = train_set
        self.regles_simplifiees = self.simplifie_all_regles(self.regles, self.train_set)
        self.correcteur = Correcteur(self.arbre,self.train_set)

    def genere_regles_rec(self, a, regles):
        if a.terminal():
            c = a.classe()
            for r in regles:
                r.set_conclusion(c)
            return regles
        else:
            res = []
            for valeur, enfant in a.enfants.items():
                next_regles = copy.deepcopy(regles)
                for r in next_regles:
                    r.add_predicat(a.attribut, valeur)
                res = res + self.genere_regles_rec(enfant, next_regles)
            return res

    def simplifie_all_regles(self, regles, train_set):
        res = []
        for r in regles:
            res.append(self.simplifie_regle(r, train_set))
        return res

    # r = Regle({'a': 0, 'b': 0}, 0)
    # set = [[0, {'a': 0, 'b': 0}], [0, {'a': 0, 'b': 1}]]
    # print(r)
    # ->{'a': 0, 'b': 0} => 0
    # print(self.simplifie_regle(r, set))
    # ->{'a': 0} => 0
    def simplifie_regle(self, regle, train_set):
        attributs = []
        for k in regle.predicats:
            attributs.append(k)
        to_delete = []
        for a in attributs:
            new_regle = copy.deepcopy(regle)
            new_regle.predicats.pop(a)
            valid = True
            for d in train_set:
                datapoint = d[1]
                target = d[0]
                if self.satisfie_regle(new_regle, datapoint):
                    valid = valid & (str(new_regle.conclusion) == str(target))
        if valid:
            to_delete.append(a)
        for a in to_delete:
            regle.predicats.pop(a)
        return regle

    def satisfie_regle(self, regle, data_point):
        attributs = []
        for k in regle.predicats:
            attributs.append(k)
        valid = True
        for a in attributs:
            valid = valid & (regle.predicats[a] == data_point[a])

        return valid

    def explique(self, fait, regles):
        datapoint = fait[1]
        for r in regles:
            if self.satisfie_regle(r, datapoint):
                if fait[0] == "1":
                    return print(
                        "Déduit " + r.conclusion + " par la règle : " + r.__repr__() + " pour le fait " + str(fait) +
                        "\nPeut être guerit en changeant : " + str(self.correcteur.corrige(fait[1])[1]))

                else:
                    return print(
                        "Déduit " + r.conclusion + " par la règle : " + r.__repr__() + " pour le fait " + str(fait))

    def explique_all(self, faits, regles):
        for fait in faits:
            self.explique(fait, regles)
