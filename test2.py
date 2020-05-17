from tree_properties import TreeProperties
from project import ResultValues
from test_env import TestEnv
from genere_regles import  GenereRegles
from moteur_id3_advance.id3_advance import ID3_advance
from regle import Regle
from data import  load_continous_train_set
from data import load_continous_test_set
from correcteur import Correcteur


moteur=ID3_advance()

continous=load_continous_train_set()
continous_test=load_continous_test_set()

arbre=moteur.construit_arbre(continous)


donnee=continous[0][1]
target=continous[0][0]
print(donnee,target)
print(arbre.classifie(donnee))

c=0
for d in continous_test:
    target=d[0]
    data=d[1]
    if arbre.classifie(data)[-1]!=target:
        c+=1

print(1-c/len(continous_test))



