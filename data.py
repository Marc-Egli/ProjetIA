import csv

def load_train_set():
   return load("train_bin.csv")

def load_test_set():
   return load("test_public_bin.csv")


def load_continous_train_set():
   return load("train_continuous.csv")


def load_continous_test_set():
   return load("test_public_continuous.csv")

def load(file_name):
    with open(file_name, newline='') as csvfile:
        data = list(csv.reader(csvfile))
    attribut = data[0]
    attribut[0]="age"
    res=[]
    for i in range(1,len(data)):
           target= data[i][-1]
           dict={}
           for j in range(len(attribut)-1):
                   dict[attribut[j]]=data[i][j]
           data_point = [target,dict]
           res.append(data_point)

    return res