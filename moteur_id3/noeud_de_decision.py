class NoeudDeDecision:
    """Un noeud dans un arbre de décision. """

    def __init__(self, attribut, donnees, enfants=None):
        """
            :param attribut: l'attribut de partitionnement du noeud (``None`` si\
            le noeud est un noeud terminal).
            :param list donnees: la liste des données qui tombent dans la\
            sous-classification du noeud.
            :param enfants: un dictionnaire associant un fils (sous-noeud) à\
            chaque valeur de l'attribut du noeud (``None`` si le\
            noeud est terminal).
        """

        self.attribut = attribut
        self.donnees = donnees
        self.enfants = enfants

    def terminal(self):
        """ Vérifie si le noeud courant est terminal. """

        return self.enfants is None

    def classe(self):
        """ Si le noeud est terminal, retourne la classe des données qui\
            tombent dans la sous-classification (dans ce cas, toutes les\
            données font partie de la même classe.
        """

        if self.terminal():
            return self.donnees[0][0]

    def classifie(self, donnee):
        """ Classifie une donnée à l'aide de l'arbre de décision duquel le noeud\
            courant est la racine.

            :param donnee: la donnée à classifier.
            :return: la classe de la donnée selon le noeud de décision courant.
        """

        rep = ''
        if self.terminal():
            rep += 'Alors {}'.format(self.classe())
        else:

            valeur = donnee[self.attribut]

            if valeur not in self.enfants:
                candidate=None
                size=0

                for k in self.enfants:
                    tmp=self.enfants[k].taille_donness()
                    if tmp>size:

                        candidate=k
                        size=tmp
                valeur=candidate

            enfant = self.enfants[valeur]

            rep += 'Si {} = {}, '.format(self.attribut, valeur)
            rep += enfant.classifie(donnee)
        return rep

    def repr_arbre(self, level=0):
        """ Représentation sous forme de string de l'arbre de décision duquel\
            le noeud courant est la racine.
        """

        rep = ''
        if self.enfants is None  :
            rep += '---'*level
            rep += 'Alors {}\n'.format(self.classe())
            rep += '---'*level
            rep += 'Décision basée sur les données:\n'
            for donnee in self.donnees:
                rep += '---'*level
                rep += str(donnee) + '\n'

        else:
            for valeur, enfant in self.enfants.items():
                rep += '---'*level
                rep += 'Si {} = {}: \n'.format(self.attribut, valeur)
                rep += enfant.repr_arbre(level+1)

        return rep

    def __repr__(self):
        """ Représentation sous forme de string de l'arbre de décision duquel\
            le noeud courant est la racine.
        """

        return str(self.repr_arbre(level=0))
    def taille_donness(self):
        if self.terminal():
            return len(self.donnees)
        else:
            res=0
            for k in self.enfants:
                res+=self.enfants[k].taille_donness()
            return res