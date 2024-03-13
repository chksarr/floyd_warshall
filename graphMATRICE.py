import sys

INF = 9999999

NIL = -1

class GraphMat:
    def __init__(self, size, type):
        self.mat = []
        self.type = type
        self.size = size
        for i in range(size):
            a = []
            for j in range(size):
                if i == j:
                    el = 0
                else:
                    el = INF
                a = a + [el]
            self.mat.append(a)

    def addarc(self, source, dest, poids):
            if source >=self.size or dest >= self.size or source < 0 or dest < 0:
                return 'ERROR'
            if self.type == 'NON_ORIENTED' and poids < 0:
                return 'ERROR'
            self.mat[source][dest] = poids
            if self.type == 'NON_ORIENTED':
                self.mat[dest][source] = poids
            return 'OK'

    
    def affiche_graphe(self):
        for i in range(self.size):
            print("")
            st = ""
            for j in range(self.size):
                if self.mat[i][j] == INF:
                    el = 'INF'
                else:
                    el = str(self.mat[i][j])
                st = st +" "+ " " + "m[{},{}]= {}". format(i,j, el)
            print(st)






"""
Exemple d'utilisation: 

G1 =GraphMat(5,'NON_ORIENTED')

G1.addarc(0, 4, 25)
G1.addarc(1, 2, 15)
G1.addarc(1, 0, 10)
G1.addarc(2, 0, 20)
G1.addarc(2, 4, 18)
G1.addarc(3, 1, 4)
G1.addarc(4, 3, 7)

print("\n\n Graph G1\n")

G1.affiche_graphe()

G2 =GraphMat(5,'ORIENTED')

G2.addarc(0, 4, 25)
G2.addarc(0, 1, -3)
G2.addarc(1, 2, -2)
G2.addarc(1, 0, 10)
G2.addarc(1, 4, -1)
G2.addarc(2, 0, 20)
G2.addarc(2, 1, 15)
G2.addarc(2, 4, 18)
G2.addarc(3, 1, -4)
G2.addarc(4, 3, 5)

print("\n\n Graph G2\n")

G2.affiche_graphe()

"""





