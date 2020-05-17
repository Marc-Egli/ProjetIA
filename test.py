from moteur_id3.id3 import ID3
from data import load_train_set
from data import load_test_set
from test_env import TestEnv
from project import ResultValues
from genere_regles import GenereRegles
from moteur_id3_advance.id3_advance import ID3_advance
from regle import Regle
from data import load_continous_train_set
from data import load_continous_test_set
from tree_properties import TreeProperties


def initial_precison():
    id3 = ID3()
    arbre = id3.construit_arbre(load_train_set())
    properties = TreeProperties(arbre)
    test_env = TestEnv(arbre, load_test_set())
    print(test_env)
    g = GenereRegles(arbre, load_train_set())
    g.explique(load_train_set()[0], g.regles)



def task5_precison():
    best_test = 0
    max_prec = 0
    for i in range(2000) :
        moteur = ID3_advance()
        continous = load_continous_train_set()
        continous_test = load_continous_test_set()
        arbre = moteur.construit_arbre(continous)
        test_env = TestEnv(arbre, continous_test)
        if test_env.precision > max_prec :
            max_prec = test_env.precision
            best_test = test_env

    print(best_test)
    print(arbre)

initial_precison()
task5_precison()
r = ResultValues()
