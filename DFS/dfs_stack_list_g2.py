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

List = {'s': ['d','e','p'],
         'd': ['b','c'],
         'e': ['h','r'],
         'p': ['q'],
         'b': ['a'],
         'c': ['a'],
         'h': ['p','q'],
         'r': ['f'],
         'q': [],
         'a': [],
         'f': ['c','g'],
         'g': []
                    }

print("The Path of DFS using List Graph 2")
path = dfs_iterative(List, 's')
for nodes in path:
    print(nodes, end=" ")
