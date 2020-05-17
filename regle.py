class Regle:

    def __init__(self, predicats={}, conclusion='?'):
        self.predicats=predicats
        self.conclusion=conclusion

    def add_predicat(self,attribut,val):
        self.predicats[attribut]=val
    def set_conclusion(self,c):
        self.conclusion=c

    def __repr__(self):
        res=str(self.predicats)

        return  res + " => " + str(self.conclusion)