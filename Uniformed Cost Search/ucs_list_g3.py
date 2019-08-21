import heapq


def UCS_AM(graph, start, goal):
    visited = set()
    pQueue = []
    heapq.heappush(pQueue, (0, start, [Nodes[start]]))

    while len(pQueue) > 0:
        nodePriority, node, path = heapq.heappop(pQueue)
        print('Node=', Nodes[node], end=" ")
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

#########################################################
#####################  Graph 3 ##########################
G3 = {
    0: {1: 2, 2: 2},
    1: {0: 2, 3: 1},
    2: {0: 2, 3: 8, 5: 3},
    3: {1: 1, 2: 8, 4: 2, 11: 3},
    4: {3: 2, 11: 9, 7: 8, 10: 2},
    5: {2: 3, 6: 2, 10: 2},
    6: {5: 2},
    7: {4: 8, 8: 4, 9: 4},
    8: {11: 1, 7: 4, 9: 15},
    9: {8: 15, 7: 4},
    10: {4: 2, 5: 2},
    11: {3: 2, 4: 9, 8: 1}
}

print('\nVertex List')
path= UCS_AM(G3, 11, 6)
print("\n Path of UCS")
for node in path:
    print(node, end=" ")

