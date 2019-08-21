import numpy as np


paths = []


def dfsRec_AM(graph, start, goal, visited, cond, path=[]):
    if visited is None:
        visited = set()
    path1 = []
    path1.append(path)
    visited.add(start)
    path = path + [start]
    print(Nodes[start],end=" ")
    if start == goal:
        paths.append(path)
    for next in range(graph.shape[1] - 1, 0, -1):
        if (graph[start, next] == 1):
            # if(cond==False):
            if next not in visited:
                if 'path' in locals():
                    dfsRec_AM(graph, next, goal, visited, cond, path)


###############################
########### Nodes dictionary
Nodes = {
    0: "a",
    1: "b",
    2: "c",
    3: "d",
    4: "e",
    5: "f",
    6: "g",
    7: "h",
    8: "p",
    9: "q",
    10: "r",
    11: "s",
}

#########################################################
#####################  Graph 1 ##########################

G1 = np.zeros((12, 12), dtype=int)
G1[0, 1] = 1;
G1[0, 2] = 1
G1[1, 0] = 1;
G1[1, 3] = 1;
G1[2, 0] = 1
G1[2, 3] = 1;
G1[2, 5] = 1
G1[3, 1] = 1;
G1[3, 2] = 1;
G1[3, 4] = 1;
G1[3, 11] = 1
G1[4, 3] = 1;
G1[4, 7] = 1;
G1[4, 10] = 1;
G1[4, 11] = 1
G1[5, 2] = 1;
G1[5, 6] = 1;
G1[5, 10] = 1
G1[6, 5] = 1
G1[7, 4] = 1;
G1[7, 8] = 1;
G1[7, 9] = 1
G1[8, 7] = 1;
G1[8, 9] = 1;
G1[8, 11] = 1
G1[9, 7] = 1;
G1[9, 8] = 1
G1[10, 4] = 1;
G1[10, 5] = 1;
G1[11, 3] = 1;
G1[11, 4] = 1;
G1[11, 8] = 1
print("DFS using Reccursion and Matrix G1")
dfsRec_AM(G1, 11, 6, None, False, [])
print("\nPath of DFS")
for path in paths:
    for p in path:
        print(Nodes[p],end=" ")
