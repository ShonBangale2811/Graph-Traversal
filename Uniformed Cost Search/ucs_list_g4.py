import numpy as np
import heapq


def UCS_AM(graph, start, goal):
    visited = set()
    pQueue = []
    heapq.heappush(pQueue, (0, start, [Nodes[start]]))

    while (len(pQueue) > 0):
        nodePriority, node, path = heapq.heappop(pQueue)
        print('node = ', Nodes[node], end=" ")
        visited.add(node)

        if node == goal:
            return path
        else:
            if node in graph:
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        heapq.heappush(pQueue,
                                       (nodePriority + graph[node][neighbor], neighbor, path + [Nodes[neighbor]]))

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


#####################  Graph 4 ##########################

G4 = np.zeros((12, 12), dtype=int)
G4 = {
    1: {0: 2},
    2: {0: 2},
    3: {1: 1, 2: 8, 4: 2},
    4: {7: 8, 10: 2},
    5: {2: 3, 6: 2},
    7: {8: 4, 9: 4},
    8: {9: 15},
    10: {5: 2},
    11: {3: 2, 4: 9, 8: 1}
}
print('\nVertex List')
path= UCS_AM(G4, 11, 6)
print("\n Path of UCS")
for node in path:
    print(node, end=" ")


