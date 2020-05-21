from moteur_id3.id3 import ID3
from data import load_train_set
from data import load_test_set
from test_env import TestEnv
from project import ResultValues
from genere_regles import GenereRegles
from moteur_id3_advance.id3_advance import ID3_advance
from data import load_continous_train_set
from data import load_continous_test_set
from tree_properties import TreeProperties


def initial_precison():
    id3 = ID3()
    arbre = id3.construit_arbre(load_train_set())
    properties = TreeProperties(arbre)
    test_env = TestEnv(arbre, load_test_set())
    print(test_env)
    print(properties)
    g = GenereRegles(arbre, load_train_set())
    g.explique(load_train_set()[0], g.regles)



def task5_precison():

    moteur = ID3_advance()
    continous = load_continous_train_set()
    continous_test = load_continous_test_set()
    arbre = moteur.construit_arbre(continous)
    test_env = TestEnv(arbre, continous_test)
    print(test_env)


initial_precison()
task5_precison()
r = ResultValues()
