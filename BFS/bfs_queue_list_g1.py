def bfs(graph, start):
    # Visited nodes
    visited = []
    # nodes not visited
    queue = [start]

    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.append(node)
            neighbors = graph[node]
            for neighbor in neighbors:
                queue.append(neighbor)
    return visited


List_G1 = {'s': ['d', 'e', 'p'],
           'd': ['b', 'c', 'e', 's'],
           'e': ['d', 'h', 'r', 's'],
           'p': ['h', 'q', 's'],
           'b': ['a', 'd'],
           'c': ['a', 'd', 'f'],
           'h': ['e', 'p', 'q'],
           'r': ['e', 'f'],
           'q': ['h', 'p'],
           'a': ['b', 'c'],
           'f': ['c', 'g', 'r'],
           'g': ['f']
           }
print("The BFS Traversal")
traversal = bfs(List_G1, 's')
for string in traversal:
    print(string, end=" ")
