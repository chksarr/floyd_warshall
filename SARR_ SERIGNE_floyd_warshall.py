from graphMATRICE import GraphMat

INF = 9999999
NIL = -1

class FloydWarshallGraph(GraphMat):
    def __init__(self, size, type):
        super().__init__(size, type)

    @staticmethod
    def initialize_matrices(size, mat):
        D = []
        P = []
        for i in range(size):
            D.append([])
            P.append([])
            for j in range(size):
                D[i].append(mat[i][j])
                if i == j or mat[i][j] == INF:
                    P[i].append(NIL)
                else:
                    P[i].append(i)
        return D, P

    def floyd_warshall(self):
        D, P = self.initialize_matrices(self.size, self.mat)

        for k in range(self.size):
            for i in range(self.size):
                for j in range(self.size):
                    if D[i][k] + D[k][j] < D[i][j]:
                        D[i][j] = D[i][k] + D[k][j]
                        P[i][j] = P[k][j]

        return D, P

    def affiche_chemin(self, i, j, P):
        if P[i][j] == NIL:
            print(f"Il n'y a pas de chemin entre {i} et {j}.")
        else:
            print(f" Le Chemin de {i} à {j} : {i}", end=" ")
            self.print_chemin(i, j, P)

    def print_chemin(self, i, j, P):
        if P[i][j] != i:
            self.print_chemin(i, P[i][j], P)
        print(f"-> {j}", end=" ")


if __name__ == "__main__":
    G = FloydWarshallGraph(5, 'NON_ORIENTED')
    G.addarc(0, 4, 25)
    G.addarc(1, 2, 15)
    G.addarc(1, 0, 10)
    G.addarc(2, 0, 20)
    G.addarc(2, 4, 18)
    G.addarc(3, 1, 4)
    G.addarc(4, 3, 7)

    D, P = G.floyd_warshall()

    print("\n\n Matrice des coûts D############################### \n")
    G.affiche_graphe()

    print("\n\n Matrice des prédécesseurs P#########################\n")
    G.affiche_graphe()
    print("\n")

    G.affiche_chemin(0, 3, P)
