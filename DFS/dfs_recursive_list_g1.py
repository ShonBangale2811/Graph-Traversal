def dfs_recursive(graph, vertex, path=[]):
    path += [vertex]

    for neighbor in graph[vertex]:
        if neighbor not in path:
            path = dfs_recursive(graph, neighbor, path)

    return path


List = {'s': ['d', 'e', 'p'],
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
print("The Path of DFS using List Graph 1")
path=dfs_recursive(List, 's')
for nodes in path:
    print(nodes, end=" ")
