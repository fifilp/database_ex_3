class GRAPH:
    # adjMatrix = None
    # size = 0

    # Initialize the matrix
    def __init__(self, size):
        self.adjMatrix = []
        for i in range(size):
            self.adjMatrix.append([0 for i in range(size)])
        self.size = size

    # Add edges
    def addEdge(self, v1, v2):
        if v1 == v2:
            return
        self.adjMatrix[v1][v2] = 1

    # Remove edges
    def removeEdge(self, v1, v2):
        if self.adjMatrix[v1][v2] == 0:
            print("No edge between %d and %d" % (v1, v2))
            return
        self.adjMatrix[v1][v2] = 0

    # Print the matrix

    def printGraph(self):
        for i in range(self.size):
            for j in range(self.size):
                print(self.adjMatrix[i][j], end=" ")
            print()

    def getVertexAdjList(self, v):
        adjList = []
        for i in range(self.size):
            if self.adjMatrix[v][i] == 1:
                adjList.append(i)

        return adjList

    def getIndegreeList(self):
        indegree = []

        for i in range(self.size):
            indegree.append(0)

        # traverse columns and not rows - delete later
        for i in range(self.size):
            for j in range(self.size):
                if self.adjMatrix[j][i] == 1:
                    indegree[i] += 1

        return indegree
