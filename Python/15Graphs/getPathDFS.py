# Given an undirected graph G(V, E) and two vertices v1 and v2(as integers), find and print the path from v1 to v2 (if exists). Print nothing if there is no path between v1 and v2.
# Find the path using DFS and print the first path that you encountered.
# V is the number of vertices present in graph G and vertices are numbered from 0 to V-1.
# E is the number of edges present in graph G.
# Print the path in reverse order. That is, print v2 first, then intermediate vertices and v1 at last.
# Note : Save the input graph in Adjacency Matrix.
# Input Format :
# Line 1: Two Integers V and E (separated by space)
# Next E lines : Two integers a and b, denoting that there exists an edge between vertex a and vertex b (separated by space)
# Line (E+2) : Two integers v1 and v2 (separated by space)
# Output Format :
# Path from v1 to v2 in reverse order (separated by space)
# Constraints :
# 2 <= V <= 1000
# 1 <= E <= 1000
# 0 <= v1, v2 <= V-1
# Sample Input 1 :
# 4 4
# 0 1
# 0 3
# 1 2
# 2 3
# 1 3
# Sample Output 1 :
# 3 0 1
# Sample Input 2 :
# 6 3
# 5 3
# 0 1
# 3 4
# 0 3
# Sample Output 2 :

class Graph:
    def __init__(self, nVertices):
        self.nVertices = nVertices
        self.adjMatrix = [[0 for i in range(nVertices)] for j in range(nVertices)]
        
    def addEdge(self, v1, v2):
        self.adjMatrix[v1][v2] = 1
        self.adjMatrix[v2][v1] = 1
        
    def dfsHelper(self, sv, v2, visited):
        visited[sv] = True
        if sv == v2:
            return [v2]
        
        for i in range(self.nVertices):
            if self.adjMatrix[sv][i] > 0 and visited[i] is False:
                val = self.dfsHelper(i, v2, visited)
                if val is not None:
                    val.append(sv)
                    return val
            
        return None
        
    
    def dfsPath(self, v1, v2):
        visited = [False for i in range(self.nVertices)]
        lst = self.dfsHelper(v1, v2, visited)
        return lst
        
    def removeEdge(self, v1, v2):
        if self.containsEdge(v1, v2) is False:
            return
        self.adjMatrix[v1][v2] = 0
        self.adjMatrix[v2][v1] = 0
    
    def containsEdge(self, v1, v2):
        return True if self.adjMatrix[v1][v2] > 0 else False
    
    def __str__(self):
        return str(self.adjMatrix)


V, E = [int(i) for i in input().strip().split()]

g = Graph(V)

for i in range(E):
    a, b = [int(i) for i in input().strip().split()]
    g.addEdge(a,b)

v1, v2 = [int(i) for i in input().strip().split()]

lst = g.dfsPath(v1, v2)
if lst:
    print(*lst)
