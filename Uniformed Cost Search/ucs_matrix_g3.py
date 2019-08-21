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

#########################################################
#####################  Graph 3 ##########################
G3 = np.zeros((12, 12), dtype=int)
G3[0, 1] = 2;
G3[0, 2] = 2
G3[1, 0] = 2;
G3[1, 3] = 1;
G3[2, 0] = 2;
G3[2, 3] = 8;
G3[2, 5] = 3
G3[3, 1] = 1;
G3[3, 2] = 8;
G3[3, 4] = 2;
G3[3, 11] = 3
G3[4, 3] = 2;
G3[4, 7] = 8;
G3[4, 10] = 2;
G3[4, 11] = 9
G3[5, 2] = 3;
G3[5, 6] = 2;
G3[5, 10] = 2
G3[6, 5] = 2
G3[7, 4] = 8;
G3[7, 8] = 4;
G3[7, 9] = 4
G3[8, 7] = 4;
G3[8, 9] = 15;
G3[8, 11] = 1
G3[9, 7] = 4;
G3[9, 8] = 15
G3[10, 4] = 2;
G3[10, 5] = 2;
G3[11, 3] = 3;
G3[11, 4] = 9;
G3[11, 8] = 1

print('\nVertex List')
path= UCS_AM(G3, 11, 6)
print("\n Path of UCS")
for node in path:
    print(node, end=" ")
