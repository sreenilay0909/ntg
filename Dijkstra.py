graph ={5:[3,7],
        3:[2,4],
        7:[8],
        2:[],
        4:[8],
        8:[8]}
visited=[]
quece=[]
def bfs (vistied,graph,node):
    visited.append(node)
    quece.append(node)
    while quece:
        m=quece.pop(0)
        print(m, end="")
        for neighbour in graph[m]:
            if neighbour not in visted:
                visited.append(neighbour)
                quece.append(neighbour)
print("following is breadth first serch")
bfs()
