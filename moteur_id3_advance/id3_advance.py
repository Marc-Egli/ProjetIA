from math import log
from .noeud_de_decision_advance import NoeudDeDecision
import copy
import random
class ID3_advance:
    """ Algorithme ID3. """

    def construit_arbre(self, donnees):
        """ Construit un arbre de décision à partir des données d'apprentissage.

            :param list donnees: les données d'apprentissage\
            ``[classe, {attribut -> valeur}, ...]``.
            :return: une instance de NoeudDeDecision correspondant à la racine de\
            l'arbre de décision.
        """

        # Nous devons extraire les domaines de valeur des
        # attributs, puisqu'ils sont nécessaires pour
        # construire l'arbre.
        attributs = {}
        for donnee in donnees:
            for attribut, valeur in donnee[1].items():
                valeurs = attributs.get(attribut)
                if valeurs is None:
                    valeurs = set()
                    attributs[attribut] = valeurs
                valeurs.add(valeur)

        arbre = self.construit_arbre_recur(donnees, attributs)



        return arbre



    def one_classe(self, donnees):
        c=donnees[0][0]
        for d in donnees:
            if c!=d[0]:
                return False
        return True




    def construit_arbre_recur(self, donnees, attributs,classe_cominante='0'):
        """ Construit rédurcivement un arbre de décision à partir
            des données d'apprentissage et d'un dictionnaire liant
            les attributs à la liste de leurs valeurs possibles.

            :param list donnees: les données d'apprentissage\
            ``[classe, {attribut -> valeur}, ...]``.
            :param attributs: un dictionnaire qui associe chaque\
            attribut A à son domaine de valeurs a_j.
            :return: une instance de NoeudDeDecision correspondant à la racine de\
            l'arbre de décision.
        """

        if donnees==[]:

            return NoeudDeDecision([],[[classe_cominante,{}],],None)
        elif self.one_classe(donnees):
            return NoeudDeDecision([],donnees,None)
        else:

            critere_sepration = self.meilleure_separation(donnees, attributs)
            attribut,valeur=critere_sepration
            classe_gauche, classe_droite = self.partitionne(donnees,critere_sepration)

            valeurs_gauches = []
            valeurs_droites = []
            for v in attributs[attribut] :
                if v < valeur :
                    valeurs_gauches.append(v)
                else :
                    valeurs_droites.append(v)

            attributs_gauche = {}
            attributs_droite = {}
            for a in attributs :
                if a == attribut :
                    attributs_droite[a] = valeurs_droites
                    attributs_gauche[a] = valeurs_gauches
                else :
                    attributs_droite[a] = attributs[a]
                    attributs_gauche[a] = attributs[a]

            enfants = {}
            enfants['left']=self.construit_arbre_recur(classe_gauche,attributs_gauche,self.classe_dominante(donnees))
            enfants['right'] = self.construit_arbre_recur(classe_droite, attributs_droite, self.classe_dominante(donnees))

            return NoeudDeDecision(attribut, donnees,critere_sepration, enfants)

    def partitionne(self,donnees, critere):
        """ Partitionne les données sur les valeurs a_j de l'attribut A.

            :param list donnees: les données à partitioner.
            :param attribut: l'attribut A de partitionnement.
            :param list valeurs: les valeurs a_j de l'attribut A.
            :return: un dictionnaire qui associe à chaque valeur a_j de\
            l'attribut A une liste l_j contenant les données pour lesquelles A\
            vaut a_j.
        """
        attribut , valeur =critere
        classe_gauche = []
        classe_droite = []

        for d in donnees:
            if d[1][attribut] < valeur:
                classe_gauche.append(d)
            else:
                classe_droite.append(d)

        return classe_gauche,classe_droite



    def meilleure_separation(self,donnees, attributs):
        candidats = ()
        candidats = []
        meilleure_entropy=1
        for a in attributs:
            for v in attributs[a]:
                entropy=self.entropy_of_split(donnees,a,v)
                if entropy<meilleure_entropy:
                    meilleure_entropy = entropy
                    candidats = [(a,v)]
                elif entropy == meilleure_entropy :
                    candidats.append((a,v))
        if len(candidats) is not  1 :
            candidats.sort(key=lambda x: x[1])
            candidat = random.choice(candidats)
        else :
            candidat = candidats[0]




        return candidat







   #calcul l'entropy d'une sepration en deux classes (attribut<valeur et attribut>valeur) des donnees
    def entropy_of_split(self,donnees, attribut , valeur):
        classe_gauche=[]
        classe_droite=[]

        for d in donnees:
            if d[1][attribut]<valeur:
                classe_gauche.append(d)
            else:
                classe_droite.append(d)

        total=len(donnees)
        p_gauche=len(classe_gauche)/total
        p_droite=len(classe_droite)/total

        #si une des classe est vide la separation est inutile, on retourne donc le valeur maximale de l'entropie (1)
        if len(classe_gauche)==0 or len(classe_droite)==0:
            return 1


        e_gauche=self.entropy_of_class(classe_gauche)
        e_droite=self.entropy_of_class(classe_droite)

        return p_gauche*e_gauche+p_droite*e_droite

    #calcule l'trntropy d'un sous ensemble de données
    def entropy_of_class(self,classe):
        zeros=0
        ones=0
        total=len(classe)
        for d in classe:
            if d[0]==str(0):
                zeros+=1
            else:
                ones+=1
        p0=zeros/total
        p1=ones/total

        if p0==0:
            return 0
        if p1==0:
            return 0

        return -p0*log(p0, 2.0)-p1*log(p1, 2.0)




    def classe_dominante(self,donnees):
        ones=0
        zeros=0
        for d in donnees:
            classe=d[0]
            if classe==str(0):
                zeros+=1
            if classe==str(1):
                ones+=1

        res=str(1)
        if zeros>ones:
            res= str(0)

        return res



