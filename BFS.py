graph = {0:[1,2],
         1:[3,4],
         2:[5,6],
         3:[],
         4:[],
         5:[],
         6:[]}
visited = []
queue = []

def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)

    while queue:
        current_node = queue.pop(0)
        print(current_node, end=" ")

        for neighbour in graph[current_node]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

print("Following is breadth first search:")
bfs(visited, graph, 0)
