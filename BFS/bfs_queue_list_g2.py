def bfs(graph, start):
    visited = []
    queue = [start]
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.append(node)
            neighbors = graph[node]
        for neighbor in neighbors:
            queue.append(neighbor)
    return visited


List_G2 = {'s': ['d', 'e', 'p'],
           'd': ['b', 'c'],
           'e': ['h', 'r'],
           'p': ['q'],
           'b': ['a'],
           'c': ['a'],
           'h': ['p', 'q'],
           'r': ['f'],
           'q': [],
           'a': [],
           'f': ['c', 'g'],
           'g': []
           }

print("The BFS Traversal")
traversal = bfs(List_G2, 's')
for string in traversal:
    print(string, end=" ")
