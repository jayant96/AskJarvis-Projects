# We will use a depth first search algorithm.
# 1. We will start at the start node.
# 2. We will add the start node to a list of visited nodes.
# 3. We will find all the nodes that are adjacent to the start node.
# 4. We will remove the adjacent nodes that have already been visited.
# 5. We will sort the adjacent nodes by the number of edges between them and the start node.
# 6. We will visit the node with the fewest number of edges between it and the start node.
# 7. We will repeat steps 3-6 until we find the target node or until there are no more nodes to visit.
# 8. If we found the target node, we will return the list of visited nodes.
# 9. If we didn't find the target node, we will return an empty list.
# Show an example


def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start)
    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return visited

graph = {'0': set(['1', '2']),
         '1': set(['0', '3', '4']),
         '2': set(['0']),
         '3': set(['1']),
         '4': set(['2', '3'])}

dfs(graph, '0')

