import numpy as np
import heapq


def UCS_AM(graph, start, goal):
    visited = set()
    pQueue = []
    heapq.heappush(pQueue, (0, start, [Nodes[start]]))

    while (len(pQueue) > 0):
        nodePriority, node, path = heapq.heappop(pQueue)
        print('Vistied node = ', Nodes[node], end=" ")
        visited.add(node)

        if node == goal:
            return path
        else:
            for x in range(0, graph.shape[1]):
                if (graph[node, x] > 0):  # weighted edge
                    neighbor = x
                    if neighbor not in visited:
                        heapq.heappush(pQueue, (nodePriority + graph[node, x], neighbor, path + [Nodes[neighbor]]))

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
G4[1, 0] = 2
G4[2, 0] = 2
G4[3, 1] = 1;
G4[3, 2] = 8;
G4[3, 4] = 2
G4[4, 7] = 8;
G4[4, 10] = 2
G4[5, 2] = 3;
G4[5, 6] = 2
G4[7, 8] = 4;
G4[7, 9] = 4
G4[8, 9] = 15
G4[10, 5] = 2
G4[11, 3] = 3;
G4[11, 4] = 9;
G4[11, 8] = 1

print('\nVertex List')
path= UCS_AM(G4, 11, 6)
print("\nPath of UCS")
for node in path:
    print(node, end=" ")


