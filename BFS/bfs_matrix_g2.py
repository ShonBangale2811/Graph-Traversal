import numpy as np


def bfs_MATRIX(g, start, goal):
    visited = set()
    queue = [[start]]
    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node not in visited:
            visited.add(node)
            print(Nodes[node], end=" ")
            if node == goal:
                return path
        for neighbor in range(0, g.shape[1]):
            if g[node, neighbor] == 1:  # Now neighbor is an actual neighbor
                if neighbor not in visited:
                    # print(node,neighbor)
                    new_path = list(path)
                    new_path.append(neighbor)
                    queue.append(new_path)


# Nodes dictionary

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

G2 = np.zeros((12, 12), dtype=int)
G2[1, 0] = 1
G2[2, 0] = 1
G2[3, 1] = 1;
G2[3, 2] = 1;
G2[3, 4] = 1
G2[4, 7] = 1;
G2[4, 10] = 1
G2[5, 2] = 1;
G2[5, 6] = 1
G2[7, 8] = 1;
G2[7, 9] = 1
G2[8, 9] = 1
G2[10, 5] = 1
G2[11, 3] = 1;
G2[11, 4] = 1;
G2[11, 8] = 1

print('\nQueue BFS - Adjacency Matrix :')
paths = []
paths = (bfs_MATRIX(G2, 11, 6))
print('\nQueue-Paths BFS - Adjacency Matrix :')
for path in paths:
    print(Nodes[path], end=" ")

