import numpy as np


def dfs_Vl(graph, start, goal):
    visited = set()
    stack = [start]
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            print(node)
            if node == goal:
                return
            for neighbor in graph[node]:
                if neighbor not in visited:
                    stack.append(neighbor)


def dfs_AM(graph, start, goal):
    visited = set()
    stack = []
    stack.append([start])
    while stack:
        path = stack.pop()
        node = path[-1]
        if node not in visited:
            visited.add(node)

            if node == goal:
                return path
            for neighbor in range(0, graph.shape[1]):
                if (graph[node, neighbor] == 1):  # Now neighbor is an actual neighbor
                    if neighbor not in visited:

                        # stack.append(neighbor)
                        new_path = list(path)
                        new_path.append(neighbor)
                        stack.append(new_path)

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

print('DFS Stack implimentation  path G1:')
paths = []
paths = (dfs_AM(G1, 11, 6))
for path in paths:
    print(Nodes[path],end=" ")
