def dfs_iterative(graph, start):
    stack, path = [start], []

    while stack:
        vertex = stack.pop()
        if vertex in path:
            continue
        path.append(vertex)
        for neighbor in graph[vertex]:
            stack.append(neighbor)

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
path = dfs_iterative(List, 's')
for nodes in path:
    print(nodes, end=" ")
