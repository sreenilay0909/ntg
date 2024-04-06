graph ={0:[1,2],
        1:[3,4],
        2:[5,6],
        3:[],
        4:[],
        5:[],
        6:[]
        }
count=0
for node in graph:
    print(node, graph[node])
    if graph[node]:
        for n in graph[node]:
            print(n)
    else:
        count=count+1
