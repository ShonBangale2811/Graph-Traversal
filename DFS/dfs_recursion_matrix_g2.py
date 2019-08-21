import numpy as np

paths = []


def dfsRec_AM(graph, start, goal, visited, cond, path=[]):
    if visited is None:
        visited = set()
    path1 = []
    path1.append(path)
    visited.add(start)
    path = path + [start]
    print(Nodes[start],end="")
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
G2 = np.zeros((12,12),dtype=int)
G2[1,0]=1
G2[2,0]=1
G2[3,1]=1 ; G2[3,2]=1 ; G2[3,4]=1
G2[4,7]=1 ; G2[4,10]=1
G2[5,2]=1 ; G2[5,6]=1
G2[7,8]=1 ; G2[7,9]=1
G2[8,9]=1
G2[10,5]=1
G2[11,3]=1; G2[11,4]=1 ; G2[11,8]=1
print("DFS using Reccursion and Matrix G2")
dfsRec_AM(G2, 11, 6, None, False, [])
print("\nPath of DFS")
for path in paths:
    for p in path:
        print(Nodes[p],end=" ")

