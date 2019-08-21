def dfs_recursive(graph, vertex, path=[]):
    path += [vertex]

    for neighbor in graph[vertex]:
        if neighbor not in path:

            path = dfs_recursive(graph, neighbor, path)

    return path


List = {'s': ['d', 'e', 'p'],
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

print("The Path of DFS using List Graph 2")
path = dfs_recursive(List, 's')
for nodes in path:
    print(nodes, end=" ")
