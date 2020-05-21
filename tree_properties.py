class TreeProperties:

    def __init__(self, a):
        self.arbre=a
        self.avg_child=self.avg_child_rec(self.arbre)
        self.longest_branch=self.longest_branch_rec(self.arbre,0)
        self.shortest_branch = self.shortest_branch_rec(self.arbre, 0)

    def avg_child_rec(self,a):
        enfants=a.enfants
        res=len(enfants)
        for k in enfants:
            e=enfants[k]
            if not e.terminal():
                res+=self.avg_child_rec(e)
                res/=2
        return  res

    def longest_branch_rec(self,a,length):
        if a.terminal():
            return length
        else:
            choices=[]
            for  k in a.enfants:
                e=a.enfants[k]
                choices.append(self.longest_branch_rec(e,length+1))
            return max(choices)


    def shortest_branch_rec(self,a,length):
        if a.terminal():
            return length
        else:
            choices=[]
            for  k in a.enfants:
                e=a.enfants[k]
                choices.append(self.shortest_branch_rec(e,length+1))
            return min(choices)

    def __repr__(self):
        return str(
            {
                "Nombre moyen d'enfants : ": self.avg_child,
                "Taille de la plus grande branche : ": self.longest_branch,
                "Taille de la plus courte branche : ": self.shortest_branch
            }
        )