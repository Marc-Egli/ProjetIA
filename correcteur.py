class Correcteur:

    def __init__(self, arbre, test_set):
        self.arbre = arbre
        self.test_set = test_set
        attributs = {}
        for donnee in test_set:
            for attribut, valeur in donnee[1].items():
                valeurs = attributs.get(attribut)
                if valeurs is None:
                    valeurs = set()
                    attributs[attribut] = valeurs
                valeurs.add(valeur)
        self.attributs = attributs
        self.attributs.pop('age')
        self.attributs.pop('sex')

    def corrige(self, fait):

        def help():
            keys = []
            current_key = 0
            for k in self.attributs:
                keys.append(k)

            queue = [fait]
            while len(queue) > 0:
                fait_actuel = queue.pop(0)
                pred = self.arbre.classifie(fait_actuel)[-1]
                if pred == str(0):
                    return fait_actuel
                else:
                    attribut = keys[current_key]
                    if current_key <= len(keys) - 2:
                        current_key += 1
                    for valeur in self.attributs[attribut]:
                        nouveau_fait = fait_actuel.copy()
                        nouveau_fait[attribut] = valeur
                        queue = queue + [nouveau_fait]

        corrected = help()
        changes = []
        for k in corrected:
            if corrected[k] != fait[k]:
                changes.append({k: corrected[k]})
        return corrected, changes
