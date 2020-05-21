from data import load_train_set, load_continous_train_set, load_continous_test_set
from data import load_test_set
from moteur_id3.id3 import ID3
from moteur_id3_advance.id3_advance import ID3_advance
from tree_properties import TreeProperties
from test_env import TestEnv
from genere_regles import GenereRegles



class ResultValues():

    def __init__(self):
        # load the datasets
        self.train_set = load_train_set()
        self.test_set = load_test_set()
        # Do computations here

        # Task 1
        id3 = ID3()
        self.arbre = id3.construit_arbre(self.train_set)
        self.tree_properties = TreeProperties(self.arbre)
        # Task 2
        self.test_env = TestEnv(self.arbre, self.test_set)
        print(self.test_env)
        print(self.tree_properties)
        # Task 3/4
        g = GenereRegles(self.arbre, self.train_set)
        self.faits_initiaux = self.train_set
        self.regles = g.regles
        #TODO Faut il expliqué le test ou train set ?
        #Car si on explique le test on classifie 40% de fau et donc les explications non pas de sens
        g.explique_all(self.test_set,g.regles)
        g.explique_all(self.train_set,g.regles)





        # Task 5
        moteur = ID3_advance()
        continous = load_continous_train_set()
        continous_test = load_continous_test_set()
        self.arbre_advance = moteur.construit_arbre(continous)
        self.test_env_advanced = TestEnv(self.arbre_advance, continous_test)
        print(self.test_env_advanced)


    def get_results(self):
        return [self.arbre, self.faits_initiaux, self.regles, self.arbre_advance]



r = ResultValues()
