from data import load_train_set
from data import load_test_set
from moteur_id3.id3 import ID3
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
        # Task 3
        g = GenereRegles(self.arbre, self.train_set)
        self.faits_initiaux = self.train_set
        self.regles = g.regles
        g.explique_all(self.test_set,g.regles)







        # Task 5
        self.arbre_advance = None

    def get_results(self):
        return [self.arbre, self.faits_initiaux, self.regles, self.arbre_advance]
