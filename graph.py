class GRAPH:
    
    def __init__(self, size):        
        self.adjMatrix = []
        for i in range(size):
            self.adjMatrix.append([0 for i in range(size)])
        self.size = size

    def addEdge(self, v1, v2):
        """adding an edge in a directed graph from V1 to V2"""
        if v1 == v2:
            return
        self.adjMatrix[v1][v2] = 1


    def removeEdge(self, v1, v2):
        if self.adjMatrix[v1][v2] == 0:            
            return
        self.adjMatrix[v1][v2] = 0


    def printGraph(self):
        for i in range(self.size):
            for j in range(self.size):
                print(self.adjMatrix[i][j], end=" ")
            print()


    def getVertexAdjList(self, v):
        """function receives a vertex and returns a list of its neighbors"""
        adjList = []
        for i in range(self.size):
            if self.adjMatrix[v][i] == 1:
                adjList.append(i)

        return adjList


    def getIndegreeList(self):
        indegree = []

        for i in range(self.size):
            indegree.append(0)

        # outer loop columns, inner loop rows
        for i in range(self.size):
            for j in range(self.size):
                if self.adjMatrix[j][i] == 1:
                    indegree[i] += 1

        return indegree
