# Using a Python dictionary to act as an adjacency list
# graph = {
#     'A': ['B', 'C'],
#     'B': ['D', 'E'],
#     'D': ['H', 'I'],
#     'C': ['F', 'G'],
#     'E': ['J', 'K'],
#     'F': ['L', 'M'],
#     'G': ['N', 'O'],
#     'H': [],
#     'I': [],
#     'J': [],
#     'K': [],
#     'L': [],
#     'M': [],
#     'N': [],
#     'O': []
# }
graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'D': ['G', 'H'],
    'C': ['E', 'F'],
    'E': ['I', 'J'],
    'F': ['K', 'L'],
    'G': [],
    'H': [],
    'I': [],
    'J': [],
    'K': [],
    'L': [],
}
visited = set()  # Set to keep track of visited nodes of graph.


def dfs(visited, graph, node):  # function for dfs
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)


# Driver Code
print("DFS")
dfs(visited, graph, 'A')
